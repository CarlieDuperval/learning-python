# we will run a loop from starting to length/2 and check the first to the last character of the string

# 0- check if the string is Palindrome or not 
#  run loop from o to length/2: for i in range( 0, int(len(str)/2)) to check if srt[i] != srt[len(srt)-i-1] in this cas return false

from re import S


def isPalindrome(string):
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            return False
    return True
s = "mioim"
result = isPalindrome(s)

if (result):
    print("Yes This is a Palindrome")
else:
    print("No This is not a Palindrome")
