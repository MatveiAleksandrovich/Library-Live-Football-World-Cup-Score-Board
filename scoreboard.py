class Match:
    def __init__(self, home_team, away_team):
        """
        Represents a match between two teams.

        Args:
            home_team (str): Name of the home team.
            away_team (str): Name of the away team.
        """
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0


class Scoreboard:
    def __init__(self):
        """
        Represents a scoreboard for ongoing football matches.
        """
        self.matches = []

    def start_game(self, home_team, away_team):
        """
        Starts a new football match and adds it to the scoreboard.

        Args:
            home_team (str): Name of the home team.
            away_team (str): Name of the away team.
        """
        match = Match(home_team, away_team)
        self.matches.append(match)

    def update_score(self, home_score, away_score, match_index):
        """
        Updates the score of a football match.

        Args:
            home_score (int): New score for the home team.
            away_score (int): New score for the away team.
            match_index (int): Index of the match to update.

        Raises:
            IndexError: If the match index is invalid.
            ValueError: If the provided scores are negative.
        """
        self.validate_match_index(match_index)
        if home_score < 0 or away_score < 0:
            raise ValueError("Scores cannot be negative")
        match = self.matches[match_index]
        match.home_score = home_score
        match.away_score = away_score

    def finish_game(self, match_index):
        """
        Finishes a football match and removes it from the scoreboard.

        Args:
            match_index (int): Index of the match to finish.

        Raises:
            IndexError: If the match index is invalid.
        """
        if match_index < 0 or match_index >= len(self.matches):
            raise IndexError("Invalid match index")
        del self.matches[match_index]

    def get_summary(self):
        """
        Retrieves a summary of ongoing football matches in the scoreboard.

        Returns:
            list: A list of strings representing the match summaries.
        """
        sorted_matches = sorted(self.matches, key=lambda x: (x.home_score + x.away_score, -len(self.matches)))
        summary = []
        for match in reversed(sorted_matches):
            summary.append(f"{match.home_team} {match.home_score} - {match.away_score} {match.away_team}")
        return summary

    def validate_match_index(self, match_index):
        """
        Validates the match index.

        Args:
            match_index (int): Index of the match to validate.

        Raises:
            IndexError: If the match index is invalid.
        """
        if match_index < 0 or match_index >= len(self.matches):
            raise IndexError("Invalid match index")
