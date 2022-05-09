#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: gets a grade level from user and returns the associated middle
# percentage

# this function matches up the grade with the percentage and returns the
# middle percentage
def calc_grade(grade):
    # if statement matches up the levels with the percents
    if grade == "4++":
        percent = "100%"
    elif grade == "4+":
        percent = "98%"
    elif grade == "4":
        percent = "91%"
    elif grade == "4-":
        percent = "83%"
    elif grade == "3+":
        percent = "78%"
    elif grade == "3":
        percent = "75%"
    elif grade == "3-":
        percent = "71%"
    elif grade == "2+":
        percent = "68%"
    elif grade == "2":
        percent = "65%"
    elif grade == "2-":
        percent = "61%"
    elif grade == "1+":
        percent = "58%"
    elif grade == "1":
        percent = "54%"
    elif grade == "1-":
        percent = "51%"
    elif grade == "R":
        percent = "Percent is less than 50%"
    else:
        percent = "level inputted was invalid"

    return percent


def main():
    # get user input
    grade = input("Enter the grade level to be converted to the middle percent: ")
    # setting a variable to the return value of calc_grade
    calculated_grade = calc_grade(grade)
    # displays the results
    if calculated_grade == "level inputted was invalid":
        print(calculated_grade)
    else:
        print("The middle percent of {} is {}.".format(grade, calculated_grade))


if __name__ == "__main__":
    main()
