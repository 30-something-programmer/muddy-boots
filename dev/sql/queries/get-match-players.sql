-- Returns the match, team and players data

select 
	t."id" as "teamID",
	t."name" as "teamName",
	p."id" as "playerID",
	p."squadName" as "playerName"
from joins."matchPlayers" mp
join main.players p on mp."playerId"=p."id" 
join main.teams t on mp."teamId"=t."id"
join main.matches m on mp."matchId"=m."id"
where m."id" = 194