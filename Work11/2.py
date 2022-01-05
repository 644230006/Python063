print(" สูตรการหาปริมาตรทรงกรวย ")
def area(w):
    x = (4/3) * 3.14 * (w**3)
    return x
a = int(input("input  รัศมี : "))

print(("ผลลัพธ์ คือ "),area(a))