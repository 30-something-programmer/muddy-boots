-- Gets all matches while also resolving team IDs to their respective names
select 
	m_t.*,
	m.*
from joins."matchTeam" m_t
join main.matches m on m_t."matchId"=m."id"
where m."id" = 1