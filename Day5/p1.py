import re

text = """Blanking: 150 ms
Medtronic CareLink Network LNQ11 Serial Number: RLA348895S 31-Mar-2023 20:07:32 Copyright © 2001-2023 Medtronic, Inc. 
Confidential Patient Information4 /
5Summary Report"""

def parse_text_with_regex_and_get_first_match_data(regex, text):
    data = {}
    match = re.search(regex, text, re.I)
    if match:
        data = match.groupdict()
    return data

regex = (
    r"Medtronic CareLink Network\s?LNQ\d{2}\sSerial\sNumber\:\s?[\w\d]{10}"
    r"\s?(?P<creation_date>\d{1,2}\-\w{3}\-\d{4}\s\d{2}\:\d{2}\:\d{2})\s?Copyright"
)



data = parse_text_with_regex_and_get_first_match_data(regex, text)

print(data)

exp = "31-Mar-2023 20:07:32"