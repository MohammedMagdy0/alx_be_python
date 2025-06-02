# pattern_drawing.py

# طلب إدخال حجم النمط من المستخدم
size = int(input("Enter the size of the pattern: "))

# التحقق إن الرقم موجب
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")  # طباعة النجوم في نفس السطر
        print()  # الانتقال لسطر جديد بعد نهاية الصف
        row += 1

