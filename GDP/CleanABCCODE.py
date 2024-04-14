# Cleaner version of ABC Data for lecture Code

# Setup Dependancies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # Add some extra plotting capability
sns.set(context='talk', palette='colorblind') # Use a colorblind frendly palette
import csv

# Setup the constant to reference the file
#TABLE1 = "5206001_key_aggregates2.csv"
TABLE1 = "MarData.csv"

# The data for the column we want doesn't start until 1973, so we need to
# read through and discard the initial rows

# These next lines determine which columns we will select
QUARTER = 0
SEASONAL = 38   

# Setup the empty lists to accepts the data as we read it initial
quarters = []
GDP_Changes = []

# We are going to read in using the CSV reader method

with open(TABLE1, newline = '') as csvfile:
    reader = csv.reader(csvfile)
    # Read to the first row
    row = next(reader)
    # Check the value in Column zero isn't the one we need
    while row[QUARTER] != 'Dec-1973':
        row = next(reader) # CHew up and discard the unwanted rows
    # We exit the loop when we hit the row we want. We need
    # to store this row
    quarters.append(row[QUARTER])
    GDP_Changes.append(float(row[SEASONAL]))
    
    # We have the first row (1973) and can now start processing the rest
    for row in reader:
        #print(row[0], row[2]) This is a diagnostic line
        quarters.append(row[QUARTER])
        # This method checks if Row[2] is empty (it would return false if it was
        # Superced by the next Try Method
        #if row[2]:
        #    GDP_Changes.append(float(row[2]))
        #else:
        #    GDP_Changes.append(float('nan')) # Python reprsentaton of 'not a number'
        
        try:
            GDP_Changes.append(float(row[SEASONAL]))
        except ValueError:
            GDP_Changes.append(float('nan')) # If we catch the filue, put in 'nan'
            
# We should now have 2 lists GPD_Changes and quarters
# Quarters contains a reference to the actual quarter (eg Dec-1985)
# whilst GDP_Changes is the data for that quarter 

# Now we want to convert the GDP_Changes data into a Numpy array.
# Eachof these values will represent a value on the y-axis

GDPs = np.array(GDP_Changes)

# We need x-axis values to plot against the GDP Values. quarters wont work because they are text
# so we will create new numerical values using the numpy a-range (array range) function.
# The number of entries will have to match the number of GDP_Change entries

# This will create an array starting with 1973.25 and increasing by 0.25 until it hits the end
# 2020.25 will NOT be included

dates = np.arange(1973.75, 2020.25, 0.25)

# For this exercise, we only want dates fro 1995 onwards, so we will create a mask

mask = dates >= 1995

# We will be reusing the masks data, so will create a new masked copy

abc_dates = dates[mask]
abc_GDPs = GDPs[mask]

# In the case of the ABC graphs, the data was annualised, so a rolling average.
# We can create an array 4 deep to hold the data

# Numpy Sum allows us to choose which access to sum across

shifts = np.zeros((4, len(GDPs))) #Creates the new 4 deep array
shifts[0] = GDPs                    # Puts the original data in the first row
shifts[1, 1:] = GDPs[:-1]
shifts[2, 2:] = GDPs[:-2]
shifts[3, 3:] = GDPs[:-3]

# With Numpy.sum(0), this is basically summing down the 4 deep array and will result
# in a new array of the same lenght.
# Annualised represents the moving sum of growth

annualised = shifts.sum(0) # Note that sum(1) would have summed across, not down

# Of course annualised is all data, so we mask it to get 1995 onwards

abc_annualised = annualised[mask]

# The get_line function will create a list of y-values we can combine with x-vales to draw a line

def get_line(xs, slope, intercept):
    # xs represents a list of xvalues, so this will return the corressponding y values
    return slope * xs + intercept 
    
# The next piece of code will return an actual / specific value from our array
# The numpy.nozero returns a boolean where 1 is true so it is acting like a mask on the output
# The command returns a masked versin of the GDP data where supplied data for comparison
# is close to the recorded value

def gdp_noloop (date, dates, GDPs):
    
    return GDPs[np.nonzero(np.isclose(date, dates))[0][0]]

# Here are some temp Slope and Intercept values

slope=-0.170
intercept=343.4

# This is the plotting function we canand will use

def plot_trends (dates, gdps, slope, intercept, residuals=True):
    plt.figure(figsize= (10,5))
    plt.margins(0.08)
    if np.min(gdps) < 0 and np.max(gdps) > 0:
        plt.axhline(color='grey', marker = 5)
        plt.text(np.max(dates)+0.8, -0.5, 'x', color='grey')
    if np.min(dates) < 0 and np.max(dates) > 0:
        plt.axvline(color='grey', marker=6)
        plt.text(-0.8, np.max(gdps)+0.1, 'y', color='grey')
    
    plt.plot(dates, gdps, color='blue', linewidth=3)
    plt.plot(dates, slope * dates + intercept, linestyle='dashed', color='black', linewidth=3)
    
    if residuals:
        for (date, gdp) in zip(dates, gdps):
            prediction = slope * date + intercept
            plt.plot(np.array([date, date]), np.array([prediction,gdp]), color='red', linewidth=2, alpha=0.6)
    plt.show()

# Now we can move on to the Mean Average Error calculations

# Calculating the Mean Absolute Error with a loop
mysum = 0
n = len(abc_dates)
for i in range(n):
    mysum = mysum + abs(abc_annualised[i] - get_line(abc_dates[i], slope, intercept))
mae = mysum / n
print("MAE using Loops:",mae)

# Calculating with Numpy
mae2 = np.mean(np.abs(abc_annualised - get_line(abc_dates, slope, intercept)))
print("MAE using Numpy:",mae2)

# Calculating with Numpy (adjusted)
mae2_adapted = np.mean(np.abs(abc_annualised - get_line(abc_dates, slope, intercept-0.5)))
print("MAE using Numpy Adjusted:",mae2_adapted)

# Now we move on to the Mean Squared Error calculations
# In this version we will calculate the mean manually
def mse (sample_values, model_values):
    return np.sum((sample_values - model_values)**2)/len(sample_values)

# This version uses np.mean instead
def mse2 (sample_values, model_values):
    return np.mean((sample_values - model_values)**2)

# Method 3 using numpy square
def mse3 (sample_values, model_values):
    return np.mean(np.square(sample_values - model_values))

# Method 4 Combining Square and mean
def mse4 (sample_values, model_values):
    return np.square(sample_values - model_values).mean()


# This will now plot the two graphs and calaculate the MSE
plot_trends(abc_dates, abc_annualised, slope, intercept)
mse = mse4(abc_annualised, get_line(abc_dates, slope, intercept))
print("Slope:", slope, "\tIntercept:", intercept, "\tMSE:", mse)

plot_trends(abc_dates, abc_annualised, slope, intercept - 0.5)
mse_adapted = mse4(abc_annualised, get_line(abc_dates, slope, intercept- 0.5))
print("Slope:", slope, "\tIntercept:", intercept-0.5, "\tMSE:", mse_adapted)

print("Mean Average Error",(mae2_adapted-mae)/mae)
print("Mean Squared Error", (mse_adapted-mse)/mse)

# Root Mean Squared Error - Puts the error in the same units as Y
rmse = np.sqrt(mse)
rmse_adapted = np.sqrt(mse_adapted)
print(rmse, rmse_adapted, (rmse_adapted - rmse)/rmse)

# *** Least Squares Optimisation ***

# Determine the mdian point for daes, so we recenter data around median

print("Median of dates is:",np.median(abc_dates))

# New library
from sklearn.metrics import mean_squared_error as skmse


# Shifting the axis

# Old values just for reference
slope = -0.170
intercept = 343.4

# New Values shifted by Median
mdates = abc_dates - np.median(abc_dates) # Dates are now centred around the median
mslope = slope

# Remember the get_line would provide us with the predicted value. We will use it
# to work out what the new intercept shoudl be on the adjusted graph aroung the median

mintercept = get_line(np.median(abc_dates), slope, intercept) # This is the value of y when x is 2007.5 (the median)

# Plot the graph

# Print the original graphs with new centre
plot_trends (mdates, abc_annualised, mslope, mintercept)
print("Original")
print("Slope:", mslope, "\tIntercept:", mintercept, "\tMSE:", skmse(abc_annualised, get_line(mdates, mslope, mintercept)))

# Plot the graph with a new slope
plot_trends (mdates, abc_annualised, mslope+0.05, mintercept)
print("Slope +0.05")
print("Slope:", mslope+0.05, "\tIntercept:", mintercept, "\tMSE:", skmse(abc_annualised, get_line(mdates, mslope+0.05, mintercept)))

# Here is a function to change the slope using degrees not a random value ;-)

def rotate (slope, phi):
    phi_radians = phi/360 * 2 * np.pi
    return np.tan (phi_radians + np.arctan(slope))


# And run the plot

new_slope = rotate(mslope, 1) # Rotate clockwise by 1 degree
plot_trends (mdates, abc_annualised, new_slope, mintercept)
print("Slope + 1 degrees")
print("Slope:", new_slope, "\tIntercept:", mintercept, "\tMSE:", skmse(abc_annualised, get_line(mdates, new_slope, mintercept)))


# Here is an iteration to try finding  a better slope
new_slope = -0.17
mintercept = 2.125 # Both these values were previously calculated

new_mse = skmse(abc_annualised, get_line(mdates, new_slope, mintercept))
count = 0
print("Iteration:", count, "\tSlope:", new_slope, "\tMSE:", new_mse)

getting_better = True

while getting_better:
    old_slope = new_slope
    old_mse = new_mse
    count = count +1
    new_slope = rotate(old_slope, 1)
    new_mse = skmse(abc_annualised, get_line(mdates, new_slope, mintercept))
    print("Iteration:", count, "\tSlope:", new_slope, "\tMSE:", new_mse)
    getting_better = new_mse < old_mse

print("\nBest slope:", old_slope, "Best MSE:", old_mse)

# Plot the best we have so far
plot_trends (mdates, abc_annualised, old_slope, mintercept)

# Here we will define a function to run through a series of options to determine the best

def get_best_parameters(dates, gdps, paramlist):
    mses = [] # New empty list to store the results
    for (slope, intercept) in paramlist:
        eval_mse = skmse (gdps, get_line(dates, slope, intercept))
        mses.append((eval_mse, slope, intercept))
    return sorted(mses)[0]

# General purpose method to optimise slope

def optimise_slope( dates, gdps, start_slope, intercept, step):
    new_slope = start_slope
    new_mse = skmse(gdps, get_line(dates, new_slope, intercept))
    count = 0
    print("Iteration:", count, "\tSlope:", new_slope, "\tMSE:", new_mse)
    
    getting_better = True
    while getting_better:
        old_slope = new_slope
        old_mse = new_mse
        count = count +1
        
        # Try rotating in both directions
        (new_mse, new_slope, intercept) = get_best_parameters(dates, gdps, \
                                                              [(rotate(old_slope, step), intercept),\
                                                               (rotate(old_slope, -step), intercept)])
        print("Iteration:", count, "\tSlope:", new_slope, "\tMSE:", new_mse)
        getting_better = new_mse < old_mse
    print("\nBest slope:", old_slope, "Best MSE:", old_mse)
    return (old_slope, old_mse)

input("Get ready for Optimised Slope")
optimise_slope(mdates, abc_annualised, -0.17, 2.125, 0.5)

# General purpose method to optimise intercept

def optimise_intercept( dates, gdps, slope, start_intercept, step):
    new_intercept = start_intercept
    new_mse = skmse(gdps, get_line(dates, slope, new_intercept))
    count = 0
    print("Iteration:", count, "\tIntercept:", new_intercept, "\tMSE:", new_mse)
    
    getting_better = True
    while getting_better:
        old_intercept = new_intercept
        old_mse = new_mse
        count = count +1
        
        # Try increasing and decreasing
        (new_mse, slope, new_intercept) = get_best_parameters(dates, gdps, \
                                                              [(slope, old_intercept + step),\
                                                               (slope, old_intercept - step)])
        print("Iteration:", count, "\tIntercept:", new_intercept, "\tMSE:", new_mse)
        getting_better = new_mse < old_mse
    
    print("\nBest intercept:", old_intercept, "Best MSE:", old_mse)
    return (old_intercept, old_mse)

input("Get ready for Optimised Intercept")
optimise_intercept(mdates, abc_annualised, -0.17, 2.125, 0.1)



# General purpose method to optimise both

def optimise ( dates, gdps, slope, slope_step, intercept, intercept_step):
    new_slope = slope
    new_intercept = intercept
    new_mse = skmse(gdps, get_line(dates, slope, intercept))
    count = 0
    print("Iteration:", count, "\tMSE:", new_mse, "\tSlope:", new_slope, "\tIntercept:", new_intercept)
    
    getting_better = True
    while getting_better:
        (old_mse, old_slope, old_intercept) = (new_mse, new_slope, new_intercept)
        count = count +1
        
        # Try bothslope and intercept changes and pick the best
        (new_mse, new_slope, new_intercept) = get_best_parameters(dates, gdps, \
                                                              [(rotate(old_slope, slope_step), old_intercept),\
                                                               (rotate(old_slope, -slope_step), old_intercept),\
                                                               (old_slope, old_intercept + intercept_step),\
                                                               (old_slope, old_intercept - intercept_step)])
                              
        print("Iteration:", count, "\tMSE:", new_mse, "\tSlope:", new_slope, "\tIntercept:", new_intercept)
        getting_better = new_mse < old_mse
    
    print("\nBest MSE:", old_mse, "\nBest slope:", old_slope, "\tBest intercept:", old_intercept)
    return (old_mse, old_slope, old_intercept)

input("Get ready for Optimised Both")
optimise(mdates, abc_annualised, -0.17, 0.5, 2.125, 0.1)