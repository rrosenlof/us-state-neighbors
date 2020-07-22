import csv

all_paths = []

with open('paths.csv', newline='') as csvfile:
    neighbors = csv.reader(csvfile, delimiter=',', quotechar='|')
    neighbors = list(neighbors)
    for n in neighbors:
        all_paths.append([n[0],n[1],n[2],n[3],n[4],n[6]])
        all_paths.append([n[2],n[3],n[0],n[1],n[5],n[6]])
    print(len(all_paths))

with open("all_paths.csv", 'w', newline='') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(all_paths)

    