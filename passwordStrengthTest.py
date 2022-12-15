# A Program to check strength of a password

Password = input("Enter Your Password ")
length = len(Password)

if(length >= 8):
    alphabetsSmall = []
    alpha = 'a'
    for i in range(0, 26):
        alphabetsSmall.append(alpha)
        alpha = chr(ord(alpha) + 1)

    alphabetsCapital = []
    Alpha = 'A'
    for i in range(0, 26):
        alphabetsCapital.append(Alpha)
        Alpha = chr(ord(Alpha) + 1)

    specialCharacters = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%',
                         '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
    numeric = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    k, j, l, m, = 0, 0, 0, 0
    for item in Password:
        if item in alphabetsSmall:
            k = 1
        if item in alphabetsCapital:
            j = 1
        if item in specialCharacters:
            l = 1
        if item in numeric:
            m = 1
    if(k == 1 and j == 1 and l == 1 and m == 1):
        print("Strong Password")

    else:
        print("Weak Password")
        if(m == 0):
            print("Numeric Value missing")
        if(k == 0):
            print("Small Alphabets missing")
        if(j == 0):
            print("Capital Alphabets missing")
        if(l == 0):
            print("Special Characters missing")


else:
    print("Password length is less than 8 ")
