from launcher import Launcher

points = []
rebounds = []
assists = []
steals = []
blocks = []

class Displayer:

    def __init__(self):
        self.program = Launcher()

        self.points_leaderboard = self.create_points_leaderboard()
        self.display_points_leaderboard()

        self.rebounds_leaderboard = self.create_rebounds_leaderboard()
        self.display_rebounds_leaderboard()

        self.assists_leaderboard = self.create_assists_leaderboard()
        self.display_assists_leaderboard()

        self.steals_leaderboard = self.create_steals_leaderboard()
        self.display_steals_leaderboard()

        self.blocks_leaderboard = self.create_blocks_leaderboard()
        self.display_blocks_leaderboard()

    def create_points_leaderboard(self):
        for player in self.program.players:
            points.append(player.points_per_game)
        points.sort(reverse = True)
        return points

    def display_points_leaderboard(self):
        print("POINTS LEADERBOARD: ")
        for player in self.program.players:
            for points_per_game in self.points_leaderboard:
                if player.points_per_game == points_per_game:
                    print(player.name + " - " + points_per_game + " ppg")
                    break

    def create_rebounds_leaderboard(self):
        for player in self.program.players:
            rebounds.append(player.rebounds_per_game)
        rebounds.sort(reverse = True)
        return rebounds

    def display_rebounds_leaderboard(self):
        print("\nREBOUNDS LEADERBOARD: ")
        for player in self.program.players:
            for rebounds_per_game in self.rebounds_leaderboard:
                if player.rebounds_per_game == rebounds_per_game:
                    print(player.name + " - " + rebounds_per_game + " rpg")
                    break

    def create_assists_leaderboard(self):
        for player in self.program.players:
            assists.append(player.assists_per_game)
        assists.sort(reverse = True)
        return assists

    def display_assists_leaderboard(self):
        print("\nASSISTS LEADERBOARD: ")
        for player in self.program.players:
            for assists_per_game in self.assists_leaderboard:
                if player.assists_per_game == assists_per_game:
                    print(player.name + " - " + assists_per_game + " apg")
                    break

    def create_steals_leaderboard(self):
        for player in self.program.players:
            steals.append(player.steals_per_game)
        steals.sort(reverse = True)
        return steals

    def display_steals_leaderboard(self):
        print("\nSTEALS LEADERBOARD: ")
        for player in self.program.players:
            for steals_per_game in self.steals_leaderboard:
                if player.steals_per_game == steals_per_game:
                    print(player.name + " - " + steals_per_game + " spg")
                    break

    def create_blocks_leaderboard(self):
        for player in self.program.players:
            blocks.append(player.blocks_per_game)
        blocks.sort(reverse = True)
        return blocks

    def display_blocks_leaderboard(self):
        print("\nBLOCKS LEADERBOARD: ")
        for player in self.program.players:
            for blocks_per_game in self.blocks_leaderboard:
                if player.blocks_per_game == blocks_per_game:
                    print(player.name + " - " + blocks_per_game + " bpg")
                    break




