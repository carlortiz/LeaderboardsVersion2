from player import Player

class Launcher:

    def __init__(self):
        self.players = []
        self.get_players()

    def new_player(self):
            new_player = Player()
            return new_player

    def get_players(self):
       while True:
               question = "\nWould you like to enter in a player?"
               answer = str(input(question + "(yes/no): ")).lower()
               if answer == 'yes':
                   self.players.append(self.new_player())
               elif answer == 'no':
                   print("\nLEADERBOARDS - ")
                   break
               else:
                   print("Enter yes/no only.")
