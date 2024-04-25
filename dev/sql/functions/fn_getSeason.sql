-- drop function IF EXISTS fn_getPlayer;

create or replace function fn_getSeason(vseason integer)
    returns table(
        "id" integer,
        "description" text
    )
as $$;
    select * from public.seasons where id = vseason;
$$ language sql;