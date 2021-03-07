SELECT people.name
FROM people
INNER JOIN
(
    --Id of people who have shared a movie with KB
    SELECT DISTINCT people.id
    FROM people
    INNER JOIN stars ON people.id = stars.person_id
    INNER JOIN movies ON stars.movie_id = movies.id
    INNER JOIN
    (
        --List of movies where KB has participated
        SELECT movies.id FROM movies
        INNER JOIN stars ON stars.movie_id = movies.id
        INNER JOIN people ON people.id = stars.person_id
        WHERE (people.name = "Kevin Bacon" AND people.birth = 1958)
    )
    AS pmovies
    ON movies.id = pmovies.id
    WHERE movies.id = pmovies.id AND people.name != "Kevin Bacon"
)
AS pshared
ON pshared.id = people.id
WHERE pshared.id = people.id
ORDER BY people.name;