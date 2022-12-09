import random

class Puzzle:
    # The word that needs to be guessed. 
    
    # The responsibility of Puzzle is to keep track of letters that have
    # been found. 
    
    # Attributes:
    #     _puzzles[]: List of 5 possible puzzles.
    #     _puzzle[]: List of letters in the puzzle
      

    def __init__(self):
        # Constructs a new Puzzle.

        # Args:
        #     self (Puzzle): An instance of Puzzle.
        
        self._puzzles = ["tomahawk", "sherman", "theory", "distance","string"]
        self._word = self._puzzles[random.randint(0, 4)]
        self._new_answers = []
        for i in list(self._word):
            self._new_answers.append("_") 
        self._letter = ""
        

    def pass_letter(self, letter):

        self._letter = letter

    
    def right_answer(self):
        if self._word.find(self._letter) > -1:
            right = "true"
        elif self._word.find(self._letter) == -1:
            right = "false"
        
        return right

    def track_answers(self):
    #     Whether or not the letter has been found in the puzzle.

    #     Args:
    #         self (Puzzle): An instance of Puzzle.
            
    #     Returns:
    #         boolean: True if the letter was found; false if otherwise.
        

        val = -1
        for i in self._new_answers:
            val += 1

            index = self._word.find(self._letter, val)
            
            if index > -1:
                self._new_answers[index] = self._letter

           
        return self._new_answers

        
   

        