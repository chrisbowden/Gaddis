# This program displays a simple bar chart
import matplotlib.pyplot as plt

def main():
    # Create a list with the X coordinates of each bars left edge
    left_edges = [0,10,20,30,40]

    # Create a list with the heights of each bar
    heights = [100,200,300,400,500]

    # Create a variable for the bar width
    bar_width = 10

    # Build the bar chart
    plt.bar(left_edges, heights, bar_width, color =('r', 'g', 'b', 'y', 'k'))

    # Add the title
    plt.title('Sales by Year')

    # Add labels to the axis
    plt.xlabel('Year')
    plt.ylabel('Sales')

    # Customise the tick marks
    plt.xticks([5,15,25,35,45], ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0,100,200,300,400,500],['$0m','$1m','$2m','$3m','$4m','$5m'])

    # Display the chart
    plt.show()

# Call the main function
main()