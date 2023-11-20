def swap_case(s):
    newValue=""
    for i in range(len(s)):
        if s[i].isupper():
            newValue += s[i].lower()
        else:
            newValue += s[i].upper()
    return newValue