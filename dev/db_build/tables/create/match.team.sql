-- An entry in this table identifies a team to a match. 

CREATE TABLE match.team
(
    match_team_id   serial primary key,     -- Primary ID of the MatchTeam - unique for each team assigned to a match
    match_id         int NOT NULL,           -- FK. The ID of the match
    team_id          int NOT NULL,           -- FK. ID of the team
    is_home_team          boolean NULL,           -- True if this team is the home team.
    goals           int NOT NULL DEFAULT 0  -- Number of goals this team scored for this match
)