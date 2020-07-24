from player import Player

class Unknown:

    def __init__(self):
        self.get_players()

    def get_players(self):
            while True:
                answer = input("\nWould you like to enter in a player? ")
                if answer == "yes":
                    new_player = Player()
                    return new_player
                elif answer == "done":
                    print("As you wish.")
                    break
                else:
                    break


