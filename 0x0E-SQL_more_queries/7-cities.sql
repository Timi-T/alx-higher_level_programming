-- New database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
DROP table IF EXISTS hbtn_0d_usa.cities;
CREATE table IF NOT EXISTS hbtn_0d_usa.cities(
	id INT NOT NULL UNIQUE AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
