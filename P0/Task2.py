"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
current_max_number = ""
current_max_time = 0

for call in calls:
    if int(call[3]) > current_max_time:
        current_max_number = call[0]
        current_max_time = int(call[3])

print ("{} spent the longest time, {} seconds, on the phone during September 2016.".\
       format(current_max_number,current_max_time))