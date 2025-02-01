-- An entry in this table holds information about a single match.
-- Teams are assigned via match.team
-- Players are assigned via match.player

CREATE TABLE match.details
(
    match_id  serial primary key,     -- Primary ID of the match
    kickoff     timestamp NULL,      -- The date and time of when the match begins
    season_id    int NULL,       -- FK. The ID of the season
    league_id    int NULL,       -- FK. If filled, the ID of the league. Mutually exclusive to CompetitionID
    tournament_id   int NULL,   -- FK. If filled, the ID of the competition. Mutually exclusuve to LeagueID
    venue_id         int NULL,   -- FK. ID of the pitch
    type_id      int NULL       -- FK. ID of the type
)