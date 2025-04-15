import os
import random

def clear():
  os.system("clear")

def user_name():
  name = input("What is your name?: ").title().strip()
  print (f"Welcome {name}!")
  return name

def get_qna():
  quizzer = [ 
    {"question": "Who created Spherical Geometry?",
     "correct_answer":"Bernhard Riemann",
     "wrongs":["Jules Ropa","Albert Einstein","John Locke"]},

    {"question": "Who is credited with the invention of Knot Theory?"
    ,"correct_answer": "Sir William Thomson", 
    "wrongs":[ "Isaac Newton","Muhammad ibn Musa al-Khwarizmi", "Euclid", ]},

    {"question": "Who created Non-Euclidian Geometry?", 
     "correct_answer": "Janos Bolyai",
     "wrongs":[ "Leonardo Fibonacci", "George Boole", "Benjamin Franklin"]}
]
  return quizzer

def get_question (qna):
  index = random.randint(0, (len(qna)-1))
  return index

def printing_qna(qna, index):
  question = (qna[index]["question"])
  correct_answer = qna[index]["correct_answer"]
  all_answers = qna[index]["wrongs"].copy()
  all_answers.append(correct_answer)
  return question, correct_answer, all_answers

def shuffle(all_answers):
  random.shuffle(all_answers)

def display_question(question, all_answers):
  print(question)
  counter = 1
  for answer in all_answers:
    print(f"{counter}. {answer}")
    counter += 1

def get_user_answer():
  player_answer = int(input("Enter the number of the correct answer: ")) 
  return player_answer

def check_answer(all_answers, correct_answer, player_answer,):
  counter = 0
  if all_answers[player_answer-1] ==correct_answer:
    print("Correct!")
    counter += 1
  else:
    print("Incorrect!")

def start():
  qna = get_qna()
  index = get_question(qna)
  name = user_name()
  print()
  while True:
    index = get_question(qna)
    question, correct_answer, all_answers= printing_qna(qna, index)
    shuffle(all_answers)
    display_question(question, all_answers)
    player_answer = get_user_answer()

    global counter
    counter = +1

    check_answer(all_answers, correct_answer, player_answer)
    print()
    if counter == 1: 
      answer = input("Would you like to play again? (y/n): ").lower().strip()
      if answer == 'y':
        clear()
        start()
    elif counter == 3:
      answer = input("Would you like to play again? (y/n): ").lower().strip()

    clear()
    print()
    clear()
    print(f"Thanks for playing {name} >+<!")
    break

start()
