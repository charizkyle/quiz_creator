import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class QuizzyCrafter:
    def __init__(self, root):
        self.root = root
        self.root.title("Quizzy Crafter")
        self.root.geometry("600x600")
        self.root.resizable(False, False)


        self.quiz_file = None
        self.question_counter = 1


        self.start_screen()


    def start_screen(self):
        self.clear_window()


        bg = Image.open("start screen.png").resize((600, 600))
        self.bg_image = ImageTk.PhotoImage(bg)
        tk.Label(self.root, image=self.bg_image).place(x=0, y=0, relwidth=1, relheight=1)


        tk.Button(self.root, text="Start a Quiz", font=("Arial", 14), command=self.init_quiz_inputs).place(relx=0.5, rely=0.7, anchor="center")
        tk.Button(self.root, text="Exit", font=("Arial", 14), command=self.root.quit).place(relx=0.5, rely=0.8, anchor="center")


    def init_quiz_inputs(self):
        self.clear_window()


        bg = Image.open("main bg.png").resize((600, 600))
        self.bg_image = ImageTk.PhotoImage(bg)
        tk.Label(self.root, image=self.bg_image).place(x=0, y=0, relwidth=1, relheight=1)


        # Center quiz title/description
        frame = tk.Frame(self.root, bg="#004477")
        frame.place(relx=0.5, rely=0.4, anchor="center")


        tk.Label(frame, text="Quiz Title:", font=("Arial", 12), bg="#004477", fg="white").grid(row=0, column=0, sticky="w", pady=5)
        self.title_entry = tk.Entry(frame, width=40)
        self.title_entry.grid(row=0, column=1, pady=5)


        tk.Label(frame, text="Description:", font=("Arial", 12), bg="#004477", fg="white").grid(row=1, column=0, sticky="w", pady=5)
        self.desc_entry = tk.Entry(frame, width=40)
        self.desc_entry.grid(row=1, column=1, pady=5)


        tk.Button(frame, text="Create Quiz", command=self.main_screen).grid(row=2, column=0, columnspan=2, pady=10)


    def main_screen(self):
        title = self.title_entry.get()
        desc = self.desc_entry.get()


        if not title or not desc:
            messagebox.showerror("Missing Info", "Please enter both title and description.")
            return


        self.quiz_file = open(f"{title.replace(' ', '_')}_quiz.txt", "w")
        self.quiz_file.write(f"Title: {title}\nDescription: {desc}\n{'-'*50}\n")


        self.clear_window()


        bg = Image.open("main bg.png").resize((600, 600))
        self.bg_image = ImageTk.PhotoImage(bg)
        tk.Label(self.root, image=self.bg_image).place(x=0, y=0, relwidth=1, relheight=1)


        # Center input form
        self.form_frame = tk.Frame(self.root, bg="#004477")
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center")


        self.question_label = tk.Label(self.form_frame, text=f"Question {self.question_counter}:", font=("Arial", 12), bg="#004477", fg="white")
        self.question_label.grid(row=0, column=0, columnspan=2, pady=(0, 5), sticky="w")


        self.question_entry = tk.Entry(self.form_frame, width=50)
        self.question_entry.grid(row=1, column=0, columnspan=2, pady=5)


        self.options = {}
        for idx, opt in enumerate(['a', 'b', 'c', 'd']):
            tk.Label(self.form_frame, text=f"{opt})", bg="#004477", fg="white", font=("Arial", 10)).grid(row=2+idx, column=0, sticky="w", padx=10)
            self.options[opt] = tk.Entry(self.form_frame, width=40)
            self.options[opt].grid(row=2+idx, column=1, pady=2)


        tk.Label(self.form_frame, text="Correct Answer (a/b/c/d):", font=("Arial", 12), bg="#004477", fg="white").grid(row=6, column=0, pady=10, sticky="w")
        self.correct_entry = tk.Entry(self.form_frame, width=5)
        self.correct_entry.grid(row=6, column=1, sticky="w")


        # Buttons
        tk.Button(self.root, text="Add a Question", font=("Arial", 12), command=self.add_question).place(x=20, y=550)
        tk.Button(self.root, text="Finish Quiz", font=("Arial", 12), command=self.finish_quiz).place(x=480, y=550)


    def add_question(self):
        q = self.question_entry.get()
        opts = {k: v.get() for k, v in self.options.items()}
        correct = self.correct_entry.get().strip().lower()


        if not q or any(not val for val in opts.values()) or correct not in opts:
            messagebox.showerror("Invalid Input", "Please fill out all fields correctly.")
            return


        # Write immediately to file
        self.quiz_file.write(f"Q{self.question_counter}: {q}\n")
        for k, v in opts.items():
            self.quiz_file.write(f"{k}) {v}\n")
        self.quiz_file.write(f"Correct Answer: {correct}\n{'-'*50}\n")


        self.question_counter += 1
        self.update_question_form()


    def update_question_form(self):
        self.question_label.config(text=f"Question {self.question_counter}:")
        self.question_entry.delete(0, tk.END)
        self.correct_entry.delete(0, tk.END)
        for entry in self.options.values():
            entry.delete(0, tk.END)


    def finish_quiz(self):
        if self.quiz_file:
            self.quiz_file.close()
        messagebox.showinfo("Quiz Saved", "Your quiz has been saved successfully!")
        self.start_screen()


    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Start App
root = tk.Tk()
app = QuizzyCrafter(root)
root.mainloop()