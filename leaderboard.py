class Leaderboard:

    def __init__(self, aTitle, aStats, aNames):
        title = aTitle
        stats = aStats
        names = aNames

        self.leaderboard = self.create_leaderboard(stats)
        self.display_leaderboard()

    def create_leaderboard(self, stats):
        stats.sort(reverse = True)
        return stats

    def display_leaderboard(self):
        print("POINTS LEADERBOARD: ")
        for player in self.program.players:
            for points_per_game in self.points_leaderboard:
                if player.points_per_game == points_per_game:
                    print(player.name + " - " + points_per_game + " ppg")
                    break