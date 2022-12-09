class Jumper():
    """The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """

    def __init__(self):
        self._jumper_tracker = ["  ___", ' /___\\', ' \\   /', '  \\ /', "   O", "  /|\\", "  / \\", " ", "^^^^^^^"]
        
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
       
    def update_jumper(self):
        """Gets the current location.
        
        Returns:
            number: The current location,
        """
            
        self._jumper_tracker.pop(0)
      
                         