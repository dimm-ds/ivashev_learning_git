CREATE TABLE IF NOT EXISTS students(
	id int PRIMARY KEY SERIAL,
	name text NOT NULL,
	email text UNIQUE,
	age int NOT NULL CHECK(age>13)
);

CREATE TABLE IF NOT EXISTS courses(
	id int PRIMARY KEY ,
	name text NOT NULL UNIQUE,
	teacher text
);

CREATE TABLE IF NOT EXISTS enrollments(
	id int PRIMARY KEY,
	student_id int NOT NULL REFERENCES students(id),
	course_id int NOT NULL REFERENCES courses(id),
	status text
);

INSERT INTO students (id, name, email, age) VALUES (1, 'Иван', 'ivan@mail.ru', 19);
INSERT INTO students (id, name, email, age) VALUES (2, 'Виктория', 'viktoriya@mail.ru', 13);
INSERT INTO students (id, name, email, age) VALUES (2, 'Виктория', 'viktoriya@mail.ru', 14);
INSERT INTO students (id, email, age) VALUES (2, 'ivan@mail.ru', 21);
INSERT INTO students (id, name, email, age) VALUES (2, 'Иван', 'ivan@mail.ru', 21);
INSERT INTO students (id, name, age) VALUES (3, 'Иван', 21);
SELECT * FROM students;

INSERT INTO courses (id, name, teacher) VALUES (1, 'SQL', 'Елена');
INSERT INTO courses (id, teacher) VALUES (1, 'Алексей');
INSERT INTO courses (id, name, teacher) VALUES (1, 'SQL', 'Алексей');
INSERT INTO courses (id, name, teacher) VALUES (2, 'SQL', 'Алексей');
INSERT INTO courses (id, name, teacher) VALUES (2, 'Docker', 'Алексей');
INSERT INTO courses (id, name, teacher) VALUES (3, 'Django', 'Алексей');
INSERT INTO courses (id, name, teacher) VALUES (4, 'HTML&CSS', 'Юлия');
SELECT * FROM courses;

INSERT INTO enrollments (id, student_id, course_id) VALUES (1, 1, 1);
INSERT INTO enrollments (id, student_id, course_id) VALUES (1, 1, 1);
INSERT INTO enrollments (id, student_id, course_id) VALUES (2, 1, 4);
INSERT INTO enrollments (id, student_id, course_id, status) VALUES (2, 1, 3, 'Done');
INSERT INTO enrollments (id, student_id, course_id, status) VALUES (3, 2, 1, 'Done');
INSERT INTO enrollments (id, student_id, course_id, status) VALUES (4, 3, 2, 'Done');
INSERT INTO enrollments (id, student_id, course_id, status) VALUES (5, 3, 3, 'Done');
SELECT * FROM enrollments;


SELECT s.name AS student_name, c.name AS course_name
FROM students s INNER JOIN enrollments e
ON s.id = e.student_id INNER JOIN courses c
ON e.course_id = c.id;


SELECT c.name AS course_name, s.name AS student_name
FROM courses c LEFT JOIN enrollments e
ON c.id = e.course_id LEFT JOIN students s
ON e.student_id = s.id;

SELECT c.name AS course_name, s.name AS student_name
FROM courses c LEFT JOIN enrollments e
ON c.id = e.course_id CROSS JOIN students s



























