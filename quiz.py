import random
import os
import time

questions = [{"question":"What was Albert Einstein's nationality? ","answers" : ["A. American", "B. German", "C. Swiss", "D. Austrian"],"correctAnswer":"b"},
          {"question":"What is Albert Einstein famous for? ","answers" : ["A. His work on quantum mechanics", "B. His contributions to the development of the nuclear bomb", "C. His theory of relativity", "D. All of the above"],"correctAnswer":"d"},
          {"question":"What was Albert Einstein's educational background? ","answers" : ["A. He was a poor student in elementary school and was once expelled from school.", "B. He received a PhD in physics from the University of Zurich in 1905.", "C. He received a PhD in chemistry from the University of Berlin in 1911.", "D. He received a PhD in biology from the University of Vienna in 1914."],"correctAnswer":"b"},
          {"question":"What was Albert Einstein's profession? ","answers" : ["A. Theoretical physicist and academic","B. Industrial engineer", "C. Medical doctor", "D. Architect"],"correctAnswer":"a"},
          {"question":"What was the first major scientific contribution of Albert Einstein? ","answers" : ["A. The theory of special relativity", "B. The concept of mass-energy equivalence (E = mc^2)", "C. The explanation of the photoelectric effect", "D. All of the above"],"correctAnswer":"d"},
          {"question":"What did Albert Einstein receive the Nobel Prize in Physics for? ","answers" : ["A. His explanation of the photoelectric effect","B. His work on quantum mechanics", "C. His theory of relativity", "D. His contributions to the development of the nuclear bomb"],"correctAnswer":"a"},
          {"question":"What was Albert Einstein's theory of relativity? ","answers" : ["A. The idea that the laws of physics are the same for all observers, regardless of their relative motion","B. The concept of space-time, which combines the three dimensions of space with the fourth dimension of time into a single, unified structure", "C. Both A and B", "D. None of the above"],"correctAnswer":"c"},
          {"question":"When and where did Albert Einstein die? ","answers" : ["A. April 18, 1955, in Berlin, Germany","B. April 18, 1955, in Princeton, New Jersey, USA", "C. April 18, 1955, in Zurich, Switzerland", "D. April 18, 1955, in Vienna, Austria"],"correctAnswer":"b"},
          {"question":"What was Albert Einstein's relationship to the development of the nuclear bomb? ","answers" : ["A. He played a key role in the development of the bomb","B. He was opposed to the development of the bomb and spoke out against it", "C. He had no involvement in the development of the bomb", "D. He was neutral on the issue of the bomb's development"],"correctAnswer":"a"},
          {"question":"What was Albert Einstein's political stance? ","answers" : ["A. Conservative","B. Liberal", "C. Marxist", "D. He was apolitical"],"correctAnswer":"B"}
          ]

def gen_random_numbers_in_range(low, high, n):
    return random.sample(range(low, high), n)

def cleanTheScreen():
    os.system('cls')

def welcomeMessage():
    print("Welcome to the quiz game developed by Farzad Nazif 2022")
    input("Press Enter to start the quiz game")

def playTheGame():
    cleanTheScreen()
    correctGuesses = 0
    numberOfChances = 7
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
     for answer in questions[randomNumber]["answers"]:
         print(answer)
     guessword = input("Enter A,B,C or D :  ")
     cleanTheScreen()
     if guessword.lower() == questions[randomNumber]["correctAnswer"]:
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
    cleanTheScreen()
    print("Your total score is : " + str(correctGuesses) + "  Or  " + str(correctGuesses/questionsCount * 100) + " % ")
    if totalTime > 300:
        print("It took more than 3 minutes, Game Over!! OPS :(((((")
    else:
        print("Your total time is :" + str(totalTime) + " Second")    
    playAgain = input("Do you want to play again? Yes or No  :  ")   
    if playAgain.lower() == "yes":
         cleanTheScreen()
         startTheGame()
    elif playAgain.lower() == "no":
         cleanTheScreen()
         print("Good bye, see you soon")   
         return

def startTheGame():
    cleanTheScreen()
    options = input("""
     !!! You will have only 5 minutes to answer the questions !!!

     1 Help
     2 Play Quiz
     3 Quit
     Please write 1 or 2 or 3
    """)
    if options == "1":
        cleanTheScreen()
        print("""
        The best tip:
        You just need to write A,B,C and D and hit the Enter
        """)
        input("Press Enter to come back to the main menu")
        cleanTheScreen()
        startTheGame()
        return
    if options == "2":
        playTheGame()        
    if options == "3":
        cleanTheScreen()
        print("Good bye, see you soon")  
        return  


welcomeMessage()    
startTheGame()
