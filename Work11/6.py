print("หาพื้นที่สามเหลี่ยม")
def area(width,length):
    x = 0.5 * width * length
    return x
a = int(input("input width : "))
b = int(input("input length : "))
print(("ผลลัพธ์ คือ "),area(a,b))