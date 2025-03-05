--  lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT city.name
FROM city
JOIN state ON city.state_id = state.id
WHERE state.name = 'california';
