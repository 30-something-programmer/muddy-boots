-- Retrieve all details of a match, grab extra info where possible
select 
	m.date, m.time, m."homeGoals", m."awayGoals", m."homeTeamId", m."awayTeamId",
	m."seasonId", m.notes, m."homePOTMId", m."awayPOTMId", m.updates,
	m.id as "matchID",
	s.description as "season",
	home_team.name as "HomeTeam",
	away_team.name as "AwayTeam"

from matches m
LEFT JOIN seasons s on m."seasonId"=s.id
LEFT JOIN teams home_team on m."homeTeamId"=home_team.id
LEFT JOIN teams away_team on m."awayTeamId"=away_team.id
where m.id = 194