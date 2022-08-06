#  Create a program that detects whether a string of characters is a palindrome. // A palindrome is a string that reads the same way both forward and backward minus any white space and punctuation
#  MADAM is palindrome
# 0- check if srt is palindrome if the reverse word == word: def isPalindrome(s): // return  s == s[::-1]
# 1- let set a variable :  result = isPalindrome(s)
# 3- if result: print("Yes") // else: print("No")


# import string


def isPalindrome(string):

    # Used predifine function to resverse to the string
    strreverse = ''.join(reversed(string))

    # Cheking if both string are equal or not
    if (string == strreverse):
        return True
    return False

string = "MADAM"
result = isPalindrome(string)

if (result):
    print('Yes This is Palindrome')
else:
    print("No This is not Palindrome")

