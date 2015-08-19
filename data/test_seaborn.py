
import matplotlib.pyplot as plot
import pandas
import seaborn

# Data
crimes = pandas.read_csv("crimeRatesByState2005.csv")
mpg = pandas.read_csv("mpg.csv")

# Plot of distribution, one variable
seaborn.distplot(crimes["robbery"])

# Save figure and then clear plot
plot.savefig("robbery.png")
plot.clf()


# Plot of 2 numerical variables
seaborn.jointplot(x=crimes["robbery"], y=crimes["murder"])

# Save figure and then clear plot
plot.savefig("robbery_murder.png")
plot.clf()



# Plot of a categorical (x) versus a numerical (y)
seaborn.boxplot(x=mpg["class"], y=mpg["cty"])

# Save figure and then clear plot
plot.savefig("class_cty.png")
plot.clf()

