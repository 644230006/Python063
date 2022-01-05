print("หาปริมาตรสี่เหลี่ยมมุมฉาก")
def area(w,h,hi):
    x = (w * h * hi)
    return x
a = int(input("input  ความกว้าง : "))
b = int(input("input  ความยาว : "))
c = int(input("input  ความสูง : "))
print(("ผลลัพธ์ คือ "),area(a,b,c))