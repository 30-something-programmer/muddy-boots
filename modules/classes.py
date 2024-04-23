
import json
from database import db # Retrieve the already prepped db connection

class MuddyBootsFW:
    """Hosts common paramaters across classes"""
    functionName = None
    
    def __init__ (self, id) -> None:
        self.id = id
        self.load_data()

    def load_data(self) -> None:
        """Will query SQL to retrieve all details of this match
        Returns object hosting properties to be loaded
        """
        try:
            sqlQuery = f"select * from {self.functionName}({self.id})"
        except:
            return None
            
        return json.loads(db.run_query(sqlQuery))[0]

    # Host a to_dict function
    def to_dict(self):
        """ Reorganises into a dict """
        return vars(self)
        
    
    def __str__(self):
        """ Return obj as a string in dict format"""
        return str(self.to_dict())

class Match(MuddyBootsFW):
    """
    Hosts all details of a match. Uses super class for common functions
    """
    
    # Prep for all other params
    functionName = "fn_getMatch"
    
    def __init__(self, id) -> None:
        super().__init__(id)
    
    def load_data(self) -> None:
        """Will query SQL to retrieve all details of this match
        Returns object hosting properties to be loaded
        """
        # Expand on the original load data
        data = super().load_data()
        
        # Retrieve the two teams
        self.homeTeam = Team(data['homeTeamId'])
        self.awayTeam = Team(data['awayTeamId'])
        self.date = data["date"]
        self.time = data["time"]
        self.homeGoals = data["homeGoals"]  
        self.awayGoals = data["awayGoals"]
        #self.season = Season(data['SeasonId'])
        #self.occasion = Occasion(data['OccasionId'])
        if data['homePOTMId']: 
            self.homePOTM = Player(data['homePOTMId'])
        else:
            self.homePOTM = None
        if data['awayPOTMId']:
            self.awayPOTM = Player(data['awayPOTMId'])
        else:
            self.awayPOTM = None
        self.updates = data["updates"]
    
    def __str__(self):
        """ Return obj as a string in dict format"""
        return str(self.to_dict())

class Team (MuddyBootsFW):
    """ Hosts all data on a team, including club"""
    functionName = "fn_getTeam"
    def __init__(self, id) -> None:
        super().__init__(id)
        
class Player (MuddyBootsFW):
    """ Hosts all data on a player"""
    functionName = "fn_getPlayer"
    def __init__(self, id) -> None:
        super().__init__(id)
    
                     
test = Match(146)
print(test)