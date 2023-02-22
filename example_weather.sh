
# Thu Feb  2 20:41:32 UTC 2023
# Get some weather data for playing around in class.

grep -i "Sacramento" /stat129/ghcnd-stations.txt > sac_stations.txt

# TODO: modify so doesn't do multiple passes through data
RAWDATA=/stat129/2022.csv.gz 
EXAMPLE=2022small.csv

zcat $RAWDATA | grep -E "US1CASA0001" | head > $EXAMPLE
zcat $RAWDATA | grep -E "US1CASA0002" | head >> $EXAMPLE
zcat $RAWDATA | grep -E "US1CASA0058" | head >> $EXAMPLE
