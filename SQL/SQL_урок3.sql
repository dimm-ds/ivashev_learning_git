INSERT INTO users (name, email)
VALUES ('Dima Andriyanov', 'dima.andriyanov.1981@mail.ru');

-- Привязка навыков к Dima Andriyanov (бэкенд)
INSERT INTO user_skills (user_id, skill_id, level, updated_at)
SELECT u.id, s.id, lvl.level, CURRENT_DATE
FROM users u
JOIN skills s ON s.name IN ('SQL', 'PostgreSQL', 'Critical Thinking', 'Presentation Skills')
JOIN (VALUES (3), (4), (5)) AS lvl(level) ON TRUE
WHERE u.name = 'Dima Andriyanov';



-- Для Dima Andriyanov
INSERT INTO user_resource_progress (user_id, resource_id, status_id, progress_percent, started_at, completed_at)
SELECT u.id, r.id, d.id, p.progress, CURRENT_DATE, 
       CASE WHEN d.code = 'cmp' THEN CURRENT_DATE ELSE NULL END
FROM users u
JOIN resources r ON r.title IN ('SQL for Beginners', 'SQL Joins Explained Visually', 'Effective Communication')
JOIN dictionaries d ON d.code IN ('cmp', 'prg', 'pln')
JOIN (VALUES (100), (50), (0)) AS p(progress) ON TRUE
WHERE u.name = 'Dima Andriyanov';


SELECT *
FROM users
WHERE (name LIKE 'A%' OR name LIKE '%ov') AND email IS NOT NULL;


SELECT * 
FROM
	(SELECT *
	FROM resources
	ORDER BY id DESC
	LIMIT 3
	)
ORDER BY title;

SELECT u.name, COUNT(DISTINCT skill_id) AS skills_count
FROM users u
JOIN user_skills us ON u.id = us.user_id
GROUP BY u.name
HAVING COUNT(DISTINCT skill_id) > 2
ORDER BY skills_count DESC, u.name;

SELECT COUNT(*)
FROM users;

SELECT COUNT(*)
FROM users
WHERE email IS NOT NULL; 

SELECT AVG(LENGTH(email))
FROM users;


