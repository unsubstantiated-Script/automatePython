import re, pyperclip

# Create a regex for phone numbers
phone_regex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))? # area code (optional)
(\s|-) # first separator
\d\d\d # first 3 digits
- # second separator
\d\d\d\d # last 4 digits
(((ext(\.)?\s)|x) # extension word-part (optional)
 (\d{2,5}}))? # extension number-part (optional)
 )
''', re.VERBOSE)
# Create a regex for emails
email_regex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@ # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)
# Get the text off the clipboard
text = pyperclip.paste()
# Extract the phone numbers and emails from the text
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_numbers = []
for phone_number in extracted_phone:
    all_phone_numbers.append(phone_number[0])

# Copy the extracted phone numbers and emails to the clipboard
results = '\n'.join(all_phone_numbers) + '\n' + '\n'.join(extracted_email)
pyperclip.copy(results)
