print("หาพื้นที่สี่เหลี่ยมคางหมู")
def area(w,l):
    x = 0.5 * w * l
    return x
a = int(input("input  ความยาวของเส้นทแยงมุม : "))
b = int(input("input ผลบวกของความยาวของด้านคู่ขนาน : "))
print(("ผลลัพธ์ คือ "),area(a,b,))