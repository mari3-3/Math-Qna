import os
import random

def clear():
  os.system("clear")

def user_name():
  name = input("What is your name?: ").title().strip()
  print (f"Welcome {name}")
  return name

def get_qna():
  quizzer = [ 
    {"question": "Who created Spherical Geometry?", "correct_answer":"Bernhard Riemann", "wrongs":["Jules Ropa","Albert Einstein","John Locke"]},

    {"question": "Who is credited with the invention of Knot Theory?","correct_answer": "Sir William Thomson", "wrongs":[ "Isaac Newton", "Muhammad ibn Musa al-Khwarizmi","Euclid", ]},

    {"question": "Who created Non-Euclidian Geometry?", "correct_answer": "Janos Bolyai", "wrongs":[ "Leonardo Fibonacci", "George Boole", "Benjamin Franklin"]}
]
  return quizzer

#Come back to this
def get_question (qna):
  return random.randint(0, (len(qna)-1))

def printing_qna(qna, index):
  question = (qna[index]["question"])
  correct_answer = qna[index]["correct_answer"]
  all_answers = qna[index]["wrongs"]
  all_answers.append(correct_answer)
  return question, correct_answer, all_answers

def display_question(question, all_answers):
  counter = 0
  print(question)
  for answer in all_answers:
    counter +=1
    print(f"{counter}. {answer}")

def get_under_answer():
  player_answer = int(input("Enter the number of the correct answer: "))
  return player_answer

def check_answer(all_answers, correct_answer, player_answer):
  if all_answers[player_answer-1] ==correct_answer:
    print("Correct!")
  else:
    print("Incorrect!")



# def coran():
#   math_coran = {
#     "Spherical Geometry": "Bernhard Riemann",
#     "Knot Theory": "Sir William Thomson",
#     "Non-Euclidian Geometry": "Janos Bolyai"
#   }
  # return math_coran
  
# def get_user_answer(quizzer, math_coran):
#   answer = input("")
#   return answer

def start():
  qna = get_qna()
  index = get_question(qna)
  user_name()
  printing = printing_qna(qna, index)
  display = display_question(question, all_answers)
  check = check_answer(all_answers, correct_answer, player_answer)
  return printing,display,check

start()
