import random


class Counter:
    go_def = 0


def input_data():
    Counter.go_def += 1
    with open("RUS.txt", "r", encoding="utf-8") as file:
        words = list(file)

    return words


def morse_encode(word, morse_code):
    Counter.go_def += 1
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


def get_word(words):
    Counter.go_def += 1
    """
    получает случайное слово из списка
    :return: строка слова
    """

    return random.choice(words)


def print_statistics(answers):
    Counter.go_def += 1
    """
    на основе списка answers выводит статистику
    :param answers: список верности ответов
    """

    answers_total = len(answers)
    answers_correct = sum(answers)
    answers_incorrect = answers_total - answers_correct
    print(f"Всего задачек: {answers_total}\nРешено верно: {answers_correct}\nРешено неверно: {answers_incorrect}")


def main():
    Counter.go_def += 1
    morse_code = {
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.", "а": ".-", "б": "-...", "в": ".--.", "г": "--.",
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
            print(f"Кол-во обращений к функциям = {Counter.go_def}")
            exit()
        elif user_input.lower() == word.strip():
            print(f"Верно {word}\n")
            answers.append(True)
        else:
            print(f"Неверно {word}")
            answers.append(False)


if __name__ == '__main__':
    main()
