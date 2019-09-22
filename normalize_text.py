# Exercise: 2.0.1
def normalize_string(s):
    assert type (s) is str
    return ''.join([char for char in s.lower() if char.isalpha() or char.isspace()])
# Demo:
print(latin_text[:100], "...\n=>", normalize_string(latin_text[:100]), "...")
