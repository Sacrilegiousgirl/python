if __name__ == '__main__':
    s = input()
    isalnum = isalpha = isdigit = islower = isupper = False
    for i in s:
        if i.isalnum():
            isalnum = True
        if i.isalpha():
            isalpha = True
        if i.isdigit():
            isdigit = True
        if i.islower():
            islower = True
        if i.isupper():
            isupper = True
            
    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)