def get_vowels(text):
    my_set = set()
    for char in text.upper():
        try:
            str(char)
        except Exception as ex:
            print(ex)
        else:
            if char in ("A", "E", "I", "O", "U"):
                my_set.add(char)
    return my_set