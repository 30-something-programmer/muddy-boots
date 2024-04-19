

-- Using the MatchID, return all players and their teamID


select 
	t."id" as "teamID",
	t."name" as "teamName",
	p."id" as "playerID",
	p."squadName" as "playerName"
from playermatch mp
join players p on mp."playerId"=p."id" 
join teams t on mp."teamId"=t."id"
join matches m on mp."matchId"=m."id"
where m."id" = 194