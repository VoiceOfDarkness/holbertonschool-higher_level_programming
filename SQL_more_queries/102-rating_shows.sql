-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT
    title,
    SUM(rate) AS rating
FROM
    tv_shows AS s
    INNER JOIN tv_show_rating AS r ON s.id = r.show_id
GROUP BY
    title
ORDER BY
    rating DESC;