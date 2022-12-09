from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (Puzzle): The game's puzzle.
        is_playing (boolean): Whether or not to keep playing.
        jumper (Jumperer): The game's jumper.
        terminal_service: For getting and displaying information on the terminal.
        _answers: list of ansers registerd

    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal_service = TerminalService()
        self._jumper = Jumper()
        self._puzzle = Puzzle()
        self._is_playing = True
        self._answers = []
        
        
    def start_game(self):
        """Starts the game by running the main game loop.
            Notifies if the game is over and if won or lost. 
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal_service.write_text(self._puzzle._new_answers)
        self._terminal_service.write_jumper(self._jumper._jumper_tracker)
        
      
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            
            if list(self._puzzle._word) == self._answers:
                self._is_playing = False
                print ("\nCongratulations, you win!")
            elif len(self._jumper._jumper_tracker) == 5:
                self._is_playing = False
                print (f"\nOooops, you lost! The word is: {self._puzzle._word} ")
        

    def _get_inputs(self):
        """Ask for a letter and stores it.

        Args:
             self (Director): An instance of Director.
        """
        letter = self._terminal_service.read_text("\nEnter a letter: ")
        self._puzzle.set_letter(letter)
        
    def _do_updates(self):
        """adds letters to the answer if they are correct, 
        and removes parts of the parachute if they are wrong.

        Args:
            self (Director): An instance of Director.
        """
        self._answers = self._puzzle.track_answers()

        if self._puzzle.right_answer() == "false":
            self._jumper.update_jumper()
     
        

    def _do_outputs(self):
        """prints the puzzle with as many letters found so far. 
        it also prints the parachute as it looks at the end of the turn.

        Args:
            self (Director): An instance of Director.
        """
        
        self._terminal_service.write_text(self._answers)
        print ()
        self._terminal_service.write_jumper(self._jumper._jumper_tracker)

