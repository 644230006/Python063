age = int(input("กรุณากรอกอายุ : "))
if age < 10:
    print("เด็กจัง")
elif age < 20:
    print("คุณเป็นวัยรุ่น")
elif age < 30:
    print("วัยหนุ่มสาว")
elif age < 60:
    print("วัยทำงานแล้วนะ")
else:
    print("เป็นคนแก่แล้วนะ")