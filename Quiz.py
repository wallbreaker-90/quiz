def display_welcome():
    menu = """
******************************
*                            *
*           WELCOME          *
*            TO              *
*           QUIZ             *
*           GAME             *
*                            *
*                            *
******************************
*       Press Enter        *"""
    print(menu)

def display_menu():
    menu = """
******************************
          1.play          
          2.Exit              
******************************
"""
    print(menu)


def play():
    questions = [
        "What is the chemical symbol for gold?",
        "Which planet is known as the Red Planet?",
        "What is the largest mammal in the world?",
        "Who wrote the play Romeo and Juliet?",
        "What is the capital city of France?",
        "Which planet is known as the Morning Star and Evening Star?"
    ]

    options = [
        ["A. Au", "B. Ag", "C. Fe", "D. Hg"],
        ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
        ["A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Rhinoceros"],
        ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Mark Twain"],
        ["A. Rome", "B. Berlin", "C. Madrid", "D. Paris"],
        ["A. Venus", "B. Mercury", "C. Mars", "D. Jupiter"]
    ]

    answers = ["A", "A", "A", "A", "D", "A"]

    guesses = []
    score = 0

    for i, question in enumerate(questions):
        print("-----------------------------------------------")
        print(question)
        for option in options[i]:
            print(option)
        guess = input("Enter The option(A,B,C,D): ").upper()

        while guess not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter A, B, C, or D.")
            guess = input("Enter The option(A,B,C,D): ").upper()

        guesses.append(guess)

        if guess == answers[i]:
            score += 1
            print("Correct")
        else:
            print("Incorrect")
            print(f"The correct answer is: {answers[i]}")
    print()
    print("****************************")
    print("RESULT")
    print("\nAnswers:", " ".join(answers))
    print("Guesses:", " ".join(guesses))

    score = (score / len(questions)) * 100
    print(f"\nYour Score is: {score}%")
    print("Do you want to play again?? ...Press Enter")
    user=input()
    if user=='':
     main()
    
def main():
    display_welcome()

    user_input = input()

    if user_input == '':
    
        display_menu()

        
        user_input2 = int(input())

        if user_input2 == 1:
            play()

if __name__=="__main__":
    main()