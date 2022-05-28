correct = 0
incorrect = 0
print("Welcome to the Imani Game Show!")
name = input("Enter your name to start: ")
print(f"OK, {name}, here's the first question.")
print("What color is the sky?(Answer by typing the letter and pressing Enter)")
print("(a) Green  (b) Blue")
print("(c) Pink   (d) Orange")
user_answer1 = input(">")
if user_answer1.lower() == "b":
    correct += 1
else:
    incorrect += 1
print("Ok, next question!")
print("What color is a Stop sign?(Answer by typing the letter and pressing Enter)")
print("(a) Yellow   (b) Green")
print("(c) Purple   (d) Red")
user_answer2 = input(">")
if user_answer2.lower() == "d":
    correct += 1
else:
    incorrect += 1
print("Interesting answer! Now the next question.")
print("How many days are in a year?(Answer by typing the letter and pressing Enter)")
print("(a) 200   (b) 365")
print("(c) 430   (d) 140")
user_answer3 = input(">")
if user_answer3.lower() == "b":
    correct += 1
else:
    incorrect += 1
print("Alright, fourth question!")
print("How many letters are in the Alphabet?(Answer by typing the letter and pressing Enter)")
print("(a) 21   (b) 23")
print("(c) 26   (d) 28")
user_answer4 = input(">")
if user_answer4.lower() == "c":
    correct += 1
else:
    incorrect += 1
print("Ok, last question!")
print("What year was the Declaration of Independence signed?(Answer by typing the letter and pressing Enter)")
print("(a) 1776   (b) 1767")
print("(c) 1773   (d) 1756")
user_answer5 = input(">")
if user_answer5.lower() == "a":
    correct += 1
else:
    incorrect += 1
print("OK! Here is your score: ")
print(f"{correct} right and {incorrect} wrong")
print("Thank you for playing!")