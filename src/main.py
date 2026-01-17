import audio_capture as ac
import audio_transcribe
import question_generate
import question_display
import threading

answered_event = question_display.get_answered_event()

def run():
    threading.Thread(target=process_data, daemon=True).start()
    question_display.run_loop()

def process_data():
    while True:
        result = ac.record_numpy()
        audio_transcribe.init()
        transcription = audio_transcribe.transcribe_numpy(result)
        question = question_generate.generate_question(transcription)
        question_display.load_question(question)
        print("Awaiting answer...")
        answered_event.wait()
        answered_event.clear()

if __name__ == "__main__":
    run()