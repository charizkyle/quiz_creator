def create_quiz():
    quiz_title = input("Enter the quiz title: ")
    quiz_description = input("Enter the quiz description: ")

    question_counter = 1
    while True:
        print(f"\nQuestion {question_counter}:")
        question_text = input("Enter the question: ")
        print("Enter 4 options:")
        a = input("a) ")
        b = input("b) ")
        c = input("c) ")
        d = input("d) ")

        print("Do you want to add another question? (yes/no): ", end="")
        continue_choice = input().strip().lower()
        if continue_choice == 'no':
            break
        question_counter += 1

create_quiz()