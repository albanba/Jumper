class Jumper():
    """The person keeping track of the parachute status. 
    
    The responsibility of the jumper is to update the status of the parachute.
    
    Attributes:
        _jumper_tracker (list) <str>: contains the elements of the complete parachute
    """

    def __init__(self):
        self._jumper_tracker = ["  ___", ' /___\\', ' \\   /', '  \\ /', "   O", "  /|\\", "  / \\", " ", "^^^^^^^"]
        
        """Constructs the initial parachute.

        Args:
            self (Jumper): An instance of Jumper.
        """
       
    def update_jumper(self):
        """eliminates the top line from the parachute
        
        Args:
            self (Jumper): An instance of Jumper.
        """  
        self._jumper_tracker.pop(0)
      
                         