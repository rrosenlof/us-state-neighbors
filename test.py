import linkedlistapi
import csv

def l_list():
  l_list = linkedlistapi.LinkedList()
  l_list.debug_print()
  with open('data_example.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      print(row)
      # perform the function in the line
      if row[0] == 'CREATE':
        l_list = linkedlistapi.LinkedList()
      elif row[0] == 'DEBUG':
        l_list.debug_print()
      elif row[0] == 'ADD':
        l_list.add(row[1])
      elif row[0] == 'SET':
        l_list.set(int(row[1]),row[2])
      elif row[0] == 'GET':
        l_list.get(int(row[1]))
      elif row[0] == 'DELETE':
        l_list.delete(int(row[1]))
      elif row[0] == 'INSERT':
        l_list.insert(int(row[1]),row[2])
      elif row[0] =='SWAP':
        l_list.swap(int(row[1]),int(row[2]))
      else:
        raise ValueError(row[0])

l_list()