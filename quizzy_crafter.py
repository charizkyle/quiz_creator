def create_quiz():
    print("Welcome to Quizzy Crafter!")
    quiz_title = input("Enter the quiz title: ")
    quiz_description = input("Enter the quiz description: ")

    with open(f"{quiz_title.replace(' ', '_')}_quiz.txt", "w") as file:
        file.write(f"Title: {quiz_title}\n")
        file.write(f"Description: {quiz_description}\n")
        file.write("-" * 50 + "\n")

        question_counter = 1
        while True:
            print(f"\nQuestion {question_counter}:")
            question_text = input("Enter a question: ")
            print("Enter 4 options:")
            a = input("a) ")
            b = input("b) ")
            c = input("c) ")
            d = input("d) ")

            correct_answer = input("Enter the correct answer (a, b, c, d): ").lower()
            while correct_answer not in ['a', 'b', 'c', 'd']:
                print("Invalid answer choice. Please enter a, b, c, or d.")
                correct_answer = input("Enter the correct answer (a, b, c, d): ").lower()

            file.write(f"Q{question_counter}: {question_text}\n")
            file.write(f"a) {a}\n")
            file.write(f"b) {b}\n")
            file.write(f"c) {c}\n")
            file.write(f"d) {d}\n")
            file.write(f"Correct Answer: {correct_answer}\n")
            file.write("-" * 50 + "\n")

            print("Do you want to add another question? (yes/no): ", end="")
            continue_choice = input().strip().lower()
            if continue_choice == 'no':
                break
            question_counter += 1

create_quiz()