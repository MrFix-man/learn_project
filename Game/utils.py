import json


def load_questions_from_json():

    file = open("data.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()
    return data


def show_field(questions):

    for category_name, category_questions in questions.items():
        print(category_name.ljust(17), end='')
        for price, question_data in category_questions.items():
            asked =  question_data["asked"]
            if not asked:
                print(price.ljust(5), end=' ')
            else:
                print("   ".ljust(6), end='')
        print()


def pars_input(user_input):

    user_data = user_input.split(" ")
    if user_data != 2:
        return


questions = load_questions_from_json()
show_field(questions)