-- Sélectionne le nom des villes depuis la table 'city'
SELECT cities.id, cities.name
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
ORDER BY cities.id ASC;
