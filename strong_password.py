#! /usr/bin/env python3

import re

def strong_password_detection(password):
    password_regex = re.compile(r'''
        (
            (\w){8,}
            ([A-Z])+
            ([a-z])+
            (\d)+
        )
    ''',re.VERBOSE)

    strong_password = password_regex.findall(password)

    if strong_password:
        return True
    else:
        return False


your_password = input()

if strong_password_detection(your_password):
    print('Your password is valid! You may login')
else:
    print('Your password does not meet the requirements... Try again')