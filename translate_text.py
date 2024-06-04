import hiragana_dict as hd


def returnKanaFromPhonetic(input):
    return hd.kana_dict.get(input)


vowels = ["a", "e", "i", "o", "u"]


def translateSentence(text_input):
    buffer = ""
    print("text input in function", text_input)
    print("text input in function final", text_input[-1])
    final = text_input[-1]

    if final in vowels:
        buffer = ""
        return returnKanaFromPhonetic(text_input)

    else:
        if text_input == "y":
            buffer += "y"
        buffer += text_input
        print("buffer no vowel", buffer)
        return text_input
