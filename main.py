from player import Player
from leaderboard import Leaderboard

class Main:

    def __innit__(self):
        players = []

        print("\nHello. Welcome to the Basketball Leaderboard App.")
        print("This app lets you enter the stats of as many players needed.")
        print("Then, it will rank each player in every major statistical category.")

        self.get_players()
        self.get_leaderboards()

    def new_player(self):
        new_player = Player()
        return new_player

    def get_players(self):
        while True:
            question = "\nWould you like to enter in a player?"
            answer = str(input(question + "(y/n): ")).lower()
            if answer == 'y':
                self.players.append(self.new_player())
            elif answer == 'n':
                print("\nTHE LEADERBOARDS - ")
                break
            else:
                print("Enter y/n only.")

    def new_leaderboard(self):
        new_leaderboard = Leaderboard()
        return new_leaderboard

    def make_leaderboards(self):
        statistic = []

        for player in self.Main.player:



