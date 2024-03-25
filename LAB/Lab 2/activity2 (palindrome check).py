 

def reversal(x):
  return x[::-1]

def isPalindrome(x,y):
   return x==y


print("string: ")
name = input()
reversed=reversal(name)

print("Is palindrome: ",isPalindrome(name,reversed)
)
