#! /usr/bin/env python3

import webbrowser, sys, pyperclip

sys.argv # collects args passed in

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# Open map of address in google maps
webbrowser.open('https://www.google.com/maps/place/' + address)
