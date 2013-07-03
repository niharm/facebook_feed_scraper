################################################

# feed_scraper.py
# Created by Nihar Madhavan
# Updated: July 3, 2013

# Description:

## Scrapes messages, likes, datetime submission, and
## tagged users from a given Facebook url, with a given
## Facebook access code. Outputs tags and top words
## to .csv files. Outputs dates to .txt file which can
## be read with date_counter.py. Message text is saved
## in a variable 'text'. Prints number of likes.

################################################

# UPDATE THESE VARIABLES

# Facebook User ID 
## Tiger Compliments = 100004671882599
## Tiger Admirers = 100004851400279
facebook_id = '100004671882599'

#number of top words desired
top_word_count = 1000

# Facebook Access Code
## Temporary Code; required to obtain posts
## Obtained from https://developers.facebook.com/tools/explorer/ (set permissions correctly)
## Sample: 'CAACEdEose0cBAIaXUWr8j61yGpAtlnQYvjrENh68ajDsUgdf3aFcvAsaQvubJkkMvXuZCKY0zfjLzHsveGs0GL0YIU5Lo6d7XnLgj1ZCfkHU39bNKZCmZA4HfyFA38nHO5gBxA95godyRDudyBlZCw461FzQwYMsZD' 
access_code = 'CAACEdEose0cBAJcjbhcGdjwqSs15ie4rqb2qWjCYug8bAx9NsZBSR1Enuc7L6O2E9IyacKZAqZBciXzrDIFXbHZAQ4ZAZBie4wXfPrrxamvgNzrLotTYaNoYAJmAfspZAYZBI8ZCPWdaF4K0Kc6KaZAtkPI4ZCfPvSJVXsZD' 

# Filenames
datefile = 'feed_dates.txt'
tagfile = 'feed_tags.csv'
wordfile = 'feed_words.csv'

################################################

from urllib.request import urlopen
import json
from collections import Counter
import re
import datetime
import matplotlib.pyplot as plt


#declare empty variables
dates = list() # for dates
text = '' # string for message text
tags = Counter() # to count tags
likes = 0 #to count likes
count = 0 #counts posts so far

#dates file
f_dates = open(datefile, 'w')

#get json format dictionary from url
def get_dict(url):
    response = urlopen(url)
    json_text = response.read().decode("utf-8")
    current_page = json.loads(json_text)
    return current_page

#form url from preset url and above parameters
base_url = 'https://graph.facebook.com/'
specifications = '/feed?fields=message,message_tags,likes,comments.fields(message,from,like_count,message_tags)&access_token='
initial_url = base_url + facebook_id + specifications + access_code

#get first page
current_page = get_dict(initial_url)

#while loop to get pages (until broken below)
while(1):

    #print posts obtained so far
    print('Posts Obtained: ', count, '\n')
    
    # get data from current page 
    current_page_data = current_page['data']

    # go through all the items (individual posts) in feed
    for item in current_page_data:
        
        #get message
        if 'message' in item:
            #print and write message
            text += (item['message'] + '\n')

            #update count
            count += 1

        #if post is not a message post (ex. an event) reject it and print
        else:
            print('(1 non-message post rejected)', '\n')

        #count likes
        if 'likes' in item:
            likes += item['likes']['count']
            
        #get tags
        if 'message_tags' in item:
            # get tags
            for tag_index in item['message_tags']:
                id = item['message_tags'][tag_index][0]['id']
                tags[id] += 1

        #get date the post was created and append to dates array
        if 'created_time' in item:
            date_string = item['created_time']
            date = datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S+0000')
            f_dates.write(str(date))
            f_dates.write('\n')
            dates.append(date)

    #if there is a next page, load the url in 'next'
    if 'paging' in current_page:
        #update current page
        next_url = current_page['paging']['next']
        current_page = get_dict(next_url)

    # if there is no page next, break the loop
    else:
        break

#close date writing stream
f_dates.close()
print('Datetimes saved in file: ' + datefile)

### GET TOP WORDS

# get the most common words in a list
words = re.findall('\w+', text.lower())
word_counter = Counter(words).most_common(top_word_count)

#save the top words in a file
f_words = open(wordfile, 'w')
for i in range(0, top_word_count):
    word = word_counter[i][0]
    count = word_counter[i][1]
    f_words.write(word + ', ' + str(count) + '\n')
f_words.close()

print('Top ' + str(top_word_count) + ' words saved in file: ' + wordfile)

### GET TAGS

#save the people with tags and the number in a csv file
f_tags = open(tagfile, 'w')
for tag in tags:
    f_tags.write(str(tag) + ', ' + str(tags[tag]) + '\n')
f_tags.close()
print('Tag ids and counts saved in file: ' + tagfile)

### PRINT LIKES
print('Like Count: ' + str(likes))

### PRINT TEXT VARIABLE
print('Text saved in variable \'text\'')

#complete
print('All done!')
