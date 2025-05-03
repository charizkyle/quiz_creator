# Import necessary libraries
import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
import json
import os
from PIL import Image, ImageTk

# ---------- SETUP ----------
root = tk.Tk()
root.title("Quizzy Crafter Simulator")
root.geometry("800x600")
root.resizable(False, False)

# Set a directory for quizzes
QUIZ_FOLDER = "quizzes"
RESULTS_FOLDER = "quiz_results"
os.makedirs(QUIZ_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

# Load Background Images
start_bg = ImageTk.PhotoImage(Image.open("assets/start_bg.png").resize((800, 600)))
create_bg = ImageTk.PhotoImage(Image.open("assets/create_bg.png").resize((800, 600)))
take_bg = ImageTk.PhotoImage(Image.open("assets/take_bg.png").resize((800, 600)))

# Load Button Images
def load_button_image(path):
    img = Image.open(path).convert("RGBA")
    return ImageTk.PhotoImage(img.resize((200, 60)))

button_images = {
    "create": load_button_image("assets/create_button.png"),
    "take": load_button_image("assets/take_button.png"),
    "next": load_button_image("assets/next_button.png"),
    "add_question": load_button_image("assets/add_question_button.png"),
    "save": load_button_image("assets/save_button.png")
}

# Load Font
custom_font = tkFont.Font(family="consolas", size=14)

# Create a function to switch between frames
current_frame = None

def switch_frame(new_frame):
    global current_frame
    if current_frame:
        current_frame.destroy()
    current_frame = new_frame
    current_frame.pack(fill="both", expand=True)

# ---------- QUIZ MANAGER ----------
# Implement a Quiz Manager
class QuizManager:
    # Store basic quiz information
    def __init__(self):
        self.title = ""
        self.description = ""
        self.questions = [] # Store questions being added

    # Reset the quiz if the user wants to start over
    def reset(self):
        self.title = ""
        self.description = ""
        self.questions = []

    # Save quiz data to a JSON file
    def save_quiz(self):
        filename = os.path.join(QUIZ_FOLDER, f"{self.title.replace(' ', '_')}.json")
        data = {
            "title": self.title,
            "description": self.description,
            "questions": self.questions
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    # Load existing quizzes
    def load_quiz(self, filename):
        with open(os.path.join(QUIZ_FOLDER, filename), 'r') as f:
            data = json.load(f)
        self.title = data['title']
        self.description = data['description']
        self.questions = data['questions']

quiz_manager = QuizManager()

# ---------- SCREENS ----------

# Set up the main screen
def start_menu():
    frame = tk.Frame(root)
    tk.Label(frame, image=start_bg).place(x=0, y=0, relwidth=1, relheight=1)

    # Add "Create Quiz" and "Take Quiz" buttons to the main screen
    tk.Button(frame, image=button_images["create"], command=lambda: create_quiz(), borderwidth=0, bg="#1f628e").place(x=300, y=430)
    tk.Button(frame, image=button_images["take"], command=lambda: take_quiz(), borderwidth=0, bg="#1f628e").place(x=300, y=510)

    switch_frame(frame)

# Show "Create Quiz" Screen
def create_quiz():
    quiz_manager.reset() # to start over
    frame = tk.Frame(root)
    tk.Label(frame, image=create_bg).place(x=0, y=0, relwidth=1, relheight=1)

    # Create Quiz Title and Description Entry Fields
    tk.Label(frame, text="Quiz Title:", font=custom_font, bg="#004477", fg="white").place(x=20, y=120)
    title_entry = tk.Entry(frame, font=custom_font, width=40, bg="#004477", fg="light pink")
    title_entry.place(x=180, y=120)

    tk.Label(frame, text="Description:", font=custom_font, bg="#004477", fg="white").place(x=20, y=180)
    desc_entry = tk.Entry(frame, font=custom_font, width=40, bg="#004477", fg="light pink")
    desc_entry.place(x=180, y=180)

    # Store input into QuizManager
    def proceed():
        quiz_manager.title = title_entry.get()
        quiz_manager.description = desc_entry.get()
        enter_questions()

    # Add a "Next" button to proceed to the question input screen
    tk.Button(frame, image=button_images["next"], command=lambda: proceed(), borderwidth=0, bg="#1f628e").place(x=300, y=430)

    switch_frame(frame)

# Add input fields for question, options, and correct answer
def enter_questions():
    frame = tk.Frame(root)
    tk.Label(frame, image=create_bg).place(x=0, y=0, relwidth=1, relheight=1)

    entries = []
    labels = ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Answer \n(a/b/c/d)"]
    y_positions = [150, 210, 260, 310, 360, 410]

    for idx, text in enumerate(labels):
        tk.Label(frame, text=text, font=custom_font, bg="#004477", fg="white").place(x=20, y=y_positions[idx])
        entry = tk.Entry(frame, width=50, font=custom_font, bg="#004477", fg="light pink")
        entry.place(x=200, y=y_positions[idx])
        entries.append(entry)

    # Add each typed-in questions to quiz_manager.questions
    def add_question():
        question_text = entries[0].get()
        options = [entries[i].get() for i in range(1, 5)]
        correct_answer = entries[5].get().lower()
        if question_text and all(options) and correct_answer:
            quiz_manager.questions.append({
                "question": question_text,
                "options": options,
                "answer": correct_answer
            })
            for entry in entries:
                entry.delete(0, tk.END)

    # Finalize the quiz
    def save():
        add_question()
        quiz_manager.save_quiz()
        start_menu()

    # Add “Add Question” and “Save” buttons
    tk.Button(frame, image=button_images["add_question"], command=lambda: add_question(), borderwidth=0, bg="#1f628e").place(x=100, y=500)
    tk.Button(frame, image=button_images["save"], command=lambda: save(), borderwidth=0, bg="#1f628e").place(x=500, y=500)

    switch_frame(frame)

# Show "Take Quiz" Screen
def take_quiz():
    frame = tk.Frame(root)
    tk.Label(frame, image=take_bg).place(x=0, y=0, relwidth=1, relheight=1)

    # Add name entry field
    tk.Label(frame, text="Enter your name:", font=custom_font, bg="#004477", fg="white").place(x=20, y=250)
    name_entry = tk.Entry(frame, width=40, font=custom_font, bg="#004477", fg="light pink")
    name_entry.place(x=180, y=300)

    # Load existing quizzes
    def show_quizzes(user_name):
        quiz_files = [f for f in os.listdir(QUIZ_FOLDER) if f.endswith('.json')]
        if not quiz_files:
            messagebox.showinfo("No Quizzes", "No quizzes available.")
            start_menu()
            return

    # Validate the name entry
    def start():
        user_name = name_entry.get()
        if not user_name:
            messagebox.showwarning("Name Required", "Please enter your name.")
            return
        show_quizzes(user_name)

    tk.Button(frame, image=button_images["next"], command=lambda: start(), borderwidth=0, bg="#1f628e").place(x=300, y=450)

    switch_frame(frame)

# Start Quiz Questions
def start_quiz_questions(user_name):
    frame = tk.Frame(root)
    tk.Label(frame, image=take_bg).place(x=0, y=0, relwidth=1, relheight=1)

    question_index =[0]
    selected_answer = [None]
    user_answers = []

    question_label = tk.Label(frame, text="", font=custom_font, bg="#004477", fg="light pink", wraplength=700)
    question_label.place(x=50, y=120)

    option_buttons = []

    for i in range(4):
        btn = tk.Button(frame, width=50, font=custom_font, bg="#004477", fg="light pink", anchor='w')
        btn.place(x=150, y=180 + i * 55)
        option_buttons.append(btn)

    # Display current question and its options
    def load_question():
        current_question = quiz_manager.questions[question_index[0]]
        question_label.config(text=current_question["question"])
        for idx, option in enumerate(current_question["options"]):
            option_buttons[idx].config(text=f"{chr(97 + idx)} {option}", command=lambda i=idx: select_answer(i))

    # Stores the selected answer letter
    def select_answer(idx):
        selected_answer[0] = chr(97 + idx)
        for i, btn in enumerate(option_buttons):
            if i == idx:
                btn.config(bg="white", fg="#004477")
            else:
                btn.config(bg="#004477", fg="light pink")

    # Proceed to the next question of the quiz
    def next_question():
        user_answers.append({
            "question": quiz_manager.questions[question_index[0]]["question"],
            "answer": selected_answer[0]
        })
        selected_answer[0] = None
        question_index[0] += 1
        if question_index[0] >= len(quiz_manager.questions):
            print("End of quiz")
        else:
            load_question()

# ---------- START ----------
# Start the application
start_menu()
root.mainloop()