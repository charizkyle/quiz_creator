# Import necessary libraries
import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
import json
import os
from PIL import Image, ImageTk
import winsound
import random

# ---------- SETUP ----------
root = tk.Tk()
root.title("Quizzy Crafter Simulator")
root.geometry("800x600")
root.resizable(False, False)

# Set directories for quizzes and quiz results
QUIZ_FOLDER = "quizzes"
RESULTS_FOLDER = "quiz_results"
os.makedirs(QUIZ_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

# Load Background Images
start_bg = ImageTk.PhotoImage(Image.open("assets/start_bg.png").resize((800, 600)))
create_bg = ImageTk.PhotoImage(Image.open("assets/create_bg.png").resize((800, 600)))
take_bg = ImageTk.PhotoImage(Image.open("assets/take_bg.png").resize((800, 600)))
score_bg = ImageTk.PhotoImage(Image.open("assets/score_bg.png").resize((800, 600)))

# Load Button Images
def load_button_image(path):
    img = Image.open(path).convert("RGBA")
    return ImageTk.PhotoImage(img.resize((200, 60)))

button_images = {
    "create": load_button_image("assets/create_button.png"),
    "take": load_button_image("assets/take_button.png"),
    "next": load_button_image("assets/next_button.png"),
    "add_question": load_button_image("assets/add_question_button.png"),
    "save": load_button_image("assets/save_button.png"),
    "back": load_button_image("assets/back_button.png"),
    "submit": load_button_image("assets/submit_button.png"),
}

# Load Font
custom_font = tkFont.Font(family="consolas", size=14)

# Global State
current_frame = None

def switch_frame(new_frame):
    global current_frame
    if current_frame:
        current_frame.destroy()
    current_frame = new_frame
    current_frame.pack(fill="both", expand=True)

# Load Sound Effects
def play_click_sound():
    winsound.PlaySound("assets/click.wav", winsound.SND_FILENAME)

# ---------- QUIZ MANAGER ----------
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
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    # Load existing quizzes
    def load_quiz(self, filename):
        with open(os.path.join(QUIZ_FOLDER, filename), 'r') as file:
            data = json.load(file)
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
    tk.Button(frame, image=button_images["create"], command=lambda: [play_click_sound(), create_quiz()], borderwidth=0, bg="#1f628e").place(x=300, y=430)
    tk.Button(frame, image=button_images["take"], command=lambda: [play_click_sound(), take_quiz()], borderwidth=0, bg="#1f628e").place(x=300, y=510)

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
    tk.Button(frame, image=button_images["next"], command=lambda: [play_click_sound(), proceed()], borderwidth=0, bg="#1f628e").place(x=300, y=430)

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
        options = [entries[idx].get() for idx in range(1, 5)]
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
    tk.Button(frame, image=button_images["add_question"], command=lambda: [play_click_sound(), add_question()], borderwidth=0, bg="#1f628e").place(x=100, y=500)
    tk.Button(frame, image=button_images["save"], command=lambda: [play_click_sound(), save()], borderwidth=0, bg="#1f628e").place(x=500, y=500)

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
        quiz_files = [file for file in os.listdir(QUIZ_FOLDER) if file.endswith('.json')]
        if not quiz_files:
            messagebox.showinfo("No Quizzes", "No quizzes available.")
            start_menu()
            return
        
        # Add quiz selection
        quiz_selection_frame = tk.Frame(root)
        tk.Label(quiz_selection_frame, image=take_bg).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(quiz_selection_frame, text="Select a Quiz:", font=custom_font, bg="#004477", fg="white").pack(pady=150)

        def select_quiz(filename):
            quiz_manager.load_quiz(filename)
            start_quiz_questions(user_name)

        # Scrollable list of quizzes
        canvas = tk.Canvas(quiz_selection_frame, bg="#004477", highlightthickness=0)
        scrollbar = tk.Scrollbar(quiz_selection_frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#004477")

        scroll_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Add quiz buttons to the scrollable frame
        for quiz in quiz_files:
            btn = tk.Button(scroll_frame, text=quiz.replace("_quiz.json", ""), font=custom_font,
                            command=lambda quiz_file=quiz: [play_click_sound(), select_quiz(quiz_file)], bg="#004477", fg="light pink")
            btn.pack(pady=5, padx=20, anchor="center")

        # Place canvas and scrollbar
        canvas.place(x=50, y=200, width=700, height=300)
        scrollbar.place(x=750, y=200, height=300)

        tk.Button(quiz_selection_frame, image=button_images["back"], command=lambda: [play_click_sound(), start_menu()], borderwidth=0, bg="#1f628e").place(x=300, y=500)

        switch_frame(quiz_selection_frame)

    # Validate the name entry
    def start():
        user_name = name_entry.get()
        if not user_name:
            messagebox.showwarning("Name Required", "Please enter your name.")
            return
        show_quizzes(user_name)

    tk.Button(frame, image=button_images["next"], command=lambda: [play_click_sound(), start()], borderwidth=0, bg="#1f628e").place(x=300, y=450)

    switch_frame(frame)

# Start Quiz Questions
def start_quiz_questions(user_name):
    frame = tk.Frame(root)
    tk.Label(frame, image=take_bg).place(x=0, y=0, relwidth=1, relheight=1)

    random.shuffle(quiz_manager.questions)  # Shuffle questions

    question_index =[0]
    selected_answer = [None]
    score = [0] # Store score as a list to modify it inside functions
    user_answers = []

    question_label = tk.Label(frame, text="", font=custom_font, bg="#004477", fg="light pink", wraplength=700)
    question_label.place(x=50, y=120)

    option_buttons = []

    for idx in range(4):
        btn = tk.Button(frame, width=50, font=custom_font, bg="#004477", fg="light pink", anchor='w')
        btn.place(x=150, y=180 + idx * 55)
        option_buttons.append(btn)

    # Display current question and its options
    def load_question():
        current_question = quiz_manager.questions[question_index[0]]
        question_label.config(text=current_question["question"])
        for idx, option in enumerate(current_question["options"]):
            option_buttons[idx].config(text=f"{chr(97+idx)}) {option}", command=lambda opt_idx=idx: select_answer(opt_idx))

    # Stores the selected answer letter
    def select_answer(idx):
        selected_answer[0] = chr(97 + idx)
        for btn_idx, btn in enumerate(option_buttons):
            if btn_idx == idx:
                btn.config(bg="white", fg="#004477")
            else:
                btn.config(bg="#004477", fg="light pink")
        play_click_sound()

    # Proceed to the next question of the quiz
    def next_question():
        if selected_answer[0] == quiz_manager.questions[question_index[0]]["answer"]:
            score[0] += 1 # Increment score if the answer is correct
        user_answers.append({
            "question": quiz_manager.questions[question_index[0]]["question"],
            "answer": selected_answer[0]
        })
        selected_answer[0] = None
        question_index[0] += 1
        if question_index[0] >= len(quiz_manager.questions):
            show_score(user_name, score[0], user_answers) # Show final score
        else:
            load_question()

    # Allow to move back to the previous question
    def prev_question():
        if question_index[0] > 0:
            question_index[0] -= 1
            load_question()

    # Add "Next" and "Back" buttons
    tk.Button(frame, image=button_images["next"], command=lambda: [play_click_sound(), next_question()], borderwidth=0, bg="#1f628e").place(x=500, y=500)
    tk.Button(frame, image=button_images["back"], command=lambda: [play_click_sound(), prev_question()], borderwidth=0, bg="#1f628e").place(x=100, y=500)

    load_question()
    switch_frame(frame)

# Show Score Screen
def show_score(user_name, score, user_answers):
    frame = tk.Frame(root)
    tk.Label(frame, image=score_bg).place(x=0, y=0, relwidth=1, relheight=1)

    # Adjust "Your Score:" to match the location of the pink bar
    title_label = tk.Label(
        frame,
        text=f"Your Score: {score}/{len(quiz_manager.questions)}",
        font=tkFont.Font(family="consolas", size=16),
        fg="white",
        bg="#e88e93",
    )
    title_label.place(x=310, y=50)

    # Scrollable frame for user answers
    canvas = tk.Canvas(frame, bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="white")

    scroll_frame.bind(
        "<Configure>",
        lambda _: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    for idx, user_answer in enumerate(user_answers):
        qtext = user_answer["question"]
        user_text = user_answer["answer"]
        correct_text = quiz_manager.questions[user_answers.index(user_answer)]["answer"]

        tk.Label(
            scroll_frame,
            text=f"Question{idx+1}: {qtext[:50]}...",
            font=tkFont.Font(family="consolas", size=10),
            bg="white",
            fg="lightpink"
        ).pack(anchor="w", pady=2)

        tk.Label(
            scroll_frame,
            text=f"Your answer: {user_text}",
            font=tkFont.Font(family="consolas", size=10),
            bg="white",
            fg="lightpink"
        ).pack(anchor="w", pady=2)

        color = "green" if user_text == correct_text else "red"
        tk.Label(
            scroll_frame,
            text=f"Correct: {correct_text}",
            font=tkFont.Font(family="consolas", size=10),
            bg="white",
            fg=color
        ).pack(anchor="w", pady=2)

    canvas.place(x=80, y=160, width=600, height=300)  # Adjust to fit inside the white bubble
    scrollbar.place(x=680, y=160, height=300)

    # Save Results
    def save_and_exit():
        result_path = os.path.join(RESULTS_FOLDER, f"{user_name}_quiz_results.txt")
        with open(result_path, "w") as file:
            file.write(f"User: {user_name}\nQuiz: {quiz_manager.title}\nScore: {score}/{len(quiz_manager.questions)}\n\n")
            # Show the summary of answers
            for answer in user_answers:
                file.write(f"Question: {answer['question']}\nYour Answer: {answer['answer']}\nCorrect Answer: {quiz_manager.questions[user_answers.index(answer)]['answer']}\n\n")
        start_menu()

    # Add "Submit" button to save the quiz results
    tk.Button(frame, image=button_images["submit"], command=lambda: [play_click_sound(), save_and_exit()], borderwidth=0, bg="#1f628e").place(x=300, y=500)   

    switch_frame(frame)

# ---------- START ----------
# Start the application
start_menu()
root.mainloop()