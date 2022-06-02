class Winner:
    def __init__(self):
        self.points = 0
        self.name = ""

    def set_points(self, points_count):
        self.points = points_count

    def set_name(self, winner_name):
        self.name = winner_name

    def get_points(self):
        return self.points

    def get_name(self):
        return self.name

class Tournament:
    def run(self, competitions, results):
        if len(competitions) != len(results):
            raise ValueError("competitions array and results array have to have the same length")
        teams = {}
        winner = Winner()
        for idx in range(0, len(competitions)):
            home_team = competitions[idx][0]
            away_team = competitions[idx][1]
            if home_team not in teams:
                teams[home_team] = 0
            if away_team not in teams:
                teams[away_team] = 0

            if results[idx] == 1:
                teams[home_team] += 3
                if teams[home_team] > winner.get_points():
                    if home_team != winner.get_name:
                        winner.set_name(home_team)
                    winner.set_points(teams[home_team])
            elif results[idx] == 0:
                teams[away_team] += 3
                if teams[away_team] > winner.get_points():
                    if away_team != winner.get_name():
                        winner.set_name(away_team)
                    winner.set_points(teams[away_team])

        return winner
