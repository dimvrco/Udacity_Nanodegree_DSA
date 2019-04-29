"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
records = {}

for text in texts:
    records[text[0]] = ""

for call in calls:
    records[call[0]] = ""

length_of_records = len(records)

print ("There are {} different telephone numbers in the records.".format(length_of_records))