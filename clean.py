import csv

final_list = []
n = 2

with open('all_paths.csv', newline='') as csvfile:
    all_paths = csv.reader(csvfile)
    for path in all_paths:
        p = path[4]
        new_p = [p[i:i+n] for i in range(0, len(p), n)]
        new_p = new_p[::-1]
        new_p = ''.join(new_p)
        final_list.append([path[0],path[1],path[2],path[3],path[4],new_p,path[5]])
    
    print(final_list)

with open("all_paths_2.csv",'w', newline='') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(final_list)