#ให้เขียนโปรแกรมคำนาณหาค่า GPA โดยมีเงื่อนนไขว่าถ้าค่า GPA 3.70 คุณได้รับเกียรตินิยมอันดับ 1 
# ถ้าค่า GPA 3.00 คุณได้รับเกียรตินิยมอันดับ 2 
# ถ้าค่าGPA 2.00 คุณเรียนจบแน่นอน ถ้า GPA น้อยกว่า 2.00 คุณคงเรียนไม่จบแน่นอน
gpa = float(input("กรุณากรอก เกรดของคุณ : "))
if gpa >= 3.70:
    print("ได้รับเกียรตินิยม อันดับ 1")
elif gpa >= 3.00:
    print("ได้รับเกียรตินิยม อันดับ 2")
elif gpa >=  2.00:
    print("คุณเรียนจบแน่นอน")
else:
    print("คุณคงเรียนไม่จบ")
