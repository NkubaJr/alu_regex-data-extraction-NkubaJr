import re

# Read the sample text from the file
with open('test_samples.txt', 'r', encoding='utf-8') as file:
        text = file.read()
# === Regex Patterns ===
# 1. Emails
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# 2. Rwandan Francs Currency (e.g., 75,000 Rwf)
currency_pattern = r'\d{1,3}(?:,\d{3})*\sRwf'

# 3. Both 12-hour and 24-hour time formats
time_pattern = r'\b(?:' \
               r'(?:0?[1-9]|1[0-2]):[0-5]\d\s?[APap][Mm]' \
               r'|' \
               r'(?:[01]?\d|2[0-3]):[0-5]\d' \
               r')\b'

# 4. Hashtags
hashtag_pattern = r'#\w+'
# === Extraction ===

emails = re.findall(email_pattern,text) 
currencies = re.findall(currency_pattern, text)
times = re.findall(time_pattern, text)
hashtags = re.findall(hashtag_pattern, text)

# === Output Results ===
print("Emails found:", emails)
print("Currency amounts found:", currencies)
print("Time values found:", times)
print("Hashtags found:", hashtags)

