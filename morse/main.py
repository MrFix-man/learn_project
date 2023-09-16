import random


def counter(func):
    def inner(*a, **kw):
        inner.count += 1
        return func(*a, **kw)

    inner.count = 0
    return inner


@counter
def input_data():

    with open("RUS.txt", "r", encoding="utf-8") as file:
        words = list(file)

    return words


@counter
def morse_encode(word, morse_code):

    """
    переводит английские слов в последовательность точек и тире
    :param morse_code:
    :param word:
    :return: строки морзянки
    """
    word_encoded = []

    for letter in word:
        word_encoded.append(morse_code.get(letter, ""))
    return " ".join(word_encoded)


@counter
def get_word(words):

    """
    получает случайное слово из списка
    :return: строка слова
    """

    return random.choice(words)


@counter
def print_statistics(answers):

    """
    на основе списка answers выводит статистику
    :param answers: список верности ответов
    """

    answers_total = len(answers)
    answers_correct = sum(answers)
    answers_incorrect = answers_total - answers_correct
    print(f"Всего задачек: {answers_total}\nРешено верно: {answers_correct}\nРешено неверно: {answers_incorrect}")


@counter
def main():

    morse_code = {
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.", "а": ".-", "б": "-...", "в": ".--", "г": "--.",
        "д": "-..", "е": ".", "ж": "...-", "з": "--..", "и": "..", "й": ".---", "к": "-.-", "л": ".-..",
        "м": "--", "н": "-.", "о": "---", "п": ".--.", "р": "-.-", "с": "...", "т": "-", "у": "..-",
        "ф": "..-.", "х": "....", "ц": "-.-.", "ч": "---.", "ш": "----", "щ": "--.-", "ъ": ".--.-.",
        "ы": "-.--", "ь": "-..-", "э": "...-...", "ю": "..--", "я": ".-.-",
        ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-",
        "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"}

    answers = []

    print("Сегодня мы потренируемся расшифровывать азбуку морзе\nЕсли захотите закончить, введите \"Конец\"")
    input("Нажмите enter")

    words = input_data()
    count_questions = 0

    while True:
        word = get_word(words)
        word_morse = morse_encode(word, morse_code)
        count_questions += 1
        user_input = input(f"Слово - {count_questions} {word_morse}\n")

        if user_input.lower() == "конец":
            break
        elif user_input.lower() == word.strip():
            print(f"Верно {word}\n")
            answers.append(True)
        else:
            print(f"Неверно {word}")
            answers.append(False)

    print_statistics(answers)

    """счетчик реалезованн через декоратор, другого способа не знаю, думаю не самый лучший способ,
    так как если в программе содержится большое количество функций, этот способ будет 
    крайне неудобен"""

    print(f"\nФункция input_data отработала {input_data.count} раз")
    print(f"Функция morse_encode отработала {morse_encode.count} раз")
    print(f"Функция get_word отработала {get_word.count} раз")
    print(f"Функция print_statistics отработала {print_statistics.count} раз")
    print(f"Функция main отработала {main.count} раз")


if __name__ == '__main__':
    main()
