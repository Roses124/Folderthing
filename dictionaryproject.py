import random

import json

survey_questions = ["name", " animal? ", " color? ", " season? ", " day of the week? ", " TV show? ", " donut flavor? "]

survey_answers = {}

allusers = []



survey_questions = [" name? ", " favorite animal? Cats or dogs? ", " favorite color? ", " favorite season? ", " favorite day of the week? ", " favorite TV show? ", " favorite donut flavor? "]
keys = ["name", "favorite animal", "favorite color", "favorite season", "favorite day of the week", "favorite TV show", "favorite donut flavor"]

users = 0

maxusers = 2

#while questions <= maxquestions:
#    randomquestion = random.choice(survey_questions)
#    index_surveyquests = iter(survey_questions)
##    index_key = index_surveyquests
#    answer = input("What is your favorite" + str(randomquestion))
#    survey_answers[keys[index]] = answer
#    questions = questions+1
#print("Here are your answers! ")
#print(survey_answers)

while users < maxusers:
    index = 0
    for q in survey_questions:
        ans = input("What is your" + q)
        survey_answers[keys[index]] = ans
        index+=1
    allusers.append(survey_answers)
    print("Here are your answers!")
    print(survey_answers)
    user_change = input("Are you a new user? Yes or no? ")
    if user_change == "yes":
        users = users+1
#        index = 0
#        for q in survey_questions:
#            ans = input("What is your" + q)
#            survey_answers2[keys[index]] = ans
#            index+=1
#        print("Here are your answers!")
#        print(survey_answers2)
#        user_change = input("Are you a new user? Yes or no. ")
    elif user_change == "no":
        break


with open('thing.json') as f:
    try:
        olddata = json.load(f)
    except:
        olddata = []
allusers.extend(olddata)
f.close()

f = open("thing.json", "w")
json.dump(allusers, f)
f.close()

fun_fact = input("Do you wanna hear a funfact about this survey? Yes ot no. ")
count = 0
catc = 0
dogc = 0
if fun_fact == "yes":

    for u in allusers:
        count += 1
        ans = u['favorite animal']
        if ans == "cats":
            catc += 1
        elif ans == "dogs":
            dogc += 1
    if catc > dogc:
        print(str(catc) + " out of " + str(count) + " are cat people!")
    elif dogc > catc:
        print(str(dogc) + " out of " + str(count) + " are dog people!")
elif fun_fact == "no":
    print("Thanks for playing! ")
