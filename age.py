from datetime import datetime, date
# Current date in the format yyyy-mm-dd
today = date.today()
current_day = today.day
current_month = today.month
current_year = today.year

# Valid input + extracting day month and year
while True:
    entered_date = input("Please enter your date of birth (dd-mm-yyyy): ").strip()
    try:
        birth_date = datetime.strptime(entered_date, "%d-%m-%Y").date() #Checking for valid date in the correct format
        input_day = int(entered_date[:2])
        input_month = int(entered_date[3:5])
        input_year = int(entered_date[6:])
    except ValueError:
        print("Thats not a valid date or format - please use the format dd-mm-yyyy")
        continue
    if birth_date > today:
        print("That is a future date - please try again")
        continue
    break

# Age calculation + logic
year = current_year - input_year
if (input_month > current_month) or (input_month == current_month and input_day > current_day):
    year -= 1

print(year)

#Testing datetime
# print(birth_date)
# print(date.today())
# print(today)
# print(today.year,today.month,today.day)

