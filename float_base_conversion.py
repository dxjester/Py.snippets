# A program designed to convert a floating string and base to a float

# 3.0.1
def is_valid_strfrac(s, base=2):
    return all([is_valid_strdigit(c, base) for c in s if c != '.']) \
        and (len([c for c in s if c == '.']) <= 1)
    
def eval_strfrac(s, base=2):
    assert is_valid_strfrac(s, base), "'{}' contains invalid digits for a base-{} number.".format(s, base)
    
    dotPos=s.find('.')
    if (dotPos == -1):
        return (int(s, base))
    places = len(s)-dotPos-1
    return float((1.0*int(s[:dotPos]+s[dotPos+1:],base)/(base**places)))
