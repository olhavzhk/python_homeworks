SELECT employees.first_name, employees.last_name, departments.department_id, departments.depart_name FROM employees LEFT JOIN departments ON employees.department_id = departments.department_id;
SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province FROM employees AS e LEFT JOIN departments AS d ON e.department_id = d.department_id LEFT JOIN locations AS l ON d.location_id = l.location_id;
SELECT e.first_name, e.last_name, d.department_id, d.depart_name FROM employees AS e LEFT JOIN departments AS d ON e.department_id = d.department_id WHERE d.department_id = 80 OR d.department_id = 40;
SELECT depart_name FROM departments;
-- no manager name in db
SELECT jobs.job_title, CONCAT(employees.first_name,' ', employees.last_name) AS 'full name', (jobs.max_salary - employees.salary) AS 'salary difference'FROM employees LEFT JOIN jobs ON employees.job_id = jobs.job_id;
SELECT jobs.job_title, AVG(employees.salary) FROM jobs JOIN employees ON employees.job_id = jobs.job_id GROUP BY jobs.job_title;
SELECT CONCAT(e.first_name,' ', e.last_name) AS 'full name', e.salary FROM employees e JOIN departments ON e.department_id = departments.department_id JOIN locations ON locations.location_id = departments.location_id WHERE locations.city = 'London';
SELECT departments.depart_name, COUNT(employees.employee_id) AS number_of_employees FROM departments LEFT JOIN employees ON departments.department_id = employees.department_id GROUP BY departments.depart_name ORDER BY number_of_employees;
