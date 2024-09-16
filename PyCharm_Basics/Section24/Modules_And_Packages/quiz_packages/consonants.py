def get_consonants(text):
    my_set = set()
    for char in text.upper():
        if char in ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"):
            my_set.add(char)
    return my_set