# quiz_game.py
# Main logic for the quiz game

import random
from questions import quiz_data

def display_welcome():
    print("\nWelcome to the Quiz Game!")
    print("Pick a category and answer questions.\n")

def display_categories():
    print("Categories:")
    count = 1
    for category in quiz_data.keys():
        print(str(count) + ". " + category)
        count = count + 1
    return list(quiz_data.keys())

def get_user_category(categories):
    while True:
        choice = input("\nPick a category number: ")
        choice = int(choice)  # Assumes input is a number
        if 1 <= choice <= len(categories):
            return categories[choice - 1]
        print("Wrong number, try again.")

def display_question(question_data):
    print("\nQuestion: " + question_data['question'])
    for option in question_data['options']:
        print(option + " - " + question_data['options'][option])

def get_user_answer():
    while True:
        answer = input("\nYour answer (a, b, c, d): ")
        answer = answer.lower()
        if answer in ['a', 'b', 'c', 'd']:
            return answer
        print("Type a, b, c, or d only!")

def check_answer(user_answer, correct_answer, explanation):
    if user_answer == correct_answer:
        print("\nRight answer!")
        return 1
    else:
        print("\nWrong! Correct answer was " + correct_answer)
        print("Why: " + explanation)
        return 0

def main():
    display_welcome()
    score = 0
    total_questions = 0

    while True:
        categories = display_categories()
        chosen_category = get_user_category(categories)
        question = random.choice(quiz_data[chosen_category])
        
        display_question(question)
        user_answer = get_user_answer()
        score = score + check_answer(user_answer, question['correct'], question['explanation'])
        total_questions = total_questions + 1
        
        play_again = input("\nAnother question? (yes/no): ")
        if play_again != "yes":
            break
    
    print("\nGame Over!")
    print("Score: " + str(score) + "/" + str(total_questions))
    percentage = (score / total_questions) * 100 if total_questions > 0 else 0
    print("Percentage: " + str(percentage) + "%")

if __name__ == "__main__":
    main()