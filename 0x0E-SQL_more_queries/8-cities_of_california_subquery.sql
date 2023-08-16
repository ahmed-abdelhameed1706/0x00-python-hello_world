-- Script to list all cities in a state
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
