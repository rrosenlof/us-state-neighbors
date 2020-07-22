import csv
import linkedlistapi

states = []

def main(state1, state2):
    lists = []
    found = False
    border_dict = create_dict()     

    with open('neighbors.csv', newline='') as csvfile:
        neighbors = csv.reader(csvfile, delimiter=',', quotechar='|')
        l_list = linkedlistapi.LinkedList()
        l_list.add(state1)
        while l_list.get(l_list.size-1) != state2:
            for neighbor in neighbors:
                if neighbor[0] == state1 and neighbor[1] == state2:
                    print(neighbor)
                    l_list.add(neighbor[1])
                    break
                else:
                    print('else block')
        l_list.debug_print()
        

        
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


def find(neighbor, state2, neighbors):
    return
        

      

main('Alabama', 'Florida')
    