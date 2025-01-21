select 
    p.*,
	e."matchId",
    e."teamId",
    m."date",
    t."name" as "teamName",
	h_t."name" as "homeTeamName",
	a_t."name" as "awayTeamName"
from main."matchEvents" e
join main.matches m on e."matchId"=m."id" 
join main.teams t on e."teamId"=t."id"
join main.teams h_t on m."homeTeamId"=h_t."id"
join main.teams a_t on m."awayTeamId"=a_t."id"
join main.players p on e."playerId"=p.id
where e."playerId" = 13 and e."eventType" = 'Goal'