-- lists all the cities of Carlifonia in the db

SELECT id, name  FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'Carlifonia') ORDER BY id ASC;
