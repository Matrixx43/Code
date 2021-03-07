SELECT AVG(rating)
FROM
(SELECT ratings.rating
FROM movies
INNER JOIN ratings
ON movies.id = ratings.movie_id
WHERE movies.year = 2012);