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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
- Fixed lines start with an area code enclosed in brackets. The area
  codes vary in length but always begin with 0.
- Mobile numbers have no parentheses, but have a space in the middle
  of the number to help readability. The prefix of a mobile number
  is its first four digits, and they always start with 7, 8 or 9.
- Telemarketers' numbers have no parentheses or space, but they start
  with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
<list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

codes_for_target_receiving_calls = {}
total_call_from_bangladore = 0
total_calls_to_bangladore = 0

for call in calls:
   # print(call)
   if call[0][:5] == "(080)":
       total_call_from_bangladore += 1
       receiving_num = call[1]
       # fixed line numbers are in ()
       if "(" in receiving_num:
           new_num = ""
           i = 1
           while receiving_num[i] != ")":
               new_num = new_num + (receiving_num[i])
               i += 1
           # print(new_num)
           if new_num == "080":
               total_calls_to_bangladore += 1
           codes_for_target_receiving_calls[str(new_num)] = None
       # mobile numbers are separated by space, area code only first 4 digits
       elif " " in receiving_num:
           # print(receiving_num[0:4])
           codes_for_target_receiving_calls[str(receiving_num[0:4])] = None
       else:
           pass

# extract keys from dictionary and put in list
code_list = [k for k in codes_for_target_receiving_calls]

# sort the list
code_list.sort()

print("The numbers called by people in Bangalore have codes:")
for pre in code_list:
   print(pre)

percent = round((total_calls_to_bangladore/total_call_from_bangladore) * 100, 2)

print("{} percent of calls from fixed lines in Bangalore are calls to\
other fixed lines in Bangalore.".format(percent))