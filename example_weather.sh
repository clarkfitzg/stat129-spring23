
# Thu Feb  2 20:41:32 UTC 2023
# Get some weather data for playing around in class.

grep -i "Sacramento" /stat129/ghcnd-stations.txt > sac_stations.csv

zcat /stat129/2022.csv.gz | grep "US1CASA0011|USW00093225" | head > 2022small.csv

zcat /stat129/2022.csv.gz | grep "USW00093225" | head >> 2022small.csv

