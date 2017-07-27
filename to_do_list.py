'''
to_do_list.py

This script lets you create a list.
It can be a grocery list, a to-do list, 
a reminders list, or really, anything you want.

'''

def showHelp():
    #prints out instructions on how to use the app
    print("This program lets you create a to-do list.")
    print("""
Type 'DONE' when you are finished adding items.
Type 'HELP' to show this menu again.
Type 'SHOW' at any time to see what's currently on the list.
""")

    
def showList():
    print("Here's what's currently on the list:")
    for item in toDoList:
        print(" ",item)
    
def addToList(newItem):
    toDoList.append(newItem)
    print("Added {}. This list now has {} items".format(newItem, len(toDoList)))
    
#empty list
toDoList = []


showHelp()

#infinite loop
while True:
    newItem = input('> ')
    
    #breaks infinite loop
    if newItem == "DONE":
        break
    elif newItem == "HELP":
        showHelp()
        continue
    elif newItem == "SHOW":
        showList()
        continue
    else:
        addToList(newItem)
        
print("Here is your final list:")

for item in toDoList:
    print(" ",item)
