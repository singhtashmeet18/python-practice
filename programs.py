#string is palindrome or not


string = input("enter a string:")
string = string.casefold()
rev_string = reversed(string)
if list(string) == list(rev_string):
  print("the string is palindrome.")
else:
  print("string is not pslindrome.")














