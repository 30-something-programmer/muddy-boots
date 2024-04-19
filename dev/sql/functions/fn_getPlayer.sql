-- drop function IF EXISTS fn_getPlayer;

create or replace function fn_getPlayer(vplayer integer)
    returns table(
        "id" integer,
        "positions" text,
        "knownas" text,
        "squadName" text,
        "forname" text,
        "userid" integer,
        "surname" text
    )
as $$;
    select * from players where id = vplayer;
$$ language sql;