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
def get_question (get_qna):
  return random.randint(0, (len(get_qna)-1))

def printing_qna(get_qna, index):
  question = (get_qna[index]["question"])
  correct_answer = get_qna[index]["correct_answer"]
  all_answers = get_qna[index]["wrongs"]
  all_answers.append(correct_answer)
  return question, correct_answer, all_answers





# def coran():
#   math_coran = {
#     "Spherical Geometry": "Bernhard Riemann",
#     "Knot Theory": "Sir William Thomson",
#     "Non-Euclidian Geometry": "Janos Bolyai"
#   }
  # return math_coran
  
def get_user_answer(quizzer, math_coran):
  answer = input("")
  return answer


# for questions in get_qna():
#   print(questions["question_1"])
#   print()

