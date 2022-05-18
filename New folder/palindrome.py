def Palindrome(s):
   rev = ''.join(reversed(s))
   if (s == rev):
       return True
   return False
    
string = input('Enter the string: ')

if (Palindrome(string)):
  print(string,'is a Palindrome')
else:
  print(string,'is not a Palindrome')