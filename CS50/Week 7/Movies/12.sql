SELECT movies.title FROM movies
INNER JOIN
(
SELECT movies.id FROM movies
INNER JOIN stars ON stars.movie_id = movies.id
INNER JOIN people ON people.id = stars.person_id
WHERE people.name = "Johnny Depp"
)
AS JD
ON JD.id = movies.id
INNER JOIN
(
SELECT movies.id FROM movies
INNER JOIN stars ON stars.movie_id = movies.id
INNER JOIN people ON people.id = stars.person_id
WHERE people.name = "Helena Bonham Carter"
)
AS HB
ON HB.id = movies.id
WHERE JD.id = HB.id;