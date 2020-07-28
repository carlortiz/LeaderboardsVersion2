class Player:

    def __init__(self):
        self.name = input("Player Name: ")
        self.points_per_game = self.ask("Points Per Game: ")
        self.rebounds_per_game = self.ask("Rebounds Per Game: ")
        self.assists_per_game = self.ask("Assists Per Game: ")
        self.steals_per_game = self.ask("Steals Per Game: ")
        self.blocks_per_game = self.ask("Blocks Per Game: ")

    def ask(self, question):
        while True:
            try:
                value = float(input(question))
                if value >= 0:
                    return str(value)
                else:
                    print("Enter a number above or equal to 0.")
            except ValueError:
                print("Enter numbers above or equal to 0 only.")

