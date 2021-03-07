SELECT movies.title
FROM movies
INNER JOIN
(
SELECT movies.id, ratings.rating FROM movies
INNER JOIN ratings ON ratings.movie_id = movies.id
INNER JOIN stars ON movies.id = stars.movie_id
INNER JOIN people ON stars.person_id = people.id
WHERE people.name = "Chadwick Boseman"
)
AS idlist
ON idlist.id = movies.id
ORDER BY idlist.rating DESC
LIMIT 5;