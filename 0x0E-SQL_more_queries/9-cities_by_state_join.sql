-- Script to list all cities
SELECT cities.id, cities.name, states.name FROM cities, states ORDER BY cities.id ASC;
