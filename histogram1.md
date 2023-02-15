## Feedback

I understand that pandas can load 95 million records, but the idea was to do this by streaming in bash and use the much smaller file of counts.
For a larger data set this pandas approach will fail while the bash one will still work.


Q1- Explain what each step of this pipeline does.

Q2- How many temperature observations total did you find? Explain how you calculated this from the above statistics.

Q3- These frequencies are too low for the whole data set- they don't add up to 95 million.
Q3- The X and Y axes need to be swapped for the histogram I believe.
Q3- Plot the histogram.
Q3- Explain the left skew (long left tail) of the histogram.
Q3- Units are tenths of degrees celsius
Q3- Range of histogram doesn't match what's in the data.

Q4- Identify the bottleneck using htop output.
Q4- Look again at your htop output- the bottleneck isn't awk.
