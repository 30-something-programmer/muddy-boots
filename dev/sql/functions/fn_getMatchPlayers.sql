-- Retrieves all players and their team from a specific match

drop function IF EXISTS fn_getMatchPlayers;

create or replace function fn_getMatchPlayers(vmatch integer) 
  returns table(
    teamID integer,  
    playerID integer
) 
as $$
    select 
        t."id" as "teamID",
        p."id" as "playerID"
        from playermatch pm
        join players p on pm."playerId"=p."id" 
        join teams t on pm."teamId"=t."id"
        join matches m on pm."matchId"=m."id"
        where m."id" = vmatch;
$$ language sql;