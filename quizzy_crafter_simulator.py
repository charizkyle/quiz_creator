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

# Load Button Images for the main screen
def load_button_image(path):
    img = Image.open(path).convert("RGBA")
    return ImageTk.PhotoImage(img.resize((200, 60)))

button_images = {
    "create": load_button_image("assets/create_button.png"),
    "take": load_button_image("assets/take_button.png"),
}

# Load Font
custom_font = tkFont.Font(family="Arial", size=14)

# Create a function to switch between frames
current_frame = None

def switch_frame(new_frame):
    global current_frame
    if current_frame:
        current_frame.destroy()
    current_frame = new_frame
    current_frame.pack(fill="both", expand=True)

# ---------- SCREENS ----------

# Set up the main screen
def start_menu():
    frame = tk.Frame(root)
    tk.Label(frame, image=start_bg).place(x=0, y=0, relwidth=1, relheight=1)

    # Add buttons to the main screen
    tk.Button(frame, image=button_images["create"], command=lambda: create_quiz(), borderwidth=0, bg="#004477").place(x=300, y=430)
    tk.Button(frame, image=button_images["take"], command=lambda: take_quiz(), borderwidth=0, bg="#004477").place(x=300, y=510)

    switch_frame(frame)

# Show "Create Quiz" Screen
def create_quiz():
    frame = tk.Frame(root)
    tk.Label(frame, image=create_bg).place(x=0, y=0, relwidth=1, relheight=1)

    # Create Quiz Title and Description Entry Fields
    tk.Label(frame, text="Quiz Title:", font=custom_font, bg="#004477", fg="white").place(x=50, y=50)
    title_entry = tk.Entry(frame, width=30, bg="#004477", fg="light pink")
    title_entry.place(x=150, y=50)

    tk.Label(frame, text="Description:", font=custom_font, bg="#004477", fg="white").place(x=50, y=100)
    desc_entry = tk.Entry(frame, width=30, bg="#004477", fg="light pink")
    desc_entry.place(x=150, y=100)

    switch_frame(frame)

# Show "Take Quiz" Screen
def take_quiz():
    frame = tk.Frame(root)
    tk.Label(frame, image=take_bg).place(x=0, y=0, relwidth=1, relheight=1)

    switch_frame(frame)

# ---------- START ----------
# Start the application
start_menu()
root.mainloop()