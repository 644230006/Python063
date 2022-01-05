ls = []
Min = 0
Max = 0
x = int(input("เลขมีทั้งหมดกี่ตัว : "))
for i in range(x):
    ls.append(int(input("กรอกตัวเลขตัวที่ {0:d} : ".format(i + 1))))
for i in range(x):
    print("แสดงผลตัวเลข ครั้งที่ {0:d} : {1:.0f}".format(i + 1, ls[i]))
for i in ls:
    if Max < i:
        Max = i
Min = Max
for i in ls:
    if i < Min:
        Min = i
print("ค่าน้อยที่สุด คือ :", Min)
print("ค่ามากที่สุด คือ :", Max)