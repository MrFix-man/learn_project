easy = {
    "cow":"корова",
    "camera":"камера",
    "dog":"собака",
    "ear":"ухо",
    "hair":"волосы"
}

medium = {
    "draw":"рисунок",
    "kettle":"чайник",
    "match":"соответствовать",
    "monkey":"обезьяна",
    "plow":"плуг"
}

hard = {
    "contest":"конкурс",
    "employee":"служащий",
    "income":"доход",
    "bargain":"сделка",
    "representative":"представитель"
}

levels = {
    0:"Нулевой",
    1:"Так себе",
    2:"Можно лучше",
    3:"Норм",
    4:"Хорошо",
    5:"Отлично"
}

answers = {

}

correct_count = 0
incorrect_count = 0
correct_words = []
incorrect_words = []

level_user = input("Выберете сложность: легкий, средний или сложный \n").lower()

if level_user == "легкий":
    words = easy

elif level_user == "средний":
    words = medium

elif level_user == "сложный":
    words = hard

else:
    print("Допущена ошибка, нет такого уровня. Вы проиграли!")
    exit()

words_count = len(words)

print(f"Выбран {level_user} уровень сложности, мы предложим {words_count} слов, подберите преревод")

for word_en, word_ru in words.items():
    input("Нажмите Enter")

    letter_count = len(word_ru)
    first_leter = word_ru[0]

    user_answer = input(f"{word_en}, {letter_count} букв, первая буква {first_leter}...\n")

    if user_answer.lower() == word_ru.lower():
        print(f"Верно, {word_en} это {word_ru}")
        correct_count += 1
        answers[word_en] = True
        correct_words.append(word_en)

    else:
        print(f"Неверно, {word_en} это {word_ru}")
        incorrect_count += 1
        answers[word_en] = False
        incorrect_words.append(word_en)

print(f"\nВаш уровень знания языка: {levels[correct_count]}")

print(f"\nПравильно отвеченные слова: {correct_count} шт.")
for correct in correct_words:
    print(correct)
print(f"\nНеправильно отвеченные слова: {incorrect_count} шт.")
for incorrect in incorrect_words:
    print(incorrect)
