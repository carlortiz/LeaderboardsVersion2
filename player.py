class Player:

    def __init__(self):
        self.name = self.get_player_name()
        self.points_per_game = self.get_player_points_per_game()
        # self.rebounds_per_game = self.get_player_rebounds_per_game()
        # self.get_player_assists_per_game = self.get_player_assists_per_game()
        # self.get_player_steals_per_game = self.get_player_steals_per_game()
        # self.get_player_blocks_per_game = self.get_player_blocks_per_game()

    def get_player_name(self):
        name = input("Player Name: ")
        return name

    def get_player_points_per_game(self):
        points_per_game = input("Points Per Game: ")
        return points_per_game

    def get_player_rebounds_per_game(self):
        rebounds_per_game = input("Rebounds Per Game: ")
        return rebounds_per_game

    def get_player_assists_per_game(self):
        assists_per_game = input("Assists Per Game: ")
        return assists_per_game

    def get_player_steals_per_game(self):
        steals_per_game = input("Steals Per Game: ")
        return steals_per_game

    def get_player_blocks_per_game(self):
        blocks_per_game = input("Blocks Per Game: ")
        return blocks_per_game


