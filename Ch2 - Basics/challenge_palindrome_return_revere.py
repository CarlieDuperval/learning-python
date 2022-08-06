#  this function will return the reverse of the string

def isPalindrome(string):
    return string == string[::-1]

string = "MADAM"
result = isPalindrome(string)

if result:
    print("Yes this is a Palindrome")
else:
    print('No this is not a Palindrome')





