-- lists all the cities of Carlifonia in the db

SELECT * FROM cities WHERE state_id = (SELECT id from states WHERE name = 'Carlifonia') ORDER BY id ASC;
