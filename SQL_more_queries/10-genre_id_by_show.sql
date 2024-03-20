-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT
    tv_show.title,
    tv_show_genres.genre_id
FROM
    tv_show
    JOIN genre ON tv_show.genre_id = genre.id
ORDER BY
    tv_show.title, tv_show_genres.genre_id;