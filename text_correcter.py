from spellchecker import SpellChecker

def read_text():
    if lang_code == 'en':
        print('Enter text')
        print('*from new line write "!!!!!" to stop')
    elif lang_code == 'ru':
        print('Напечатайте текст')
        print('*с новой строки напечатайте "!!!!!", чтобы остановиться')
    else:
        print('Tippen Sie bitte den text')
        print('*aus der neuen Zeile tippen Sie "!!!!!", um zu stoppen')
    inp = []
    sentence = ''
    while sentence != '!!!!!':
        sentence = input()
        inp.append(sentence.split())
    inp.pop(-1)

    return inp

def check_word():
    if lang_code == 'en':
        word = input('Please type your word: ')
    elif lang_code == 'ru':
        word = input('Пожалуйста, напечатайте ваше слово: ')
    else:
        word = input('Bitte tippen Sie Ihr Wort: ')

    ans = checker.correction(word)
    if ans == word:
        if lang_code == 'en':
            print('Word is already correct!')
        elif lang_code == 'ru':
            print('Слово уже правильно написано!')
        else:
            print('Das Wort ist schon richtig geschrieben!')

    else:
        if lang_code == 'en':
            print(f'Corrected word is "{ans}"')
            print(f'There are some more variants: {", ".join(list(checker.candidates(word))[:10])}')
        elif lang_code == 'ru':
            print(f'Отредактированное слово "{ans}"')
            print(f'Другие варианты: {", ".join(list(checker.candidates(word))[:10])}')
        else:
            print(f'Korregiertes Wort ist "{ans}"')
            print(f'Hier sind einige andere Variante: {", ".join(list(checker.candidates(word))[:10])}')

def correct_word(word):
    new_word = list(word)
    ending = []
    while not new_word[-1].isalpha():
        ending.append(new_word[-1])
        new_word.pop(-1)
    ending = ending[::-1]
    new_word = checker.correction(''.join(new_word))
    new_word += ''.join(ending)
    return new_word


def text_correct(text):
    correct_sen = []
    for sen in text:
        for word in sen:
            correct_sen.append(correct_word(word))
        print(' '.join(correct_sen))
        correct_sen = []


global lang_code

langs = ['russian','english','german']
langs_dict = {'russian' : 'ru','english' : 'en','german' : 'de'}

lang = input("Enter text language (russian/english/german): ").lower().strip()
while lang not in langs:
    lang = input("Uncorrect input. Choose one of the list: (russian,english,german): ").lower().strip()

lang_code = langs_dict[lang]
checker = SpellChecker(language=lang_code)

if lang_code == 'en':
    mode = input('If you want to check only 1 word type "1"\n'
                 'If you want to check full text type "2": ')
elif lang_code == 'ru':
    mode = input('Если Вы хотите проверить одно слово, напишите "1"\n'
                 'Если Вы хотите проверить текст, напишите "2": ')
else:
    mode = input('Wenn Sie wollen ein Wort überprüfen, tippen Sie "1"\n'
                 'Wenn Sie wollen den Text überprüfen, tippen Sie "2": ')

if mode == '1':
    check_word()
elif mode == '2':
    text_correct(read_text())
else:
    if lang_code == 'en':
        print('Uncorrect mode.')
    elif lang_code == 'ru':
        print('Неправильный режим.')
    else:
        print('Falscher Modus.')