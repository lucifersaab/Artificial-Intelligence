 
list1=list();

def reversal(x):
  return x[::-1]


for i in range(3):
    print("name ",i+1)
    name = input()
    reversed=reversal(name)
    list1.append(reversed);

print(list1)