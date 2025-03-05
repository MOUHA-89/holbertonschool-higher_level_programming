--  city table
SELECT city.name
-- city concerning
FROM city
-- link cities
JOIN state ON city.state_id = state.id
-- state table
WHERE state.name = 'california';
