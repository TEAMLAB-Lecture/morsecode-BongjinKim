# -*- coding: utf8 -*-
import re

def get_morse_code_key(morse_code_dict, morse_code_value):
    return next(key for key, value in morse_code_dict.items()if value == morse_code_value)

# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 대소문자 구분없이 "H" 또는 "HELP"일 경우 True,
          그렇지 않을 경우 False를 반환함
    Examples:
        >>> import morsecode as mc
        >>> mc.is_help_command("H")
        True
        >>> mc.is_help_command("Help")
        True
        >>> mc.is_help_command("Half")
        False
        >>> mc.is_help_command("HeLp")
        True
        >>> mc.is_help_command("HELLO")
        False
        >>> mc.is_help_command("E")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = user_input.lower()
    return result == "h" or result == "help"
    # ==================================
# print(is_help_command("H"))
# print(is_help_command("Halp"))
# print(is_help_command("Hakf"))
# print(is_help_command("help"))
# print(is_help_command("e"))

def is_validated_english_sentence(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) 숫자가 포함되어 있거나,
          2) _@#$%^&*()-+=[]{}"';:\|`~ 와 같은 특수문자가 포함되어 있거나
          3) 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력했을 경우
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_english_sentence("Hello 123")
        False
        >>> mc.is_validated_english_sentence("Hi!")
        True
        >>> mc.is_validated_english_sentence(".!.")
        False
        >>> mc.is_validated_english_sentence("!.!")
        False
        >>> mc.is_validated_english_sentence("kkkkk... ^^;")
        False
        >>> mc.is_validated_english_sentence("This is Gachon University.")
        True
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    p = re.compile("[0-9]+|\@|\#|\$|\%|\^|\&|\*|\(|\)|\-|\+|\=|\[|\]|\\|\}|\{|\"|\'|\;|\||\`|\~")
    temp = "".join(p.findall(user_input))
    result = False
    #쓰래기 값이 없을때 길이가 0이므로, 문장부호 ,.!? 제거
    if not temp:
        p = re.compile("[a-z]+")
        result = bool(p.findall(user_input.lower()))
    return result
    # ==================================
# print(is_validated_english_sentence("This is Gachon University."))
# print(is_validated_english_sentence("Hello 123"))
# print(is_validated_english_sentence("Hi!"))
# print(is_validated_english_sentence(".!."))
# print(is_validated_english_sentence("!.!."))
# print(is_validated_english_sentence("kkkkk... ^^;"))
def is_validated_morse_code(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) "-","."," "외 다른 글자가 포함되어 있는 경우
          2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우 ex)......
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_morse_code("..")
        True
        >>> mc.is_validated_morse_code("..-")
        True
        >>> mc.is_validated_morse_code("..-..")
        False
        >>> mc.is_validated_morse_code(". . . .")
        True
        >>> mc.is_validated_morse_code("-- -- -- --")
        True
        >>> mc.is_validated_morse_code("!.1 abc --")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    p = re.compile("[\-|\.|\ ]+")
    is_not_trash = len("".join(p.findall(user_input))) == len(user_input) #쓰래기값이 없으면 true, 있으면 false
    morse_code_dict_values = get_morse_code_dict().values()
    result = False
    if is_not_trash: #쓰래기값이 없으면
        split_string = user_input.split()
        result = not bool([morse_code_string for morse_code_string in split_string if morse_code_string not in morse_code_dict_values])
    return result
    # ==================================
# print(is_validated_morse_code(".."))
# print(is_validated_morse_code("..-"))
# print(is_validated_morse_code("..-.."))
# print(is_validated_morse_code(". . . ."))
# print(is_validated_morse_code("-- -- -- --"))
# print(is_validated_morse_code("--.--.- .-.-. .-"))


def get_cleaned_english_sentence(raw_english_sentence):
    """
    Input:
        - raw_english_sentence : 문자열값으로 Morse Code로 변환 가능한 영어 문장
    Output:
        - 입력된 영어문장에수 4개의 문장부호를 ".,!?" 삭제하고, 양쪽끝 여백을 제거한 문자열 값 반환
    Examples:
        >>> import morsecode as mc
        >>> mc.get_cleaned_english_sentence("This is Gachon!!")
        'This is Gachon'
        >>> mc.get_cleaned_english_sentence("Is this Gachon?")
        'Is this Gachon'
        >>> mc.get_cleaned_english_sentence("How are you?")
        'How are you'
        >>> mc.get_cleaned_english_sentence("Fine, Thank you. and you?")
        'Fine Thank you and you'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = raw_english_sentence.replace('.','').replace(',','').replace('!','').replace('?','')
    while result[0]==' ' and result[-1]==' ':
        if result[0] == ' ':
            result = result[1:]
        if result[-1] == ' ':
            result = result[:-1]
    return result
    # ==================================
# print(get_cleaned_english_sentence("  This is Gachon!!  "))
# print(get_cleaned_english_sentence("Is this Gachon?"))
# print(get_cleaned_english_sentence("How are you?"))
# print(get_cleaned_english_sentence("Fine, Thank you. and you?"))
def decoding_character(morse_character):
    """
    Input:
        - morse_character : 문자열값으로 get_morse_code_dict 함수로 알파벳으로 치환이 가능한 값의 입력이 보장됨
    Output:
        - Morse Code를 알파벳으로 치환함 값
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_character("-")
        'T'
        >>> mc.decoding_character(".")
        'E'
        >>> mc.decoding_character(".-")
        'A'
        >>> mc.decoding_character("...")
        'S'
        >>> mc.decoding_character("....")
        'H'
        >>> mc.decoding_character("-.-")
        'K'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    result = get_morse_code_key(morse_code_dict, morse_character)

    return result
    # ==================================

def encoding_character(english_character):
    """
    Input:
        - english_character : 문자열값으로 알파벳 한 글자의 입력이 보장됨
    Output:
        - get_morse_code_dict 함수의 반환 값으로 인해 변환된 모스부호 문자열값
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_character("G")
        '--.'
        >>> mc.encoding_character("A")
        '.-'
        >>> mc.encoding_character("C")
        '-.-.'
        >>> mc.encoding_character("H")
        '....'
        >>> mc.encoding_character("O")
        '---'
        >>> mc.encoding_character("N")
        '-.'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    result = morse_code_dict[english_character]

    return result
    # ==================================
# print(encoding_character("G"))
# print(encoding_character("A"))
# print(encoding_character("C"))
# print(encoding_character("H"))
# print(encoding_character("O"))
# print(encoding_character("N"))

def decoding_sentence(morse_sentence):
    """
    Input:
        - morse_sentence : 문자열 값으로 모스 부호를 표현하는 문자열
    Output:
        - 모스부호를 알파벳으로 변환한 문자열
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_sentence("... --- ...")
        'SOS'
        >>> mc.decoding_sentence("--. .- -.-. .... --- -.")
        'GACHON'
        >>> mc.decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-")
        'I LOVE YOU'
        >>> mc.decoding_sentence("-.-- --- ..-  .- .-. .  ..-. ")
        'YOU ARE F'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    #2칸 간격 split
    temp = morse_sentence.split("  ")
    result = " ".join("".join(decoding_character(morse_string) for morse_string in word.split()) for word in temp)
    return result
    # ==================================
# print(decoding_sentence("... --- ..."))
# print(decoding_sentence("--. .- -.-. .... --- -."))
# print(decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-"))
# print(decoding_sentence("-.-- --- ..-  .- .-. .  ..-. "))

def encoding_sentence(english_sentence):
    """
    Input:
        - english_sentence : 문자열 값으로 모스 부호로 변환이 가능한 영어문장
    Output:
        - 입력된 영어문장 문자열 값을 모스부호로 변환된 알파벳으로 변환한 문자열
          단 양쪽 끝에 빈칸은 삭제한다.
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_sentence("HI! Fine, Thank you.")
        '.... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-'
        >>> mc.encoding_sentence("Hello! This is CS fifty Class.")
        '.... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...'
        >>> mc.encoding_sentence("We Are Gachon")
        '.-- .  .- .-. .  --. .- -.-. .... --- -.'
        >>> mc.encoding_sentence("Hi! Hi!")
        '.... ..  .... ..'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    p = re.compile("[A-Z]+")
    temp = p.findall(english_sentence.upper())
    result = "  ".join(" ".join(encoding_character(morse_string) for morse_string in word) for word in temp)
    return result
    # ==================================
# print(encoding_sentence("HI! Fine, Thank you.")=='.... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-')
# print(encoding_sentence("Hello! This is CS fifty Class.")=='.... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...')
# print(encoding_sentence("We Are Gachon")=='.-- .  .- .-. .  --. .- -.-. .... --- -.')
# print(encoding_sentence("Hi! Hi!")=='.... ..  .... ..')

def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    user_input = '1'
    while user_input != '0':
        user_input = input("Input your message(H - Help, 0 - Exit): ")
        user_output = ""
        #입력이 올바른경우
        if is_help_command(user_input):
            user_output = get_help_message()
        elif is_validated_english_sentence(user_input):
            english_sentence = get_cleaned_english_sentence(user_input)
            user_output = encoding_sentence(english_sentence)
        elif is_validated_morse_code(user_input):
            user_output = decoding_sentence(user_input)
        else:
            user_output = "Wrong Input"
        print(user_output)
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
