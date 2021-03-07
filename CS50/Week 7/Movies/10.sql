SELECT name FROM people
INNER JOIN
(
SELECT DISTINCT(person_id) FROM directors
INNER JOIN movies ON movies.id = directors.movie_id
INNER JOIN ratings ON movies.id = ratings.movie_id
WHERE ratings.rating >= 9
)
AS file2
ON file2.person_id = people.id;