import json
import random

templates = [
    "Those {team1} are on fire with a {streak}-game roll. Watch out {team2}!",
    "Who cares if the {team2} have won {wins} games? The red hot {team1} are rolling up the wins with {streak} in a row."
]

def write_message():
    with open('stats.json') as json_data:
        stats = json.load(json_data)
        best_streak, most_wins = stats["best_streak"], stats["most_wins"]
        text = random.choice(templates).format(
            team1 = best_streak["name"],
            streak = best_streak["streak"],
            team2 = most_wins["name"],
            wins = most_wins["wins"]
        )
        return text

if __name__ == '__main__':
    print(write_message())