
import matplotlib.pyplot as plt
from pandas import read_csv
import seaborn as sns

# Data
crimes = read_csv("crimeRatesByState2005.csv")
mpg = read_csv("mpg.csv")

# Plot of distribution, one variable
sns.distplot(crimes["robbery"])

# Save figure and then clear plot
plt.savefig("robbery.png"); plt.clf()


# Plot of 2 numerical variables
sns.jointplot(x=crimes["robbery"], y=crimes["murder"])

# Save figure and then clear plot
plt.savefig("robbery_murder.png"); plt.clf()



# Plot of a categorical (x) versus a numerical (y)
sns.boxplot(x=mpg["class"], y=mpg["cty"])

# Save figure and then clear plot
plt.savefig("class_cty.png"); plt.clf()

