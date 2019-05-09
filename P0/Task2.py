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

# Create dictionary, where the phone number is the key and the duration is call minutes total
call_tallies = {}

# Iterate through the call list and add call length to the dict entry of the sender and receiver
for call in calls:
    current_call_time = call[3]
    if call[0] in call_tallies:
        call_tallies[call[0]] += int(current_call_time)
    else:
        call_tallies[call[0]] = int(current_call_time)

    if call[1] in call_tallies:
        call_tallies[call[1]] += int(current_call_time)
    else:
        call_tallies[call[1]] = int(current_call_time)


# Iterate through the dictionary and identify the max time, return the stats
current_max_number = ""
current_max_time = 0

for current_num, current_time in call_tallies.items():
    if current_time > current_max_time:
        current_max_number, current_max_time = current_num, current_time

print ("{} spent the longest time, {} seconds, on the phone during September 2016.".\
       format(current_max_number,current_max_time))