SELECT COUNT(rating)
FROM (SELECT ratings.rating
FROM movies
INNER JOIN ratings
ON movies.id = ratings.movie_id WHERE ratings.rating = 10.0)
WHERE rating = 10;