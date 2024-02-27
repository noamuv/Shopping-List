#Quick introduction
print("Welcome to the Shopping List App!")
 
#Create a function that will loop the shopping_list app
def shopping_list():
    user_input = int(input("Press 1 for a new list or press 2 to see previous lists\r\n"))

#1st condition, user_input is 1 -> create a new list                                                                                                                                                          
    if user_input == 1:
        new_list = []
        user_item = ""

        while user_item != "exit": 
            user_item = input("What would you like to add to the list? (To end the list, type in 'exit')\r\n")
            new_list.append(user_item)
        new_list.pop()
        print(new_list)
        f = open("shopping_list.txt", "a")
        f.writelines(new_list)
        f.close()

#2nd condition, user_input is 1 -> read last line of the txt file (aka last shopping list)
    elif user_input == 2:
        with open("shopping_list.txt", "r") as file:
            for line in file:
                pass
            last_line = line
        print(last_line)

#Condition set to make sure input was 1 or 2 and nothing else
    elif user_input != 1 or user_input != 2:
        return user_input

while True:
    shopping_list()
