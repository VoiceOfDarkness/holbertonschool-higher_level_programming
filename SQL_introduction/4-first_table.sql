-- create a table called first_table
CREATE TABLE first_table IF NOT EXISTS(
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  age INT
);
