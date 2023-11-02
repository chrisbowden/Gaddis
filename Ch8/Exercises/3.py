# Data printer

def main():
    the_date = input("Enter the date in the format mm/dd/yyyy: ")

    date_list = the_date.split("/")

    day = date_list[1]
    month = date_list[0]
    year = date_list[2]

    if month == "01":
        month_long = "January"
    elif month == "02":
        month_long = "February"
    elif month == "03":
        month_long = "March"
    elif month == "04":
        month_long = "April"
    elif month == "05":
        month_long = "May"
    elif month == "06":
        month_long = "June"
    elif month == "07":
        month_long = "July"
    elif month == "08":
        month_long = "August"
    elif month == "09":
        month_long = "September"
    elif month == "10":
        month_long = "October"
    elif month == "11":
        month_long = "November"
    else:
        month_long = "December"

    print ("The date you entered is", month_long, day, year)

main()