import csv
import os
import time

# Specify the file to write to
output_path = os.path.join('3. Python/employee_data2.csv')
first_name = []
last_name = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'r', newline='') as csvfile:

    # Initialize csv.writer
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader, None)

    new_csv = list()
    new_csv.append(header)
# The Name column should be split into separate First Name and Last Name columns.
    for row in csvreader:
        print(type(row))
        emp_id = row[0]
        full_name = row[1]
        dob = time.strptime(row[2], '%Y-%m-%d')
        ssn = row[3]
        new_ssn = '***-**-'+ssn[-4:]
        state = row[4]
        new_state = us_state_abbrev[state]
        
        first_name = full_name.split(' ')[0]
        last_name = full_name.split(' ')[1]

        new_dob = time.strftime('%d/%m/%Y', dob)

        new_csv.append([emp_id, first_name, last_name, new_dob, new_ssn, new_state])

    #print(new_csv)
# Create list as variables

# Zip lists together
    cleaned_csv = zip("Emp ID", "First Name", "Last Name", "DOB", "SSN", "State")
    print(cleaned_csv)
    
# The DOB data should be re-written into DD/MM/YYYY format.
# Set variable for output file
#output_file = os.path.join("web_final.csv")

#  Open the output file
with open("web_final.csv", "w", newline="") as web_final_file_variable:
    writer_program = csv.writer(web_final_file_variable)

    for line in new_csv:
        writer_program.writerow(line)

    #for date in DOB:
    #    row[4] = row[4].strftime('%d/%m/%y')
    #    writer.writerow(row)
# The SSN data should be re-written such that the first five numbers are hidden from view.
    #for num in SSN: 
    #    revised_num = 0

# The State data should be re-written as simple two-letter abbreviations.
    
    #for abb in State:
    #    pass