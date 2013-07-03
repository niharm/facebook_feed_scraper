README for Feed Scraper
Nihar Madhavan
07/03/2013

INTRODUCTION
============
These are the Python scripts used in the "" project at http://www.princeton.edu/~madhavan/TAandTCAnalysis/.

They can be used to analyze any facebook feed you have access to! (be sure to get a Facebook access code from https://developers.facebook.com/tools/explorer/)


USAGE
=====

Scrape Data
-------------------------
Run "feed_scraper.py" 
--- Update the variables in the first section
--- Scrapes messages, likes, datetime submission, and tagged users from a given Facebook url, with a given Facebook access code.
--- Outputs tags and top words to .csv files. 
--- Outputs dates to .txt file which can be read with date_counter.py. 
--- Message text is saved in a variable 'text'. Prints number of likes.


Count Posts by Date
-------------------------
- Run "date_counter.py"
--- Takes in a .txt file with a list of datetimes.
--- Outputs a .csv file with the frequency by date.

