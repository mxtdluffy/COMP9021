# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly_csv.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a year or a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx -- xxxx (with any number of spaces,
#   possibly none, around --) and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the first year can be posterior to the first year.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by Di Peng and Eric Martin for COMP9021


import sys
import os
import csv
import re
import statistics

def switchMonthtoNumber(month):
    months = {
        'January' : '01',
        'Fabruary' : '02',
        'March' : '03',
        'April' : '04',
        'May' : '05',
        'June' : '06',
        'July' : '07',
        'August' : '08',
        'September' : '09',
        'October' : '10',
        'November' : '11',
        'December' : '12'
    }
    return months.get(month)

def splitYears(yearString):
    years_pattern = re.compile(r'\s*--\s*')
    years = years_pattern.split(year_or_range_of_years)
    if years[0] > years[-1]:
        switch = years[-1]
        years[-1] = years[0]
        years[0] = switch
    return years

filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
month = input('Enter a month: ')
average = 0
years_above_average = []

# REPLACE THIS COMMENT WITH YOUR CODE
temperature_data = {}
years_and_month_list = []
years = splitYears(year_or_range_of_years)
with open(filename) as temperature_file:
    temperature_file_csv = csv.reader(temperature_file)
    headers = next(temperature_file_csv)
    for line in temperature_file_csv:
        if source in line[0]:
            temperature_data.setdefault(line[1], line[2])

try:
    for i in range(int(years[0]), int(years[-1]) + 1):
        key = str(i) + '-' + switchMonthtoNumber(month) + '-06'
        years_and_month_list.append(float(temperature_data.get(key)))

    average = statistics.mean(years_and_month_list)

    for i in range(int(years[0]), int(years[-1]) + 1):
        key = str(i) + '-' + switchMonthtoNumber(month) + '-06'
        if float(temperature_data.get(key)) > average:
            years_above_average.append(i)
except:
    average = 0
    years_above_average = []
    
print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
