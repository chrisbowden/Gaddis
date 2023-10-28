# Program to display totals in sales data file

def main():
    # init the accumulator
    total = 0.0

    try:
        # Open sales data file
        infile = open("sales_data.txt")

        # Read the file
        for line in infile:
            amount = float(line)
            total += amount

        # Close the file
        infile.close()

        # print totals
        print(format(total, ",.2f"))
    except IOError:
        print("An error has occurred trying to read the file")
    except ValueError:
        print("Non-numeric data was found in the file")
    except:
        print("An error has occurred")

main()
