from datetime import *

print("\nQ1")
def today_day():
    """ Use the datetime module to write a program that gets the current date and prints the day of the week.
    """
    return datetime.today().strftime("%A")
print(today_day())

print("\nQ2")
def birthday_countdown(birth_date): # yyyy, mm, dd
    """ Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday.
    """
    today = date.today()
    birthday = birth_date.replace(year = today.year)
    birthday = birthday.replace(year = birthday.year + 1) if birthday <= today else birthday
    age = today.year - birth_date.year - 1 if birth_date.year == birthday.year else today.year - birth_date.year - 1
    countdown = datetime(birthday.year, birthday.month, birthday.day, 0, 0, 0) - datetime.now()
    return f"You are currently {age} years old\nIt is {countdown.days} days, {countdown.seconds // 3600} hours, {countdown.seconds // 60 % 60} minutes, and {countdown.seconds % 60} seconds until your next birthday"

print(birthday_countdown(date(1998, 8, 26)))

print("\nQ3")

def double_day(date_1, date_2):
    """ For two people born on different days, there is a day when one is twice as old as the other. That’s their Double Day. Write a program that takes two birthdays and computes their Double Day.
    """
    d1 = min(date_1, date_2)
    d2 = max(date_1, date_2)
    double_day = (d2 - d1).days # double_day is this many days from d2
    return d2 + timedelta(days = double_day)

print(double_day(date(1998, 8, 26), date(1969, 7, 16)))

print("\nQ4")

def product_day(date_1, date_2, product):
    """ For a little more challenge, write the more general version that computes the day when one person is n times older than the other.
    """
    d1 = min(date_1, date_2)
    d2 = max(date_1, date_2)
    difference = (d2 - d1).days
    product_day = difference/(product - 1)
    return d2 + timedelta(days = product_day)

print(product_day(date(1998, 8, 26), date(1969, 7, 16), 3))