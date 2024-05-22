CREATE TABLE workers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, salary INTEGER);
ALTER TABLE workers RENAME TO Dunder_Mifflin_employees;
ALTER TABLE Dunder_Mifflin_employees ADD position TEXT;
INSERT INTO Dunder_Mifflin_employees (name, salary, position) VALUES ('Michael Scott', 3000, 'Regional Manager'), ('Pam Beesly', 1800, 'Receptionist'), ('Jim Halpert', 2500, 'Sales'), ('Toby Flenderson', 2200, 'Human Resources');
UPDATE Dunder_Mifflin_employees SET name = 'Pam Halpert', salary = 2400, position = 'Office Administrator' WHERE id = 2;
DELETE FROM Dunder_Mifflin_employees WHERE id = 4;