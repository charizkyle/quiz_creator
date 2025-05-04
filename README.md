🎮 **Quizzy Crafter**

Quizzy Crafter is a simple yet fun GUI-based application that allows users to create and take quizzes with ease. Whether you're a student, teacher, or trivia enthusiast, this app provides a visually appealing way to craft and enjoy quizzes.

🧰 **Features:*
-   📝 Create custom quizzes with questions and multiple choices
-   🎯 Take quizzes and get your score instantly
-   💾 Saves quizzes and results in neatly organized folders
-   🖼️ Uses a colorful and engaging GUI built with Tkinter and PIL

🛠️ **Requirements**

Make sure the following are set up before running the app:
- Python 3 installed
- Pillow library (PIL fork) for handling images in the GUI

📦 **Installing Pillow**

You need to install Pillow in your terminal (or command prompt) before running the application. Here's how:
1. Open Terminal (or Command Prompt on Windows, or the Terminal panel in VS Code).
2. Run this command: pip install pillow

⚠️ Without Pillow installed, running the app will raise an ImportError, and image components like buttons and backgrounds won't display properly.

📂 **Setup Instructions**
1. **Download Assets:* Make sure to download all the files inside the **assets/** folder. These include the GUI images such as buttons, backgrounds, and custom text visuals required for the interface to display correctly.
2. Run the main Python file using the terminal: **python quizzy_crafter_final.py**

📁 **Folder Structure**

quiz_creator/

├── assets/                  # Required image assets for the GUI

├── quizzes/                 # Contains created quizzes (JSON)

├── quiz_results/            # Contains quiz results (JSON)

├── quizzy_crafter_final.py  # Main script to run the application

└── README.md                # This file

- The **quizzes/** folder stores all quizzes created using the app.
- The **quiz_results/** folder stores results when a quiz is taken.
- **These folders are automatically created if they don't already exist.**
