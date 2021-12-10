from emoji.core import emojize
from colorama import Fore, Back, Style
from components.quizQuestions import questions
from components import vars, quizTally

#Intro of the Quiz___________________________________________________
print("")
print("")
print(Fore.RED + "$$\      $$\  $$$$$$\  $$$$$$$\  $$\    $$\ $$$$$$$$\ $$\       ")
print("$$$\    $$$ |$$  __$$\ $$  __$$\ $$ |   $$ |$$  _____|$$ |      ")
print("$$$$\  $$$$ |$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ |      $$ |      ")
print("$$\$$\$$ $$ |$$$$$$$$ |$$$$$$$  |\$$\  $$  |$$$$$\    $$ |      ")
print("$$ \$$$  $$ |$$  __$$ |$$  __$$<  \$$\$$  / $$  __|   $$ |      ")
print("$$ |\$  /$$ |$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |      $$ |      ")
print("$$ | \_/ $$ |$$ |  $$ |$$ |  $$ |   \$  /   $$$$$$$$\ $$$$$$$$\ ")
print("\__|     \__|\__|  \__|\__|  \__|    \_/    \________|\________|")
print(Style.RESET_ALL)
print(Back.CYAN + Fore.BLACK + "Design a superhero identity for yourself,")
print("and then take a look at which Marvel superhero resembles you the most! ! !" + Style.RESET_ALL)
print("")
print("")

# Question start ____________________________________________________
#question 1
print(Back.LIGHTBLACK_EX + "________________________________________________________________________________")
answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print("+++++++++++++++++++++++++++++++\n")

#question 2
answer2 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer2
print("+++++++++++++++++++++++++++++++\n")

#question 3
answer3 = questions["q3"][input(questions["q3"]["question"])]
print(answer3)

vars.quizTotal += answer3
print("+++++++++++++++++++++++++++++++\n")

#question 4
answer4 = questions["q4"][input(questions["q4"]["question"])]
print(answer4)

vars.quizTotal += answer4
print("+++++++++++++++++++++++++++++++\n")

#question 5
answer5 = questions["q5"][input(questions["q5"]["question"])]
print(answer5)

vars.quizTotal += answer5
print("+++++++++++++++++++++++++++++++\n")

#question 6
answer6 = questions["q6"][input(questions["q6"]["question"])]
print(answer6)

vars.quizTotal += answer6
print("+++++++++++++++++++++++++++++++\n")

#question 7
answer7 = questions["q7"][input(questions["q7"]["question"])]
print(answer3)

vars.quizTotal += answer7
print("+++++++++++++++++++++++++++++++\n")
print("______________________________________________________________________________" + Style.RESET_ALL)
print("")
print(Fore.CYAN + "total so far: " + str(vars.quizTotal) + "\n")
print(Style.RESET_ALL)

#question end ______________________________________________________

# after answer all the questions, figure out who your character is
quizTally.total(vars.quizTotal)