
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
        self.data = self.run_query(self.functionName,self.id)
        
    def get_id(self) -> int:
        """ Returns the id of the obj """
        return self.id
    
    def run_query(self, fun, var) -> object:
        """" Provides consistent method for getting data from db class"""
        try:
            sqlQuery = f"select * from {fun}({var})"
            data = json.loads(db.run_query(sqlQuery))
            # Return as a dict if a single item
            if len(data) == 1: data = data[0]
            return data
        except:
            return None
        
        
    # Produce a string of the dict on call
    def __str__(self):
        """ Return obj as a string in dict format"""
        return str(self.data)

class Match(MuddyBootsFW):
    """
    Hosts all details of a match. Uses super class for common functions
    """
    
    # Prep for all other params
    functionName = "fn_getMatch"
    
    def load_data(self) -> None:
        """Will query SQL to retrieve all details of this match
        Returns object hosting properties to be loaded
        """
        # Expand on the original load data
        super().load_data()
        
        # Retrieve the team details
        self.homeTeamId = self.data.pop('homeTeamId')
        self.awayTeamId = self.data.pop('awayTeamId')
        self.get_teams()

        #self.data["season"] = str(Season(self.data.pop('SeasonId')))
        #self.data["occasion"] = str(Occasion(self.data.pop('OccasionId')))
        
        # Set up the Person of the Match
        self.data['homePOTM'] = self.data.pop('homePOTMId')
        self.data['awayPOTM'] = self.data.pop('awayPOTMId')
        self.get_potm()
        
        # Retrieve all events
        self.get_events()
        
        # Retrieve the season
        self.seasonId = self.data.pop('seasonId')
        self.get_season()
        
        # Retrieve the occasion
        self.occasionId = self.data.pop('occasionId')
        self.get_occasion()
    
    def get_teams(self) -> None:
        """ Retrieves the teams """
        
        # Retrieve the two teams by removing the ID from the main data
        self.homeTeam = Team(self.homeTeamId)
        self.awayTeam = Team(self.awayTeamId)
        
        # Retrieve all players from the teams
        self.get_players()
    
    def get_players(self) -> None:
        """ Retrieves all the selected players for this match"""
        
        # Get data from the database
        players = self.run_query("fn_getMatchPlayers",self.id)
        
        # Clear the lists prior to adding all members
        self.homeTeam.clear_players()
        self.awayTeam.clear_players()
        
        # Add each player into the relevant team
        for player in players:
            teamId = player.pop("teamid")
            if teamId == self.homeTeam.get_id():
                self.homeTeam.add_player(player)
            else:
                self.awayTeam.add_player(player) 
    
    def get_potm(self) -> None:
        """ Retrieves the POTM for each team"""
        
        # Update the POTM only if one has been specified
        if self.data['homePOTM']: 
            self.data['homePOTM'] = self.homeTeam.get_player(self.data['homePOTM'])
            
        if self.data['awayPOTM']: 
            self.data['awayPOTM'] = self.awayTeam.get_player(self.data['awayPOTM'])  
            
    def get_occasion(self) -> None:
        """" Updates the occasion """
        self.occasion = self.run_query("fn_getOccasion",self.occasionId)
    
    def get_season(self) -> None:
        """ Retrieves the season """
        self.season = self.run_query("fn_getSeason",self.seasonId)
            
    def get_events(self) -> None:
        """ Retrieves all events for this match"""
        self.data["events"] = self.run_query("fn_getMatchEvents",self.id)
        
    def __str__(self):
        """ Modify the string return to update itself """
        self.data["homeTeam"] = str(self.homeTeam)
        self.data["awayTeam"] = str(self.awayTeam)
        self.data["season"] = self.season["description"]
        self.data["occasion"] = self.occasion["description"]
        return str(self.data)
    
class Team (MuddyBootsFW):
    """ Hosts all data on a team, including club"""
    functionName = "fn_getTeam"
    def __init__(self,id):
        super().__init__(id)
        self.clear_players()
        
    def add_player(self,player):
        """ Adds players to the player list"""      
        self.data["players"].append(player)
    
    def clear_players(self):
        """ Removes all players from the list"""
        self.data["players"] = []
    
    def remove_player(self,player):
        """ Removes a player from the list"""
        # Allow for none type to squash bugs
        self.data["players"].pop(player, None)
    
    def get_player(self,playerId):
        """" Retrieves a player based on Id """

        for player in self.data["players"]:
            if player["playerid"] == playerId:
                return player
    
    def get_players(self):
        """ Returns all players """
        return self.data["players"]
    
class Player (MuddyBootsFW):
    """ Hosts all data on a player"""
    functionName = "fn_getPlayer"

class Players:
    """ Hosts a temp db of players, will only update once requested"""
      
    
test = Match(6)
print(test)