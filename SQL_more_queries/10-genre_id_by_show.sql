-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_show.title, tv_showgenres.genre_id
FROM tv_show.title AS t
INNER JOIN tv_show_genres AS g t.id = g.show_id
ORDER BY t.title, g.genre_id ASC;
