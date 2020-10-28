class Card():

    SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King", "Ace")

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank. Your value is '{rank}'. Rank must be one of the following {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Your value is '{suit}'. It must be one of the following {self.SUITS}")
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"


