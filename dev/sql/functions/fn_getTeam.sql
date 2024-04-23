create or replace function fn_getteam(vteam integer)
    returns table(
        "id" integer,
        "name" text,
        "clubID" integer
    )
as $$;
    select * from teams where id = vteam;
$$ language sql;