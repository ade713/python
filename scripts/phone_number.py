
'''
def is_phone_number(text): #415-554
    if len(text) != 12:
        return False # correct size check
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # area code check
    if text[3] != '-':
        return False # dash check
    if i in range(4, 7):
        if not text[i].isdecimal():
            return False # 1st 3 digits check
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me @ 832-555-6789 tomorrow or 281-555-6789'
found_number = False

for i in range(len(message)):
    chunk = message[i:i + 12]
    if is_phone_number(chunk):
        print("Phone number found: %s" % (chunk))
        found_number = True

if not found_number:
    print('Couldn\'t find any phone numbers...')
'''

import re

message = 'Call me at 713-555-9000 or 718-555-6000'
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.findall(message) # mo -- matching object

# print(mo.group()) #  -- used with .search() to
print(mo) # -- used with .findall()