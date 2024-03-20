-- script that lists all shows contained in the database hbtn_0d_tvshows
SELECT
    s.title,
    g.genre_id
FROM
    tv_show_genres AS g
    RIGHT JOIN tv_shows AS s ON s.id = g.show_id
ORDER BY
    s.title,
    g.genre_id;