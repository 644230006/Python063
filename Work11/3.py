print(" สูตรการหาปริมาตรทรงกระบอก ")
def area(w,h):
    x = 3.14 * (w**2) * h
    return x
a = int(input("input  รัศมี : "))
b = int(input("input  ความสูง : "))

print(("ผลลัพธ์ คือ "),area(a,b))