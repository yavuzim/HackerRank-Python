if __name__ == '__main__':
    s = input()
    for f in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(f(c) for c in s))