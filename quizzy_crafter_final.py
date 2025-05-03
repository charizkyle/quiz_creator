# Import necessary libraries
import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk

# ---------- SETUP ----------
root = tk.Tk()
root.title("Quizzy Crafter Simulator")
root.geometry("800x600")
root.resizable(False, False)

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

    # Reset the quiz if the user wants to start over
    def reset(self):
        self.title = ""
        self.description = ""

quiz_manager = QuizManager()

# ---------- SCREENS ----------

# Set up the main screen
def start_menu():
    frame = tk.Frame(root)
    tk.Label(frame, image=start_bg).place(x=0, y=0, relwidth=1, relheight=1)

    # Add "Create Quiz" and "Take Quiz" buttons to the main screen
    tk.Button(frame, image=button_images["create"], command=lambda: create_quiz(), borderwidth=0, bg="#004477").place(x=300, y=430)
    tk.Button(frame, image=button_images["take"], command=lambda: take_quiz(), borderwidth=0, bg="#004477").place(x=300, y=510)

    switch_frame(frame)

# Show "Create Quiz" Screen
def create_quiz():
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

    # Add a "Next" button to proceed to the question input screen
    tk.Button(frame, image=button_images["next"], command=lambda: proceed(), borderwidth=0, bg="#004477").place(x=300, y=430)

    switch_frame(frame)

# Add input fields for quiz questions, options, and correct answers
def enter_questions():
    frame = tk.Label(root)
    tk.Label(frame, image=create_bg).place(x=0, y=0, relwidth=1, relheight=1)

    entries = []
    labels = ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Answer"]
    y_positions = [120, 180, 240, 300, 360, 420]

    for idx, text in enumerate(labels):
        tk.Label(frame, text=text, font=cutom_font, bg="004477", fg="white").place(x=20, y=y_positions[idx])
        entry = tk.Entry(frame, width=40, font=custom_font, bg="#004477", fg="light pink")
        entry.place(x=180, y=y_positions[idx])
        entries.append(entry)

# Show "Take Quiz" Screen
def take_quiz():
    frame = tk.Frame(root)
    tk.Label(frame, image=take_bg).place(x=0, y=0, relwidth=1, relheight=1)

    switch_frame(frame)

# ---------- START ----------
# Start the application
start_menu()
root.mainloop()