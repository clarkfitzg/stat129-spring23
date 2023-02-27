#zgrep "TMAX"  | cut -d, -f4 | head

# Which stations have complete data?
# That is, TAVG observations for 365 days every year?
# This would probably be easier to do with a SQL database.
# Pandas would also work fine.
# This would all be easier if it were sorted by station first, and day of the year second.
# Let's break this up into pieces.
# First, let's count the times each station appears.

# What's my goal here?
# prepare for tomorrow's lectures.
# STAT 129 needs to see Python processing stdin
# STAT 196L needs a data set.
# It's probably sufficient to just start with one station.


zcat /stat129/*csv.gz | grep "TAVG" | head
