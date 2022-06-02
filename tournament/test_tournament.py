import unittest
import tournament

class TestTournament(unittest.TestCase):
    def test_run(self):
        my_tournament = tournament.Tournament()
        my_example_competitions = [
            ["HTML","C#"],
            ["C#","Python"],
            ["Python","HTML"],
        ]
        my_example_results = [0,1,1]
        result = my_tournament.run(my_example_competitions, my_example_results)
        print(result.get_name())
        print(result.get_points())

if __name__ == "__main__":
    unittest.main()
