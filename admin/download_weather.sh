# Tue Jan 24 21:18:22 UTC 2023
# https://registry.opendata.aws/noaa-ghcn/

# NOAA Global Historical Climatology Network Daily (GHCN-D)

for yr in {1900..2022}
do
	wget "https://noaa-ghcn-pds.s3.amazonaws.com/csv.gz/${yr}.csv.gz"
	# Nah, let's deal with data as it exists.
	#gunzip ${yr}.csv.gz
done
