
import pandas
import seaborn
from matplotlib import pyplot

# Data
crimes = pandas.read_csv("crimeRatesByState2005.csv")
mpg = pandas.read_csv("mpg.csv")

# Plot of distribution, one variable
seaborn.distplot(crimes["robbery"])

# Save figure and then clear plot
pyplot.savefig("robbery.png")
pyplot.clf()


# Plot of 2 numerical variables
seaborn.jointplot(x=crimes["robbery"], y=crimes["murder"])

# Save figure and then clear plot
pyplot.savefig("robbery_murder.png")
pyplot.clf()



# Plot of a categorical (x) versus a numerical (y)
seaborn.violinplot(x=mpg["class"], y=mpg["cty"])

# Save figure and then clear plot
pyplot.savefig("class_cty.png")
pyplot.clf()

