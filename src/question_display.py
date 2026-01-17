import tkinter as tk
from tkinter import messagebox
import threading



current_question = None
answered_event = threading.Event()

root = tk.Tk()
root.geometry("1000x500")

selected_option = tk.StringVar()
radio_buttons = []
label = tk.Label(root, font=("Arial", 15), text="Question Label", wraplength=600)
label.pack(pady=20)
root.withdraw()

for _ in range(4):
    rb = tk.Radiobutton(
        root,
        text="Choice",
        variable=selected_option,
        font=("Arial", 12)
    )
    rb.pack(pady=4)
    radio_buttons.append(rb)

def get_answered_event():
    return answered_event

def submit_answer():
    answer = selected_option.get()
    if answer == current_question["answer"]:
        messagebox.showinfo("Result", "Correct!!!")
        answered_event.set()
        root.withdraw()
    else:
        messagebox.showerror("Result", "Incorrect!")

submit_button = tk.Button(
    root,
    text="Submit",
    command=submit_answer
)
submit_button.pack(pady="15")

def load_question(question_data):
    global current_question
    current_question = question_data
    selected_option.set("")
    root.title("Question")
    bring_to_front()
    label.config(text=question_data["question"])
    for i, rb in enumerate(radio_buttons):
        option = question_data["options"][i]
        rb.config(text=option, value=option)

def bring_to_front():
    root.deiconify()
    root.lift()                    # raise above other windows
    root.attributes("-topmost", True)   # make it topmost...
    root.after(1600, lambda: root.attributes("-topmost", False))  # ...then normal again
    #root.focus_force()             # try to force keyboard focus        


def run_loop():
    root.mainloop()