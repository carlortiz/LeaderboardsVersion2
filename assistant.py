class Assistant:

    def __init__(self):
        self.greet_user()
        self.explain_rules()

    def greet_user(self):
        print("Hello. Welcome to the NBA/NBA2K Leaderboard App.")
        print("This app lets you enter the stats of as many players desired.")
        print("Then, it will rank each player in every major statistical category.")

    def explain_rules(self):
        print("\nOnly 'yes', 'done', or 'quit' will be accepted as answers.")
        print("Enter 'done' when you have entered all players.")
        print("Enter 'quit' when finished.")
