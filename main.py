from google import search

question = input("q\n")

choice1 = input("c1\n")
choice2 = input("c2\n")
choice3 = input("c3\n")

startdex = 1
while True:
    search(startdex, question, choice1, choice2, choice3)
    startdex += 10