day_of_week = input("What day of the week is it today?").lower()

# print(day_of_week == "Monday") # Печатаешь Monday -> True
if day_of_week == "monday":
    print("Have a great start to your week!")

# if day_of_week != "Monday": # тоже самое, что внизу
elif day_of_week == "tuesday":
    print("It's tuesday")
else:
    print("Full seep ahead!")

print("This always runs")