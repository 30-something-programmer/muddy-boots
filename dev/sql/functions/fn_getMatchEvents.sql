-- Retrieves all events of a specific match

drop function IF EXISTS fn_getMatchEvents;

create or replace function fn_getMatchEvents(vmatch integer) 
  returns table(  
    playerId integer,
    matchSegment varchar,
    matchTime varchar,
    eventType varchar,
    "data" varchar,
    id int,
    teamId int
) 
as $$
    select 
        "playerId", "matchSegment", "matchTime", "eventType", "data", "id", "teamId"
        from public.matchevents
        where "matchId" = vmatch;
$$ language sql;