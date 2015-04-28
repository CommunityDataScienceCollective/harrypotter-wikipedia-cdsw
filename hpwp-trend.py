from csv import DictReader

# read in the input file and count by day
input_file = open("hp_wiki.csv", 'r')

edits_by_day = {}
for row in DictReader(input_file):
    day_string = row['timestamp'][0:10]

    if day_string in edits_by_day:
        edits_by_day[day_string] = edits_by_day[day_string] + 1
    else:
        edits_by_day[day_string] = 1

input_file.close()

# output the counts by day
output_file = open("hp_edits_by_day.csv", "w")

# write a header
output_file.write("date,edits\n")

# iterate through every day and print out data into the file
for day_string in edits_by_day:
    output_file.write(",".join([day_string, str(edits_by_day[day_string])]) + "\n")

output_file.close()
