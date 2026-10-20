for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")



# 1
# 3
# else will not print because break will terminate the loop.