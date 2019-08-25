# 1.0.7
def count_word_lengths(s):
    assert all([x.isalpha() or x == ' ' for x in s])
    assert type(s) is str
    words = s.split() # split the words within the string
    letter_count_per_word = [len(w) for w in words] # get the letter count for each word
    return letter_count_per_word
