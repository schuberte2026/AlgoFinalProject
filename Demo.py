from SkipList import SkipList, Node

def setup_skiplist():
    """
    Sets up a skip list with given nodes of given levels (so we can have a consistent skip list to test on)

    Returns:
    (SkipList): A skip list with nodes of given levels
    """
    skiplist = SkipList(max_levels=5)
    skiplist.levels = 5
    current_node = skiplist.head

    node_values = [1, 5, 12, 14, 22, 23, 24, 26, 28, 30, 50]
    node_levels = [4, 1, 2, 3, 1, 5, 1, 2, 1, 3, 5]

    for node_value, node_level in zip(node_values, node_levels):
        new_node = Node(node_value, node_level)    
        for i in range(min(len(current_node.next), node_level)):
            current_node.next[i] = new_node
        current_node = current_node.next[0]

    return skiplist

def get_action_choice():
    """
    Prompts the user to enter a choice of action to perform on the skip list (insert, delete, or search)

    Returns:
    (str): The user's choice of action to perform on the skip list (1 for insert, 2 for delete, 3 for search)
    """
    valid_choice = False
    while not valid_choice:
        action_choice = input("Hit 1 to insert a number, 2 to delete a number, or 3 to search for a number in a skip list: ")
        if action_choice in ['1', '2', '3']:
            valid_choice = True
        else:
            print("Invalid input. Please try again.")
    return action_choice

def get_element_to_perform_action_on(action):
    """
    Prompts the user to enter an integer to perform an action on (insert, delete, or search for) in the skip list

    Parameters:
    action (str): The action to perform on the skip list (insert, delete, or search for)

    Returns:
    (int): The integer the user entered to perform the action on
    """
    valid_element = False
    while not valid_element:
        element = input(f"Enter the integer you would like to {action}: ")
        if element.isnumeric():
            element = int(element)
            valid_element = True
        else:
            print("Invalid input. Please enter a integer.")
    
    return element

def perform_insert(skiplist):
    """
    Performs insertion operation on skiplist. Asks user for an integer to insert into the skip list, then displays the skip list before
    and after the insertion operation is performed (if successful, otherwise lets user know the element could not be added to the skip list)
    """
    element = get_element_to_perform_action_on("insert")
    print("Before:")
    skiplist.display()
    print()
    insert_successful = skiplist.insert(element)
    if insert_successful:
        print("After: ")
        skiplist.display()
    else:
        print(f"The element {element} could not be added to the skip list.")

def perform_delete(skiplist):
    """
    Performs deletion operation on skiplist. Asks user for an integer to delete from the skip list, then displays the skip list before
    and after the deletion operation is performed (if successful, otherwise lets user know the element could not be removed from the skip list)
    """
    element = get_element_to_perform_action_on("delete")
    print("Before:")
    skiplist.display()
    print()
    remove_successful = skiplist.remove(element)
    if remove_successful:
        print("After: ")
        skiplist.display()
    else:
        print(f"The element {element} could not be removed from the skip list.")

def perform_search(skiplist):
    """
    Performs search operation on skiplist. Asks user for an integer to search for in the skip list, then displays whether the skip list
    contains the element or not
    """
    element = get_element_to_perform_action_on("search for")
    contains_element = skiplist.contains(element)
    if contains_element:
        print(f"The skip list contains the element {element}.")
    else:
        print(f"The skip list does not contain the element {element}.")

def perform_action_on_skiplist():
    """
    Prompts the user to perform an action on a skip list (insert, delete, or search for an element) and prompts the user to enter an integer
    to perform this action with, then displays the skip list before and after the action is performed
    """
    quit = False
    while not quit:
        skiplist = setup_skiplist()
        print("Here is your skip list: ")
        skiplist.display()
        print()

        action_choice = get_action_choice()

        if action_choice == '1':
            perform_insert(skiplist)
        elif action_choice == '2':
            perform_delete(skiplist)
        elif action_choice == '3':
            perform_search(skiplist)

        quit_choice = input("\nEnter 'q' to quit or any other key to perform another action on a reset version of the skip list: ")
        if quit_choice == 'q':
            quit = True

perform_action_on_skiplist()