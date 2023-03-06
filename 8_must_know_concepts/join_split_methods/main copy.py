'''Project: A file containing 500 phone numbers is given. 
Read all the phone numbers from that file, split the country
codes from the phone numbers and put them inside a bracket,
spilt the country code and phone numbers with hyphen(-) 
and save these phone numbers in a separate file.

for example:
convert phone_num = 918888888888  into phone_num = (91)-8888888888
'''

import os

current_path = os.getcwd()
ph_num_filepath = os.path.join(
    os.sep, current_path, 'tmp', 'phone_numbers.txt')
new_file_path = os.path.join(
    os.sep, current_path, 'tmp', 'phone_number_amended.txt')


with open(ph_num_filepath, 'r') as f:
    ph_nums = f.readlines()
    for ph_num in ph_nums:
        ph_num = ph_num.splitlines()[0]
        country_code, ph_num = (ph_num[:2], ph_num[2:])
        country_code = f"({country_code})"
        amended_ph_num = '-'.join((country_code, ph_num))
        with open(new_file_path, 'a') as f:
            f.write(f"{amended_ph_num}\n")
