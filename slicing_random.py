
# Slicing

x = 'abcdef'

# The element of x starting at position 2
x[2]

# elements starting at position 2 through position 4
x[2:4]

# elements starting at position 2 through the end
x[2: ]

# elements up until position 2
x[ :2]

# What happens?
# Slices like this partition the whole into two pieces
x[ :2] + x[2: ]

# last element
x[-1]

# last 3 elements
x[-3: ]

# every 2nd element
x[::2]

# every 2nd element from position 1 to up to 5
x[1:5:2]

############################################################# 

# Standard library
import random

# Pick 1 random elements from n
random.choice(range(n))

# Pick 5 random elements from n
n = 100
random.sample(range(n), 1)

# combine with conditional statement
x = random.choice(range(n))
if x < 50:
    print("small")
else:
    print("big")
