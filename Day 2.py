import random
import os as clear

def user_name():
  name = input("What is your name?: ").title
  print (f"Welcome {name}")
  return name

def get_qna():
  quizzer = [ 
    {"question_1": "Who created Spherical Geometry?", "correct_answer":"Bernhard Riemann", "wrongs_1":["Jules Ropa","Albert Einstein","John Locke"]},

    {"question_2": "Who is credited with the invention of Knot Theory?","correct_answer": "Sir William Thomson", "wrongs_2":[ "Isaac Newton", "Muhammad ibn Musa al-Khwarizmi","Euclid", ]},

    {"question_3": "Who created Non-Euclidian Geometry?", "correct_answer": "Janos Bolyai", "wrongs_3":[ "Leonardo Fibonacci", "George Boole", "Benjamin Franklin"]}
]
  return quizzer

def coran():
  math_coran = {
    "Spherical Geometry": "Bernhard Riemann",
    "Knot Theory": "Sir William Thomson",
    "Non-Euclidian Geometry": "Janos Bolyai"
  }
  return math_coran
  
def get_user_answer(quizzer, math_coran):
  answer = input("")
  return answer


# def r_or_w(quizzer):
#   if user_answer = 

for questions in get_qna():
  print(questions["question_1"])
  print()
