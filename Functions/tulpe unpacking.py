food_rating = [('pizza', 8), ('chicken and rice', 10), ('clams', 8)]

for food in food_rating:
    print(food)

print('\n')

for food, rating in food_rating:
    print(food)

print('\n')

work_hours = [('abby', 100), ('billy', 54), ('maddy', 700)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return employee_of_month, current_max


print(employee_check(work_hours))
