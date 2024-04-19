


class match ():
    """
    Hosts all details of a match.
    """
    
    def __init__(self, id) -> None:
        self.id = id
    
    def QuerySQL(self, database) -> object:
        """Will query SQL to retrieve all details of this match
        Returns object hosting properties to be loaded
        """
        return database.get_match(self.id)
        
    def load_players(teamID):
        """
        Args:
            teamID (_type_): _description_
        """