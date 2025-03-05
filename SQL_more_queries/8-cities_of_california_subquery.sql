-- Select the id and name of cities
SELECT cities.id, cities.name
FROM cities
-- Join the 'cities' table with the 'states' table using the foreign key 'state_id'
-- and the primary key 'id' of the 'states' table
JOIN states ON cities.state_id = states.id
-- Filter the results to keep only cities located in California
WHERE states.name = 'California'
-- Sort the results by city id in ascending order
ORDER BY cities.id ASC;
