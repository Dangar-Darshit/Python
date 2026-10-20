for x in range(3):
    continue
else:
    print("A")
#Yes, it will run because there is continue statement which only skips value but loop will complete so after that else block will print "A"

for x in range(3):
    break
else:
    print("B")
#No, the loop will be terminated so it will not come to else block.


for x in range(0):
    print(x)
else:
    print("C")
#Yes, the loop will complete and comes  to else block and prints "C"