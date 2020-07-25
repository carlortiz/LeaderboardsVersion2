from player import Player

class Unknown:

    def __init__(self):
        self.players = []
        self.points_leaderboard = []
        self.more_players()
        self.pointss()
        self.experiment()

    def more_players(self):
        while True:
            answer = input("\nWould you like to enter in a player? ")
            if answer == "yes":
                self.players.append(self.get_player())
            elif answer == "done":
                print("As you wish.")
                break
            else:
                break

    def get_player(self):
        while True:
            new_player = Player()
            return new_player

    def pointss(self):
        for player in self.players:
            self.points_leaderboard.append(player.points_per_game)
            self.points_leaderboard.sort(reverse = True)

    def experiment(self):
       print("POINTS LEADERBOARD: ")
       for player in self.players:
           for players_points in self.points_leaderboard:
               if player.points_per_game == players_points:
                   print(player.name + " - " + players_points + " ppg")





