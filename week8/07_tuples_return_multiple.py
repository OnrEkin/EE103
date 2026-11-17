# Tuples: Returning more than one value


def name_splitter(full_name):
    """full_name is a string like 'Name Surname'.
    Returns a tuple (first_name, surname). If there is more than one first name,
    everything except the last word is the first name."""
    words = full_name.split()
    first_name = " ".join(words[:-1])
    surname = words[-1]
    return (first_name, surname)


def char_counts(s):
    """ s is a string of lowercase chars
    Return a tuple where the first element is the number of vowels in s and the second element is
    the number of consonants in s """
    vowels = 0
    consonants = 0
    for char in s:
        if char in "aeiou":
            vowels += 1
        elif char.isalpha():   # letters that are not vowels; spaces, digits, etc. are skipped
            consonants += 1
    return (vowels, consonants)


print(name_splitter("Onur Ekin Cetin"))
first, last = name_splitter("Ada Lovelace")   # unpack the returned tuple
print("first name:", first, " surname:", last)

print(char_counts("abcd"))          # (1, 3)
print(char_counts("programming"))   # (3, 8)
v, c = char_counts("hello world")
print("vowels:", v, " consonants:", c)   # 3, 7
