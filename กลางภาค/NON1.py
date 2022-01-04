a = int(input("กรอกตัวเลขที่ 1 :"))
b = int(input("กรอกตัวเลขที่ 2 :"))
print("ท่านจะดำเนินการด้วยวิธีใด \n 1. บวก \n 2. ลบ \n 3. คูณ \n 4. หาร \n 5. หารเอาเศษ  ") 
op =int(input("ดำเนินการด้วยวิธีใด :  "))
if op == 1:
    print(a + b)
elif op == 2:
    print(a - b)
elif op == 3:
    print(a * b)
elif op == 4:
    print(a - b)
elif op == 5:
    print(a % b)