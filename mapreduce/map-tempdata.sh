#zgrep $1 "TMAX" | cut -d"," -f 4 | python3 map-count.py counts/$1.pickle
zgrep $1 "TMAX" | head | cut -d"," -f 4 | python3 map-count.py counts/$1.pickle
