def create_quiz():
    print("Welcome to Quizzy Crafter!")
    quiz_title = input("Enter the quiz title: ")
    quiz_description = input("Enter the quiz description: ")

    file_name = f"{quiz_title.replace(' ', '_')}_quiz.txt"
    with open(file_name, "w") as quiz_file:
        quiz_file.write(f"Title: {quiz_title}\n")
        quiz_file.write(f"Description: {quiz_description}\n")
        quiz_file.write("-" * 50 + "\n")

        question_counter = 1
        while True:
            print(f"\nQuestion {question_counter}:")
            question_text = input("Enter a question: ")
            
            print("Enter 4 options:")
            option_a = input("a) ")
            option_b = input("b) ")
            option_c = input("c) ")
            option_d = input("d) ")

            correct_option = input("Enter the correct answer (a, b, c, d): ").lower()
            while correct_option not in ['a', 'b', 'c', 'd']:
                print("Invalid answer choice. Please enter a, b, c, or d.")
                correct_option = input("Enter the correct answer (a, b, c, d): ").lower()

            quiz_file.write(f"Q{question_counter}: {question_text}\n")
            quiz_file.write(f"a) {option_a}\n")
            quiz_file.write(f"b) {option_b}\n")
            quiz_file.write(f"c) {option_c}\n")
            quiz_file.write(f"d) {option_d}\n")
            quiz_file.write(f"Correct Answer: {correct_option}\n")
            quiz_file.write("-" * 50 + "\n")

            continue_choice = input("Do you want to add another question? (yes/no): ").strip().lower()
            if continue_choice == 'no':
                break

            question_counter += 1

create_quiz()