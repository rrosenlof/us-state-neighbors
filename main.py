import csv

states = []

# with open('borders.csv', newline='') as csvfile:
#     borders = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in borders:
#         # print(', '.join(row))
#         print(row[2])
#         for border in row[2].split('/'):
#             states.append([row[1],border])

# with open('all_borders.csv', 'w', newline='') as csvfile:
#     border_writer = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     border_writer.writerows(states)




def main():
    border_paths = []

    border_dict = create_dict()     

    with open('borders.csv', newline='') as csvfile:
        borders = csv.reader(csvfile, delimiter=',', quotechar='|')
        borders = list(borders)
        i = 0
        while i < len(borders):
            j = 0
            while j < len(borders):
                # print(borders[i][1], borders[j][1])

                state1 = borders[i][1]
                state2 = borders[j][1]
                dist = 0

                if state1 == state2:
                    border_paths.append([state1,state2,dist])
                else:
                    for obj in find_borders(state1,state2,border_dict):
                        print(obj)
                        border_paths.append(obj)
                    # border_paths.append(res)
                j += 1
            i += 1
        
    # print(border_paths)

def create_dict():
    with open('borders.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        with open('all_borders_dict.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[1]:rows[2] for rows in reader}
            return mydict

def find_borders(state1, state2, border_dict, dist=1,index=0):
    print('...................')
    print('state1: {}'.format(state1))
    print('index: {}'.format(index))
    for border in border_dict[state1].split('/'):
        print(border)
        if border == state2:
            yield ([state1, state2, dist])
    yield from find_borders(border_dict[state1].split('/')[index],state2,border_dict,dist+1,index+1)
      

main()
    