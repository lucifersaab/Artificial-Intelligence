hello="hello"
world="world"
print(hello)
print(world)

newWord=hello+" "+world
print(newWord)
print(len(newWord))
hw12 = '%s %s %d' % (hello, world, 12)
print(hw12)

print(world.rjust(6))
print(hello.center(8))
print(world.replace('l', '(ell)'))
print('  world '.strip()) 