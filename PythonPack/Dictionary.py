customer = {
    "name": "Natnael",
    "Age": "30",
    "is_verified": "false"
}

print(customer["name"])

number = input("Phone Number? ")
p_number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five"
}

result = ""

for n in number:
    if(n in p_number.keys()):
        result += p_number.get(n) + " "
else:
    print(result)


def emoji_converter(emoji):
    words = emoji.split(" ")

    emojis = {
        ":)": "😀",
        ":(": "😔"
    }

    result2 = ""

    for word in words:
        result2 += emojis.get(word, word) + "😀 "

    return result2

print("Hi there")
print(emoji_converter(""))