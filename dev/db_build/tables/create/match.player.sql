-- An entry in this table assigns a player to a team that's already assigned to a match.

CREATE TABLE match.team
(
    ID              serial primary key,         -- Primary ID of the MatchPlayer - unique for each player assigned to a MatchTeam
    MatchTeamID     int NOT NULL,               -- FK. The ID of the MatchTeam
    PosX            int NOT NULL DEFAULT 0,     -- The X position assigned to this player. 0 if sub/not assigned
    PosY            int NOT NULL DEFAULT 0,     -- The Y position assigned to this player. 0 if sub/not assigned
    isHome          boolean NULL                -- True if this team is the home team.
)