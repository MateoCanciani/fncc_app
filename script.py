import re
from unidecode import unidecode

questions = {"A1": ("Q01", "Q02", "Q03", "Q04", "Q05"),
             "A2": ("Q01", "Q02", "Q03", "Q04", "Q05"),
             "B1": ("Q01", "Q02", "Q03", "Q04", "Q05"),
             "B2": ("Q01", "Q02", "Q03", "Q04", "Q05")}
answers = {"A1": ("A01", "A02", "A03", "A04", "A05"),
           "A2": ("A01", "A02", "A03", "A04", "A05"),
           "B1": ("A01", "A02", "A03", "A04", "A05"),
           "B2": ("A01", "A02", "A03", "A04", "A05")}
index_question = 0
levels = {"beginner": "A1", "medium": "A2", "advanced": "B1", "master": "B2"}

def set_level():
    user_level = ""
    while not user_level:
        user_input = input("Quel niveau de Français estimez vous avoir ?\nRéponse possible: beginner, medium, advanced, master: ")
        user_level = levels.get(user_input.lower().strip(), None)
        if not user_level:
            print("Wrong input. Please choose one of the given levels.")
    return user_level

def level_checkpoint(score, user_level):
    number_questions = len(questions[user_level])
    universal_levels = list(levels.values())
    if user_level == universal_levels[-1]: #popitem() ?
        print(f"You reached the higher level of our test with a score of: {score}/{number_questions}. Congrats!")
        return
    if score <= 3:
        print(f"Your score is: {score}/{number_questions}.\nNot enough to go to the upper level.")
        print(f"Congrats! Your current level is: {user_level}.")
        return
    print(f"Your score is: {score}/{number_questions}.\nYou will go to the upper level.")
    index_level = universal_levels.index(user_level)
    user_level = universal_levels[index_level + 1]
    return user_level

def get_questions(current_level):
    return questions[current_level]

def ask_question(question) : 
    print(f"Question: {question}")
    user_answer = input("Your answer is: ")
    return(user_answer)

def check_answer(user_answer, user_level, index):
    correct_answer = answers[user_level][index]
    ascii_user_answer = unidecode(user_answer)
    regex_pattern = re.compile(re.escape(ascii_user_answer), re.IGNORECASE)
    if regex_pattern.match(correct_answer):
        print("oui")
        return 1
    else:
        print("non")
        return 0

#### Main algorythm
# User presses "Let's get started" button
"""user_level = set_level()

while user_level:
    score = 0
    question_set = get_questions(user_level)

    for count, question in enumerate(question_set):
        user_answer = ask_question(question)
        score += check_answer(user_answer, user_level, count)

    user_level = level_checkpoint(score, user_level)

"""
"""
This function can be used to follow your way to do this.

def get_question(current_level, index_question):
if current_level == levels[-1]:
    return
if index_question == 4:
    index_level = levels.index(current_level)
    current_level = levels[index_level + 1]
    index_question = 0
    return questions[current_level][index_question]
question_set = questions[current_level]
index_question += 1
return question_set[index_question]
"""