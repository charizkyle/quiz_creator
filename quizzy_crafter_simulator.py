import tkinter as tk
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

current_frame = None

# ---------- SCREENS ----------

# Set up the main screen
def start_menu():
    frame = tk.Frame(root)
    tk.Label(frame, image=start_bg).place(x=0, y=0, relwidth=1, relheight=1)
    
    switch_frame(frame)
# ---------- START ----------
# Start the application
start_menu()
root.mainloop()