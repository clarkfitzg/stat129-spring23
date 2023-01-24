# Tue Jan 24 21:18:22 UTC 2023
# https://registry.opendata.aws/noaa-ghcn/

# NOAA Global Historical Climatology Network Daily (GHCN-D)

# Last 10 years seems fine
for yr in {2013..2022}
do
	wget "https://noaa-ghcn-pds.s3.amazonaws.com/csv.gz/${yr}.csv.gz"
	gunzip ${yr}.csv.gz
done

# for year in range(
# https://noaa-ghcn-pds.s3.amazonaws.com/csv.gz/1810.csv.gz
