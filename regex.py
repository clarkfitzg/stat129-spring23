import re


x = " Hello Clark, I'm Carl. The cat is outside.   "

# Goal: Words that start with a capital C.
# Start small, work your way up.
re.findall("C", x)
re.findall("C\S*", x)

# r for raw strings- this tells Python to ignore all special
# formatting characters.
r'''hello\nthere'''

'''hello\nthere'''

'''hello
there'''


# re.VERBOSE helps with readability
p1 = re.compile(r'''
C       # Single capital C
\S*     # non whitespace character 0 or more times
''', re.VERBOSE)

type(p1)

re.findall(p1, x)


# Suppose we don't want the period
p2 = re.compile(r'''
C       # Single capital C
\w*     # 0 or more alphanumeric characters
''', re.VERBOSE)
re.findall(p2, x)


# All capital words
p3 = re.compile(r'''
[A-Z]   # capital
\w*     # 0 or more alphanumeric characters
''', re.VERBOSE)
re.findall(p3, x)

# Does [A-F] find all capital letters between A and F?
# Perform an experiment and test it.


# Task: strip (remove) leading and trailing whitespace

# Using a regular expression
p4 = re.compile(r'''
\S      # non whitespace
.*      # Anything
\S      # non whitespace
''', re.VERBOSE)
re.findall(p4, x)[0]


# Using a string method
x.strip()

# The string method is much clearer.
# What's the lesson here?


# Exercise: find the names and salutations in 
xmen = "Yesterday, Ms. Grey met Dr. Xavier and Mr. Logan"
