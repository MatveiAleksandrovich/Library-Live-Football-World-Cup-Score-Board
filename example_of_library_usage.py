from scoreboard import Scoreboard

scoreboard = Scoreboard()

# Empty summary
summary = scoreboard.get_summary()
print("Summary (Empty):")
for match_summary in summary:
    print(match_summary)

scoreboard.start_game("Mexico", "Canada")
scoreboard.update_score(0, 5, 0)

scoreboard.start_game("Spain", "Brazil")
scoreboard.update_score(10, 2, 1)

# Negative scores
try:
    scoreboard.update_score(-1, 3, 1)
except ValueError as e:
    print(f"Error: {str(e)}")

# Invalid match index
try:
    scoreboard.update_score(2, 2, 2)
except IndexError as e:
    print(f"Error: {str(e)}")

scoreboard.start_game("Germany", "France")
scoreboard.update_score(2, 2, 2)

summary = scoreboard.get_summary()
print("\nSummary:")
for match_summary in summary:
    print(match_summary)

# Invalid match index
try:
    scoreboard.finish_game(3)
except IndexError as e:
    print(f"Error: {str(e)}")

scoreboard.finish_game(1)

summary = scoreboard.get_summary()
print("\nUpdated Summary:")
for match_summary in summary:
    print(match_summary)
