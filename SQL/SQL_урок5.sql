---1.
CREATE OR REPLACE PROCEDURE update_progress_bulk (
    IN p_resource_id INT,
    IN p_increment INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    updated_rows INT;
BEGIN
    UPDATE public.user_resource_progress
    SET progress_percent = LEAST(progress_percent + p_increment, 100)
    WHERE resource_id = p_resource_id
        AND progress_percent < 100;

    GET DIAGNOSTICS updated_rows = ROW_COUNT;
    RAISE NOTICE 'Количество обновленных строк: %', updated_rows;
END
$$;

select *
from public.user_resource_progress
where resource_id = 1 and progress_percent < 100


CALL public.update_progress_bulk(1, -5);

--2.
CREATE OR REPLACE FUNCTION get_user_skill_level(u_id INT, sk_id INT)
RETURNS INT
AS $$
	SELECT MAX(level)
	FROM user_skills
	WHERE user_id = u_id and skill_id = sk_id;
$$ LANGUAGE sql;

SELECT get_user_skill_level(1, 1)

--3
CREATE TABLE user_skills_log (
    log_id SERIAL PRIMARY KEY,
    id INTEGER,
    user_id INTEGER,
    skill_id INTEGER,
    level INTEGER,
    updating_at TIMESTAMP,
    operation TEXT
);

CREATE OR REPLACE FUNCTION log_after_change_func()
RETURNS TRIGGER AS $$
BEGIN
	IF TG_OP = 'INSERT' THEN
	    INSERT INTO user_skills_log(id, user_id, skill_id, level, updated_at, operation)
        VALUES (NEW.id, NEW.user_id, NEW.skill_id, NEW.level, NEW.updated_at, 'INSERT');
	ELSIF TG_OP = 'UPDATE' THEN
	    INSERT INTO user_skills_log(id, user_id, skill_id, level, updated_at, operation)
        VALUES (NEW.id, NEW.user_id, NEW.skill_id, NEW.level, NEW.updated_at, 'UPDATE');
	END IF;
	RETURN NULL;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER log_after_change
AFTER UPDATE OR INSERT ON public.user_skills
FOR EACH ROW
EXECUTE FUNCTION log_after_change_func();


select *
from user_skills;

select *
from user_skills_log;

INSERT INTO user_skills(user_id, skill_id, level, updated_at)
VALUES (1, 1, 4, NOW())

select *
from user_skills;

select *
from user_skills_log;

UPDATE user_skills
SET updated_at = NOW()
WHERE id = 3

select *
from user_skills;

select *
from user_skills_log;

--4
--SELECT * FROM user_skills WHERE user_id = ? - частичный индекс если постоянно запрашиваем одного и того же пользователя
--SELECT * FROM user_skills WHERE user_id = ? AND skill_id = ? - составной индекс (в порядке слева направо)
--SELECT * FROM user_resource_progress WHERE resource_id = ? AND progress_percent < - составной индекс (в порядке слева направо)
--SELECT * FROM users WHERE LOWER(email) = 'some@email.com' - индекс по выражению
--SELECT user_id, progress_percent FROM user_resource_progress WHERE resource_id = покрывающий индекс