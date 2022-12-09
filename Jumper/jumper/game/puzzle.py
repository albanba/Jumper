import random

class Puzzle:

    """The secret word representing every letter as a dash. 
    
    The puzzle picks a random word form the available words in the list,
    evaluates the asnwers as right or wrong and records the correct ones. 
    
    Attributes:
        _puzzles (list) <str>: contains 5 possible secret words
        _word <str>: contains 1 random pick from the possible secret words
        _new_answers (list): same amount of letters as the _word but in dashes 
        _letter <str>: the letter received from the user
    """
      

    def __init__(self):
        
        """Constructs the initial puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        
        self._puzzles = ["tomahawk", "sherman", "theory", "distance","string"]
        self._word = self._puzzles[random.randint(0, 4)]
        self._new_answers = []
        for i in list(self._word):
            self._new_answers.append("_") 
        self._letter = ""
        

    def set_letter(self, letter):
        """receives the letter (guess) and stores it.

        Args:
            self (Puzzle): An instance of Puzzle.
            letter: input from user
        """
        self._letter = letter

    
    def right_answer(self):
        """evaluates if the letter fits in the puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
            self._letter: the upodated letter 
        """


        if self._word.find(self._letter) > -1:
            right = "true"
        elif self._word.find(self._letter) == -1:
            right = "false"
        
        return right

    def track_answers(self):
        """adds to the answer the letters that match the puzle

        Args:
            self (Puzzle): An instance of Puzzle.
            self._new_answers: input from user
        """
        

        val = -1
        for i in self._new_answers:
            val += 1

            index = self._word.find(self._letter, val)
            
            if index > -1:
                self._new_answers[index] = self._letter

           
        return self._new_answers

        
   

        