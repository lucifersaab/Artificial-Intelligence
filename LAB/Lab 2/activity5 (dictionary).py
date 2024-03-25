list1=['hashim','fahad','ali']
list2=[10,20,30]

dic2={list1[i]:list2[i] for i in range(3) if len(list1)==len(list2)}

print(dic2)