import random
import os
import time

questions = [{"question":"Who created Python?: ","answer" : ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],"correctAnswer":"A"},
          {"question":"What year was Python created?: ","answer" : ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],"correctAnswer":"B"},
          {"question":"Python is tributed to which comedy group?: ","answer" : ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],"correctAnswer":"C"},
          {"question":"Is the Earth round?: ","answer" : ["A. True","B. False", "C. sometimes", "D. What's Earth?"],"correctAnswer":"A"}]

def gen_random_numbers_in_range(low, high, n):
    return random.sample(range(low, high), n)

def welcomeMessage():
    print("Welcome to the quiz game developed by Farzad Nazif 2022")
    input("Press Enter to start the quiz game")

def startTheGame():
    os.system('cls')
    options = input("""
     1 Help
     2 Play Quiz
     3 Quit
     Please write 1 or 2 or 3
    """)
    if options == "1":
        os.system('cls')
        print("""
        The best tip:
        You just need to write A,B,C and D and hit the Enter
        """)
        input("Press Enter to come back to the main menu")
        os.system('cls')
        startTheGame()
        return
    if options == "3":
        os.system('cls')
        print("Good bye, see you soon")  
        return  
    if options == "2":
        os.system('cls')
        correctGuesses = 0
        numberOfChances = 5
        questionsCount = len(questions)
        startTime = time.time()
        randomNumbers = gen_random_numbers_in_range(0, len(questions), len(questions))
        print("You have :" + str(numberOfChances) + " Chances")
        print("--------------------- \nThe timer has started\n ---------------------")
        for randomNumber in randomNumbers:  
         if numberOfChances<1:
             startTheGame()
             return
         print(questions[randomNumber]["question"])
         for answer in questions[randomNumber]["answer"]:
             print(answer)
         guessword = input("Enter A,B,C or D :  ")
         os.system('cls')
         if guessword == questions[randomNumber]["correctAnswer"]:
             correctGuesses+=1
             print("You have :" + str(numberOfChances) + " Chances")
             print("Your total score is : " + str(correctGuesses) + "  Or  " + str(correctGuesses/questionsCount * 100) + " % ")
             print("Correct Answer, Answer next question:")
             print("----------------")
         else: 
            correctGuesses-=1
            numberOfChances-=1
            print("You have :" + str(numberOfChances) + " Chances")
            print("Your total score is : " + str(correctGuesses) + "  Or  " + str(correctGuesses/questionsCount * 100) + " % ")
            print("Wrong Answer, Answer next question:")
            print("----------------")
        endTime = time.time()
        totalTime = round(endTime-startTime,2)
        os.system('cls')
        print("Your total score is : " + str(correctGuesses) + "  Or  " + str(correctGuesses/questionsCount * 100) + " % ")
        if totalTime > 180:
            print("It took more than 3 minutes, Game Over!! OPS :(((((")
        else:
            print("Your total time is :" + str(totalTime) + " Second")    
        playAgain = input("Do you want to play again? Yes or No   :")   
        if playAgain == "Yes":
             os.system('cls')
             startTheGame()
        elif playAgain == "No":
             os.system('cls')
             print("Good bye, see you soon")   
             return

welcomeMessage()    
startTheGame()
