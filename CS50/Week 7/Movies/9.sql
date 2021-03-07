SELECT name FROM people
INNER JOIN
(
SELECT DISTINCT(people.id)
FROM
(
people
INNER JOIN stars ON people.id = stars.person_id
INNER JOIN movies ON movies.id = stars.movie_id
)
WHERE movies.year = 2004
)
AS file2
ON file2.id = people.id
ORDER BY people.birth;