BUCKET = s3://noaa-ghcn-pds/csv.gz/by_year

size:
	aws s3 ls $(BUCKET) --no-sign-request --summarize --human-readable --recursive

download:
	aws s3 cp $(BUCKET) /stat129 --no-sign-request --recursive
