import subprocess

letterEmoteCode = ":regional_indicator_"
numberEmoteCodes = {
    "0": ":zero:",
    "1": ":one:",
    "2": ":two:",
    "3": ":three:",
    "4": ":four:",
    "5": ":five:",
    "6": ":six:",
    "7": ":seven:",
    "8": ":eight:",
    "9": ":nine:",
}
miscEmotesCodes = {
    "?": ":question:",
    "!": ":exclamation:",
    "utopia": ":dog:",
}


def translate_word(word: str) -> str:
    emote_list = list()
    for x in word:
        if x.isalpha():
            emote_list.append(letterEmoteCode + x + ":")
        elif x.isalnum():
            emote_list.append(numberEmoteCodes[x])
        else:
            misc = miscEmotesCodes.get(x, f" {x}")
            emote_list.append(misc)

    return " ".join(emote_list)


def translate_to_emote(message: str) -> str:
    cleaned_message = message.lower()
    words_list = cleaned_message.split(" ")
    words_as_emotes = [translate_word(word) for word in words_list if len(word) > 0]
    return "--".join(words_as_emotes) + "."


print("Enter '/q' or press 'Ctrl + C' to quit")
while True:
    input_text = input("Text to Emote:\n->")
    if input_text.lower() == "/q":
        break
    if len(input_text.strip()) == 0:
        print("\033[91m" + "No input was provided" + "\033[0m")
        continue
    output_text = translate_to_emote(input_text)
    cmd = "echo " + output_text + "|clip"
    subprocess.check_call(cmd, shell=True)
    print("\033[92m" + "Text was copied to clipboard" + "\033[0m")
print("Goodbye!!")
