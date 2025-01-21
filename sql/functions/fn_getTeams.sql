-- drop function IF EXISTS fn_getPlayer;

create or replace function fn_getTeams(vteams integer[])
    returns table(
        "id" integer,
        "name" text,
        "clubID" integer
    )
as $$;
    select * from teams where id in (select unnest(vteams));
$$ language sql;