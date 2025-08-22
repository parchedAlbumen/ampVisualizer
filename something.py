from helpers.utility import Utility

# Utility.removeSongs()
# print("Removed all the songs")
options = "(1)Add a song\n(2)Remove all the songs\n(else)list all songs"
choice = int(input("What would you like to do: "))

match choice:
    case 1:
        #add a song
        print("add a song")
        Utility.addSongFiles()
    case 2:
        Utility.removeSongs()
        print("removed songs successfully!")
    case _:
        print("basically anything else")
        #everything else basically 

