# Phone&Email.py - Finds Bangladeshi phone numbers and email addresses on the clipboard.

import re, pyperclip

# Create phone number regex.
phoneRegex = re.compile(r'''(           
(\+\d{2}|\d{2}|\+\d{3}|\d{3}|)?              # +88 or +880 dial code for Bangladesh
(\s|)?                                       # space
(\d{4}|\d{5})                                # first 4 or 5 digits
(\s|-|\.|)                                   # separator 
(\d{6})                                      # last 6 digits
(\s*(ext|x|ext.)\s*(\d{4,7}))?               # extension
)''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+                      # username
@                                      # @ symbol
[a-zA-Z0-9.-]+                         # domain name
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    pn = groups[1]
    phoneNum = groups[1] + ' ' + '-'.join([groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No Bangladeshi phone numbers or email addresses found.')

