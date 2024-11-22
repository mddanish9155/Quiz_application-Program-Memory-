import random

py_q = {
    "DSA": {
        1: ["What does DSA stand for?", "Data Science Analysis", "Data Structure and Algorithms", "Data Security Administration", "Data System Analysis", 2],
        2: ["Which of the following is not a data structure?", "Array", "Stack", "Queue", "Function", 4],
        3: ["What is the time complexity of binary search?", "O(n)", "O(log n)", "O(n log n)", "O(1)", 2],
        4: ["What is the worst-case time complexity of bubble sort?", "O(n)", "O(n^2)", "O(log n)", "O(n log n)", 2],
        5: ["Which data structure uses LIFO?", "Queue", "Stack", "Array", "Linked List", 2]
    },
    "DBMS": {
        1: ["What does DBMS stand for?", "Database Management System", "Data Backup Management System", "Database Maintenance System", "Data Management System", 1],
        2: ["Which of the following is a type of database?", "Relational", "Flat File", "Hierarchical", "All of the above", 4],
        3: ["What is SQL used for?", "Data Manipulation", "Data Definition", "Data Control", "All of the above", 4],
        4: ["What does ACID stand for?", "Atomicity, Consistency, Isolation, Durability", "Accuracy, Consistency, Isolation, Durability", "Atomicity, Consistency, Isolation, Delivery", "Atomicity, Consistency, Integrity, Durability", 1],
        5: ["Which SQL statement is used to retrieve data?", "GET", "SELECT", "PICK", "RETRIEVE", 2]
    },
    "Python": {
        1: ["What is the output of print(2 ** 3)?", "6", "8", "9", "4", 2],
        2: ["Which keyword is used to define a function in Python?", "function", "def", "func", "define", 2],
        3: ["What data type is the result of 3 / 2?", "Integer", "Float", "String", "Complex", 2],
        4: ["What is a lambda function?", "A type of loop", "A small anonymous function", "A built-in function", "A type of error", 2],
        5: ["Which of the following is a mutable type?", "Tuple", "List", "String", "Dictionary", 2]
    }
}

users = {}

def display_banner():
    print("=================================")
    print("          QUIZ APPLICATION       ")
    print("=================================")

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = password
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def shuffle_questions(questions):
    """Shuffle only the sequence of questions."""
    question_ids = list(questions.keys())
    random.shuffle(question_ids)
    shuffled_questions = {}

    for new_id, old_id in enumerate(question_ids, start=1):
        shuffled_questions[new_id] = questions[old_id]

    return shuffled_questions

def attempt_quiz(selected_topic):
    score = 0
    total_questions = 5
    questions = shuffle_questions(py_q[selected_topic])
    question_results = {}

    for q_id in questions:
        question_data = questions[q_id]
        print(f"\nQ{q_id}: {question_data[0]}")
        for idx, option in enumerate(question_data[1:5], start=1):
            print(f"{idx}. {option}")

        answer = input("Select your answer (1-4): ")
        
        if int(answer) == question_data[5]:
            print("Correct!")
            score += 1
            question_results[q_id] = ("Correct", None)
        else:
            print("Wrong answer.")
            question_results[q_id] = ("Wrong", question_data[5])  # Store the correct answer

    print(f"\nYour score for {selected_topic}: {score}/{total_questions}")
    
    # Show correct answers for questions the user got wrong
    print("\nQuestions Review:")
    for q_id, (result, correct_answer) in question_results.items():
        if result == "Wrong":
            print(f"Q{q_id}: Correct answer was: {questions[q_id][correct_answer]}")

    return score

def show_result(results):
    print("\nFinal Results:")
    for topic, score in results.items():
        print(f"{topic}: {score}/5")
    print("Thank you for participating!")

def main():
    while True:
        display_banner()
        print("1. Registration")
        print("2. Login")
        print("3. Exit Quiz")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            if login():
                print("Select a topic to attempt:")
                print("1. DSA")
                print("2. DBMS")
                print("3. Python")
                
                topic_choice = input("Enter your choice (1-3): ")
                topics = ["DSA", "DBMS", "Python"]
                
                if topic_choice in ['1', '2', '3']:
                    selected_topic = topics[int(topic_choice) - 1]
                    score = attempt_quiz(selected_topic)
                    show_result({selected_topic: score})
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting the quiz. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
