def create_quiz():
    # ask for quiz title and description
    quiz_title = input("Enter the quiz title: ")
    quiz_description = input("Enter the quiz description: ")

    print(f"\nCreating quiz: {quiz_title}")
    print(f"Description: {quiz_description}")

create_quiz()