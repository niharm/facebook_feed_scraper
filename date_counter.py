################################################

# date_counter.py
# Created by Nihar Madhavan
# Updated: July 3, 2013

# Description:

## reads in datetimes from dates from given file (default: feed_dates.txt)
## writes frequencies to given file (default: date_counts.txt)
## used with feed_scraper.py

################################################

from collections import Counter

# FILENAMES
datefile = 'feed_dates.txt'
output_datefile = 'date_counts.csv'


#files
dates = open(datefile, 'r')
date_counts = open(output_datefile, 'w')

#date counter dict
date_counter = Counter()

#read in every line in the file f_read
for line in dates:
    
    # split the line and assign to different variables
    columns = line.split()
    
    date = columns[0]
    time = columns[1]

    date_counter[date] += 1
    
    times.write(time + '\n')
    

# write date counts
for date in date_counter:
    date_counts.write(date + ', ' + str(date_counter[date]) + '\n')

#close file reading
times.close()
date_counts.close()

print('done')
