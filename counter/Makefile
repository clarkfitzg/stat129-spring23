test: counter.py testdata.txt
	python3 $< < testdata.txt 

counts.csv: counter.py 
	zgrep "TAVG" /stat129/2022.csv.gz | cut -d, -f4 | python3 $< > $@

