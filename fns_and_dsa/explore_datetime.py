from datetime import datetime, timedelta

# ✅ الجزء 1: عرض التاريخ والوقت الحالي
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date  # نرجعه علشان نستخدمه في الجزء الثاني

# ✅ الجزء 2: حساب التاريخ المستقبلي
def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# ✅ البرنامج الرئيسي
def main():
    # عرض التاريخ الحالي
    current_date = display_current_datetime()

    # طلب عدد الأيام من المستخدم
    try:
        user_input = input("Enter the number of days to add to the current date: ")
        days = int(user_input)
        calculate_future_date(current_date, days)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
