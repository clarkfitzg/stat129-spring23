
# Prepare
mkdir counts

# Map step
parallel bash map-tempdata.sh ::: /stat129/202*.csv.gz

# Reduce
python3 reduce.py > TMAX.txt

# Clean up
rm -r counts
