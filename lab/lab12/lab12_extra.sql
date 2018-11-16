.read lab12.sql

-- Q5
CREATE TABLE fa18favpets AS
  SELECT pet, COUNT(*) AS count FROM students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE fa18dog AS
  SELECT pet, COUNT(*) AS count FROM students GROUP BY pet HAVING pet = 'dog';


CREATE TABLE fa18alldogs AS
  SELECT 'dog' AS pet, COUNT(*) AS count FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*) as count FROM students WHERE seven = '7' GROUP BY denero;

-- Q6
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) AS count FROM students GROUP BY smallest ORDER BY smallest;
