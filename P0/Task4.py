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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

send_calls = {}
receiving_calls = []
send_texts = []
receiving_texts = []
for call in calls:
   # use dictionary to make sure there is only one entry for each call
   send_calls[call[0]] = None
   receiving_calls.append(call[1])

for text in texts:
   send_texts.append(text[0])
   receiving_texts.append(text[1])

for call in receiving_calls:
   if call in send_calls:
       del send_calls[call]

for text in send_texts:
   if text in send_calls:
       del send_calls[text]

for text in receiving_texts:
   if text in send_calls:
       del send_calls[text]

# Convert dictionary to list
send_call_converted = [k for k in send_calls]
send_call_converted.sort()

print("These numbers could be telemarketers: ")
for num in send_call_converted:
   print(num)
