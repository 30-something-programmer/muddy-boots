drop function IF EXISTS fn_getMatch;

create or replace function fn_getMatch(vmatch integer)
    returns table(
        "date" date, 
        "time" time, 
        "homeGoals" integer, 
        "awayGoals" integer, 
        "homeTeamId" integer, 
        "awayTeamId" integer, 
        "seasonId" integer, 
        "occasionId" integer, 
        "notes" text, 
        "homePOTMId" integer, 
        "awayPOTMId" integer, 
        "updates" text, 
        "ID" integer
    )
as $$;
    select * from matches where id = vmatch;
$$ language sql;