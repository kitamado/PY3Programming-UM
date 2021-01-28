VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    """a Wheel of Fortune player"""
    def __init__(self, nm):
        self.name = nm # The name of the player 
        self.prizeMoney = 0 # The amount of prize money for this player
        self.prizes = [] # The prizes this player has won so far


    def addMoney(self, amt):
        self.prizeMoney = self.prizeMoney + amt

    def goBankrupt(self):
        self.prizeMoney = 0


    def addPrize(self, prize):
        self.prizes.append(prize)


    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
    
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obsuredPhrase, guessed):
        prompt = """{name} has ${prizeMoney}

        Category: {category}
        Phrase:  {obscured_phrase}
        Guessed: {guessed}

        Guess a letter, phrase, or type 'exit' or 'pass':""".format(self.name, self.prizeMoney, category, obsuredPhrase, guessed)
        move = input(prompt)
        return move

    
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, nm, df):
        WOFPlayer.__init__(self, nm)
        self.difficulty = df


    def smartCoinFlip(self):
        random_num = random.randint(1, 10)
        if random_num > self.difficulty:
            return True
        else:
            return False


    def getPossibleLetters(self, guessed):
        posb_lst = []
        
        if self.prizeMoney < VOWEL_COST:
            for l in LETTERS:
                if l not in guessed and l not in 'AEIOU':
                    posb_lst.append(l)
        else:
            for l in LETTERS:
                if l not in guessed:
                    posb_lst.append(l)
        return posb_lst


    def getMove(self, category, obsuredPhrase, guessed):
        possible_chars = []
        if self.prizeMoney < VOWEL_COST:
            for l in LETTERS:
                if l not in guessed and l not in 'AEIOU':
                    possible_chars.append(l)
        else:
            for l in LETTERS:
                if l not in guessed:
                    possible_chars.append(l)
        if possible_chars == []:
            return 'pass'
        
        if self.smartCoinFlip() == True:
            for idx in range(26):
                guess_x = self.SORTED_FREQUENCIES[-idx-1]
                if guess_x in possible_chars:
                    return guess_x
        else:
            guess_x = random.choice(possible_chars)
            return guess_x


