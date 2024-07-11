-- settings.sql
CREATE DATABASE cities_project;
CREATE USER cities_projectuser WITH PASSWORD 'cities_project';
GRANT ALL PRIVILEGES ON DATABASE cities_project TO cities_projectuser;