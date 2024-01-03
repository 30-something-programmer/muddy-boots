from modules.database import db
from flask import Flask, jsonify, request
import logging
from requests.exceptions import HTTPError


log = logging.getLogger("werkzeug")
log.setLevel(logging.INFO)


# Set up the flask server
flask_server = Flask("muddy boots") 
 
@flask_server.route('/', methods = ['GET']) 
def home(): 
	if(request.method == 'GET'): 
		return jsonify({'data': (f"{flask_server.name} is up and running") }) 

# Retrieve all matches
@flask_server.route('/matches', methods = ['GET', 'POST']) 
def matches(): 
	if(request.method == 'GET'):
		return db.run_query( 'SELECT * FROM main."matches"')
		
# Retrieve all players
@flask_server.route('/players', methods = ['GET', 'POST']) 
def players(): 
	if(request.method == 'GET'): 
		return db.players()
     
# Retrieve all seasons
@flask_server.route('/seasons', methods = ['GET', 'POST']) 
def seasons(): 
	if(request.method == 'GET'): 
		return db.seasons()
     
# Retrieve all leagues
@flask_server.route('/leagues', methods = ['GET', 'POST']) 
def leagues(): 
	if(request.method == 'GET'): 
		return db.leagues()
     
# Retrieve all teams
@flask_server.route('/teams', methods = ['GET', 'POST']) 
def teams(): 
	if(request.method == 'GET'): 
		return db.teams()
    
# Retrieve all clubs
@flask_server.route('/clubs', methods = ['GET', 'POST']) 
def clubs(): 
	if(request.method == 'GET'): 
		return db.clubs()
     
# Retrieve all goals
@flask_server.route('/goals', methods = ['GET', 'POST']) 
def goals(): 
	if(request.method == 'GET'): 
		return db.goals()
     
# Retrieve all cards
@flask_server.route('/cards', methods = ['GET', 'POST']) 
def cards(): 
	if(request.method == 'GET'): 
		return db.cards()
     
# Retrieve all users
@flask_server.route('/users', methods = ['GET', 'POST']) 
def users(): 
	if(request.method == 'GET'): 
		return db.users()
     
# Retrieve all officials
@flask_server.route('/officials', methods = ['GET', 'POST']) 
def officials(): 
	if(request.method == 'GET'): 
		return db.officials()
     
# Retrieve all organisers
@flask_server.route('/organisers', methods = ['GET', 'POST']) 
def organisers(): 
	if(request.method == 'GET'): 
		return db.organisers()

# Retrieve all squads
@flask_server.route('/squads', methods = ['GET', 'POST']) 
def squads(): 
	if(request.method == 'GET'): 
		return db.squads()
     
# Retrieve matchup between squads and matches
@flask_server.route('/match_squad', methods = ['GET', 'POST']) 
def match_squad(): 
	if(request.method == 'GET'): 
		return db.match_squad()
     
# Retrieve matchup between league and team
@flask_server.route('/league_team', methods = ['GET', 'POST']) 
def league_team(): 
	if(request.method == 'GET'): 
		return db.league_team()
     
# Retrieve matchup between league and season
@flask_server.route('/league_season', methods = ['GET', 'POST']) 
def league_season(): 
	if(request.method == 'GET'): 
		return db.league_season()
     
# Retrieve matchup between club and player
@flask_server.route('/club_player', methods = ['GET', 'POST']) 
def club_player(): 
	if(request.method == 'GET'): 
		return db.club_player()
     
# Retrieve matchup between oraniser and event
@flask_server.route('/organiser_event', methods = ['GET', 'POST']) 
def organiser_event(): 
	if(request.method == 'GET'): 
		return db.organiser_event()
     

# Retrieve matchup between match and team
@flask_server.route('/match_team', methods = ['GET', 'POST']) 
def match_team(): 
	if(request.method == 'GET'): 
		return db.match_team()
	
# Retrieve matchup between tournament and event
@flask_server.route('/tournament_event', methods = ['GET', 'POST']) 
def tournament_event(): 
	if(request.method == 'GET'): 
		return db.tournament_event()
     
# Retrieve matchup between club and team
@flask_server.route('/club_team', methods = ['GET', 'POST']) 
def club_team(): 
	if(request.method == 'GET'): 
		return db.club_team()
