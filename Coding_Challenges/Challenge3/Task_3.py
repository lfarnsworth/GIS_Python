"""
# 3. Working with CSV
#
# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements at Mauna Loa, Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# Using Python (csv) calculate the following:
#
# Annual average for each year in the dataset.
# Minimum, maximum and average for the entire dataset.
# Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November) and Winter (December, January, February).
# Calculate the anomaly for each value in the dataset relative to the mean for the entire timeseries."""

import csv
# create empty lists for calculations:
stored_co2_levels = []
year_list = []
month_list = []


# open CO2 dataset and read the CSV by using the "," as a delimiter:
with open("co2-ppm-daily.csv") as co2_dataset:
    csv_reader = csv.reader(co2_dataset, delimiter=',')
    line_count = 0
    next(co2_dataset) # skips the header row

    # Use for loop to split the data into three lists: year, month and day
    for row in csv_reader:
        year, month, day = row[0].split("-")
        if year not in year_list:
            year_list.append(year)
            if month not in month_list:
                month_list.append(month)
# Put the data into lists
            stored_co2_levels.append(float(row[1]))
            line_count = line_count + 1
# Print your results!
print("Minimum co2 in dataset = " + str(min(stored_co2_levels)))
print("Maximum co2 in dataset = " + str(max(stored_co2_levels)))
print("Average co2 in dataset = " + str(sum(stored_co2_levels) / len(stored_co2_levels)))

# Create a dictionary to calculate the average for each year in the dataset:
year_dict = {}
for year in year_list:
    co2_years = []
    with open("co2-ppm-daily.csv") as co2_dataset:
        csv_reader = csv.reader(co2_dataset, delimiter=',')
        next(co2_dataset)
        for row in csv_reader:
            year_co2, month_co2, day = row[0].split("-")
            if year_co2 == year:
                co2_years.append(float(row[1]))
# populate the dictionary with averages for each year:
    year_dict[year] = str(sum(co2_years) / len(co2_years))
print("Here are the averages of co2 by year: " + str(year_dict))

# Next, find seasonal averages of the dataset:
# Create empty seasonal lists:

spring = []
summer = []
fall = []
winter = []

with open("co2-ppm-daily.csv") as co2_dataset:
    csv_reader = csv.reader(co2_dataset, delimiter=',')
    next(co2_dataset)

# Use for loop to split the data into separate months
    for row in csv_reader:
        year, month, day = row[0].split("-")
        if month == "03" or month == "04" or month == "05":
            spring.append(float(row[1]))
        if month == "06" or month == "07" or month == "08":
            summer.append(float(row[1]))
        if month == "09" or month == "10" or month == "11":
            fall.append(float(row[1]))
        if month == "12" or month == "01" or month == "02":
            winter.append(float(row[1]))
            
# Print all seasonal averages:
print("Spring Average CO2 = " + str(sum(spring) / len(spring)) + " ppm")
print("Summer Average CO2 = " + str(sum(summer) / len(summer)) + " ppm")
print("Fall Average CO2 = " + str(sum(fall) / len(fall)) + " ppm")
print("Winter Average CO2 = " + str(sum(winter) / len(winter)) + " ppm")

# Now, calculate the anomalies relative to the mean in the entire dataset:
# Create an empty dictionary to store anomalies:
overall_average = sum(stored_co2_levels) / len(stored_co2_levels)
anomaly_dict = {}
# Once again open the CSV and split it by the delimiter.
# Then, split the data into year, month and day,
# Populate anomaly dictionary with data:
with open("co2-ppm-daily.csv") as co2_dataset:
    csv_reader = csv.reader(co2_dataset, delimiter=',')
    next(co2_dataset)
    for row in csv_reader:
        year, month, day = row[0].split("-")
        anomaly_dict[year] = float(row[1]) - overall_average

print("Here are the anomalies of co2 by year: " + str(anomaly_dict))

