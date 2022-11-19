#in simple hindi its called ulta sidha ek saman as NITIN
def palindrome():
    a = input("enter your name :  ")
    # you have to know that this line "b =" convert a string into a reverse string ...
    b = a[::-1]
    if a==b:
      # here we check our reverse and original string is equal or not , simple ....
        print("your name is palindrome ...")
    else :
        print("your name is not a palindrome...")
palindrome()
# so lets run and check your name fast ......
