'''
MIT License

Copyright (c) 2024 Federico Grosso, Tommaso Vallone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

#Description: In a village, an n number of families have children until a boy comes out

import random
import matplotlib.pyplot as plt

families = 5000000  # Number of families
males = 0  # Count of male children
females = 0  # Count of female children
ratio = []  # List of male/female ratios

# Generate children for each family
for _ in range(families):
    while True:
        newborn = random.randint(0, 1)  # Male = 1, Female = 0
        if newborn == 1:
            males += 1
            break
        females += 1

    # Append the male/female ratio at each step (only if there are females to avoid division by zero)
    if females > 0:
        ratio.append(males / females)

# Print the number of males, females, and the final ratio
print(f"Number of males: {males}")
print(f"Number of females: {females}")
print(f"Ratio males/females: {males/females}")

# Plot the male/female ratio progression
plt.plot(ratio)
plt.ylabel('Ratio male/female')
plt.xlabel('Number of families')
plt.show()
