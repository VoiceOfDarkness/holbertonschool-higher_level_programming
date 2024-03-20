SELECT
    g.name AS genre,
    count(sg.show_id) AS number_of_shows
FROM
    tv_show_genres s
    LEFT JOIN tv_genres g ON s.genre_id = g.id
GROUP BY
    g.name
ORDER BY
    2 DESC;