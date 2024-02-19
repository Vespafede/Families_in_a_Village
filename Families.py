'''
Authors: Federico Grosso, Tommaso Vallone
Description: In a village, an n number of families have children until a boy comes out
'''
import random
import matplotlib.pyplot as plt

families = 5000000 # Number of families (WARNING: it is recommended not to enter a number greater than about 5 million or the time to run the program could become very long)
family = [] # List of newborns in a family
newborns = [] # All newborns list
ratio = [] # List of male/female ratios for families
males = 0 # Numbers of males
females = 0 # Numbers of females

# Do the cycle until we reach the number of families
for x in range(families):
    newborn = random.randint(0,1) # Male = 1, Female = 0
    family.append(newborn)
    # Make a new child until one is male
    while newborn != 1:
        newborn = random.randint(0,1)
        family.append(newborn)
    newborns.append(family)
    family = []

# Count the number of males and females for each family and calculate the ratio
for eachfamily in newborns:
    males += eachfamily.count(1)
    females += eachfamily.count(0)
    ratio.append(males/females)

# Print the number of males, of females and the ratio
print(f"Number of males: {males}")
print(f"Number of females: {females}")
print(f"Ratio males/females: {males/females}")

# Create the ratio progression chart
plt.plot(ratio)
plt.ylabel('Ratio male/female')
plt.xlabel('Number of couples')
plt.show()
