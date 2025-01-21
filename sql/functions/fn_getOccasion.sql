-- drop function IF EXISTS fn_getPlayer;

create or replace function fn_getOccasion(voccasion integer)
    returns table(
        "id" integer,
        "description" text
    )
as $$;
    select * from public.occasions where id = voccasion;
$$ language sql;