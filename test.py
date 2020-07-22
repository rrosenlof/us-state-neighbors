import csv

with open('borders.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    with open('all_borders_dict.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[1]:rows[2] for rows in reader}

        print(mydict)