while True:
    print("Enter 'x' for exit: ")
    num = int(input("Enter any number: "))
    num1 = "{0:b}".format(num)
    if num == 'x':
        break
    else:
        number = int(num1)
        orig = number
        rev = 0
        while number > 0:
            rev = (rev*10)+number%10
            number //= 10
        if orig == rev:
            print(orig, "is a palindrome number ")
        else:
            print(orig, "is not a palindrome Number ")
