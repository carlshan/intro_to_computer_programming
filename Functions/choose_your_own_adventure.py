def start_story():
    print("You wake up in a cold, dark room with no recollection as to how you got there.")
    print("As your eyes adjust to the surroundings, you take what's around you.")
    print("Suddenly you hear footsteps approaching the only door in the room.")
    print("Please choose one of the following:")
    print("1. Lie still and pretend to be asleep.")
    print("2. Ready yourself for mortal combat!!!!!!")
    choice = input("Please type 1 or 2")
    if choice == "1":
        pretend_to_sleep()
    elif choice == "2":
        mortal_combat()
    else:
        print("You need to choose 1 or 2")
        choice = input("Please type 1 or 2")


def pretend_to_sleep():
    # your code here
    pass


def mortal_combat():
    # your code here
    pass


start_story()
