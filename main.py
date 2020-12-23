# Leaderboards Version 2
players = []

class Player:

    def __init__(self):
        self.name = input("Player Name: ")
        self.points = self.get_averages("Points Per Game: ")
        self.rebounds = self.get_averages("Rebounds Per Game: ")
        self.assists = self.get_averages("Assists Per Game: ")
        self.steals = self.get_averages("Steals Per Game: ")
        self.blocks = self.get_averages("Blocks Per Game: ")
        self.field_goal = self.get_averages("Field Goal Percentage: ")
        self.three_point = self.get_averages("Three Point Percentage: ")
        self.free_throw = self.get_averages("Free Throw Percentage: ")

        # Adds player instance to list of players
        players.append(self)

    def get_averages(self, question):
        while True:
            value = float(input(question))
            if value >= 0:
                return str(value)
            else:
                print("Enter numbers above or equal to 0 only.")

class Leaderboard:

    def __init__(self, category, abbreviation):
        self.category = category
        self.abbreviation = abbreviation

        self.data = self.get_data(self.category)
        self.data = sorted(self.data, key=lambda x: x[self.category], reverse=True)

        self.display()

    def get_data(self, category):
        data = []

        for player in players:
            data.append({'name': player.name, category: getattr(player, category)})
        return data

    def display(self):
        print("\n%s LEADERBOARD: " % (self.category.upper()))
        for element in self.data:
            position = self.data.index(element) + 1
            name = element['name']
            average = element[self.category]
            print("{}. {} - {} {}".format(position, name, average, self.abbreviation))


while True:
    question = "\nWould you like to enter in a player?"
    answer = str(input(question + "(yes/no): ")).lower()
    if answer == "yes":
        player = Player()
    elif answer == "no":
        break;
    else:
        print("Enter yes/no only.")

points = Leaderboard("points", "PPG")
rebounds = Leaderboard("rebounds", "RPG")
assists = Leaderboard("assists", "APG")
steals = Leaderboard("steals", "SPG")
blocks = Leaderboard("blocks", "BPG")
field_goal = Leaderboard("field_goal", "FG%")
three_point = Leaderboard("three_point", "3P%")
free_throw = Leaderboard("free_throw", "FT%")