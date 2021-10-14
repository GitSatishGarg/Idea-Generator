import random

while(0==0):
    genres = [
        "Adventure",
        "Epic",
        "Fable",
        "Fairy tale",
        "Fantasy",
        "Folk tale",
        "Historical fiction",
        "Horror",
        "Humour",
        "Legend",
        "Mystery",
        "Myth",
        "Poetry",
        "Realistic fiction",
        "Science fiction"
    ]

    time= [
        "Past",
        "Present",
        "Future",
        "The beggining of the world",
        "The end of the world",
        "outside time"
    ]

    setting = [
        "simple neibhourhood"
        "a planet other than Earth",
        "the Moon",
        "space",
        "the bottom of the ocean",
        "the Sky",
        "the core of the Earth",
        "inside a black hole",
        "a volcano"
    ]

    house = [
        "a castle",
        "a house",
        "a spaceship",
        "an abandoned house",
        "stomach of a monster",
        "a boat"
    ]

    players = [
        "children",
        "magical beings",
        "elves",
        "dwarves",
        "trolls",
        "gods",
        "aliens",
        "creators of the universe",
        "wizards / witches",
        "minions",
        "time travelling humans",
        "ghosts"
    ]

    goal = [
        "make peace",
        "destroy peace",
        "destroy the world",
        "save the world",
        "destroy the universe",
        "save the universe",
        "give everyone powers",
        "give wisdom",
        "create a god",
        "become gods or the kings of gods",
        "unite the universe",
        "customize the universe",
        "turn things into ridiculous things"
    ]

    choice = input("Do you want an idea? Y for Yes or N for No and E to quit: ")
    if(choice=="Y" or choice=="y"):
        print("Idea! The genre is", random.choice(genres),". Where the time is in", random.choice(time), ". Where the setting is in", random.choice(setting), "where the house is", random.choice(house), ". Where the main people are a group of", random.choice(players), ". Where the main goal is to", random.choice(goal),".")
        print("")

    if(choice == "E" or choice == "e"):
        "Sayonaraaa!"
        break

    if(choice == "N" or choice == "n"):
        print("All right!")
        print("")