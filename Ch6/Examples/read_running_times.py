# This progrma reads the running time values

FILE = "video_times.txt"

def main():
    # Open the file for reading
    video_file = open(FILE, "r")

    # Initialise an accumulator
    total = 0.0

    # Init video count
    count = 0

    print("Here are the running times for each video:")

    # Get the values from the file and total them
    for line in video_file:
        # Convert to float
        run_time = float(line)

        # Add 1 to the count
        count += 1

        # Display the time
        print("Video #", count, ": ", run_time, sep='')

        # Add the total to the total run time
        total += run_time

    # Close the file
    video_file.close()

    # Display totals
    print("The total running time is", total, "seconds.")

main()

