x = int(input("แม่ของสูตรคูณ : "))
p = int(input("เริ่มจาก : "))
m = int(input("คูณทั้งหมด : "))
while p <= m:
    print("%d * %d = %d" % (x , p ,x * p))
    p+=1