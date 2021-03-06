#! /usr/bin/env python3
import re, pyperclip

 phone_regex = re.compile(r''' 
# 415-555-000, 555-0000, (415) 555-000, 555-0000 ext 12345, ext. 12345, x12345
(
 ((\d\d\d) | (\(\d\d\d\)))?  # area code (optional)
(\s | -)       # first separator
\d\d\d       # first 3 digits
-           # separator
\d\d\d\d     # last 4 digits
(((ext(\.)?\s) | x)        # extension word-part (optional)
 (\d{2, 5}))?               # extension number-part (optional)
)
''', re.VERBOSE)

email_regex = re.compile(r''' 
    # some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+] + # name part
@               # at symbol
[a-zA-Z0-9_.+] + # domain name part
''', re.VERBOSE)

text = pyperclip.paste()

extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_numbers = []
for phone_number in extracted_phone:
    all_phone_numbers.append(phone_number[0])


results = '\n'.join(all_phone_numbers) + '\n' + '\n'.join(extracted_email)
pyperclip.copy(results)



