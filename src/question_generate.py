from openai import OpenAI
import json
import random
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)

client = OpenAI(api_key=OPENAI_API_KEY)

prompt = \
"""
Your goal is to create questions based off a transcript of a video and enhance learning through ACTIVE RECALL
Make sure that your question can be answered based off the audio and not any subjectivity.
Try not to ask repeat questions and FOCUS ON questions/topics that haven't yet been asked.
DO NOT contradict the video. Questions generated should be COLLEGE level difficulty, like preparing a student for a test.
Try not to make the right answer too obvious. For example, making the right answer the longest answer everytime.
These questions should reward paying attention to the video's topics.

Generate ONE multiple-choice question based on the text below.

Return ONLY valid JSON in this format:
{
  "question": "string",
  "options": ["string", "string", "string", "string"],
  "answer": "string"
}
"""

#The answer should be the EXACT same as the correct option string

input_history = []
current_response_id = None

def generate_question(audio):
    input_history.append({"role":"user", "content":audio})

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=prompt,
        store=False,
        input=input_history
    )

    input_history.append({"role":"assistant", "content":response.output_text})

    output = json.loads(response.output_text)
    random.shuffle(output["options"])

    return output

def chat_loop():
    for i in range(5):
        user_input = input("Audio: ")
        question_data = generate_question(user_input)
        print(question_data)