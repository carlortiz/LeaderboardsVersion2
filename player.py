class Player:

    def __init__(self):
        self.name = self.get_name()
        self.points_per_game = self.get_points_per_game()
        self.rebounds_per_game = self.get_rebounds_per_game()
        self.assists_per_game = self.get_assists_per_game()
        self.steals_per_game = self.get_steals_per_game()
        self.blocks_per_game = self.get_blocks_per_game()

    def get_name(self):
        name = input("Player Name: ")
        return name

    def get_points_per_game(self):
        while True:
            try:
                points_per_game = float(input("Points Per Game: "))
                if points_per_game >= 0:
                    return str(points_per_game)
                else:
                    print("Enter a number above or equal to 0.")
            except ValueError:
                print("Enter numbers above or equal to 0 only.")

    def get_rebounds_per_game(self):
        while True:
            try:
                rebounds_per_game = float(input("Rebounds Per Game: "))
                if rebounds_per_game >= 0:
                    return str(rebounds_per_game)
                else:
                    print("Enter a number above or equal to 0.")
            except ValueError:
                print("Enter numbers above or equal to 0 only.")

    def get_assists_per_game(self):
        while True:
            try:
                assists_per_game = float(input("Assists Per Game: "))
                if assists_per_game >= 0:
                    return str(assists_per_game)
                else:
                    print("Enter a number above or equal to 0.")
            except ValueError:
                print("Enter numbers above or equal to 0 only.")

    def get_steals_per_game(self):
        while True:
            try:
                steals_per_game = float(input("Steals Per Game: "))
                if steals_per_game >= 0:
                    return str(steals_per_game)
                else:
                    print("Enter a number above or equal to 0.")
            except ValueError:
                print("Enter numbers above or equal to 0 only.")

    def get_blocks_per_game(self):
        while True:
            try:
                blocks_per_game = float(input("Blocks Per Game: "))
                if blocks_per_game >= 0:
                    return str(blocks_per_game)
                else:
                    print("Enter a number above or equal to 0.")
            except ValueError:
                print("Enter numbers above or equal to 0 only.")


