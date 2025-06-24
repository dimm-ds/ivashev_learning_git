--1
select
    u.name,
    count(*)
from user_resource_progress urp
join users u on u.id = urp.user_id
where status_id = 6 and (name ~'(.)\1\1' or name ~ '\d+')
group by u.name
having count(*) >= 1;

--2
select
	user_id,
	resource_id,
	progress_percent,
	count(*) over(partition by user_id),
	round(avg(progress_percent) over(partition by user_id order by resource_id), 1),
	row_number()  over(partition by user_id order by progress_percent desc),
	progress_percent - lag(progress_percent) over(partition by user_id order by resource_id)
from user_resource_progress
where user_id = 1
order by user_id, resource_id

--3
create or replace view user_progress_overview as
with cte as(
	select
	u.name,
	count(distinct urp.resource_id) as resourse_total,
	count(urp.resource_id) filter (WHERE status_id = 7) as resourse_finish,
	round(avg (urp.progress_percent), 1)
	from user_resource_progress urp
	join users u on u.id = urp.user_id
	group by name
	)
select *
from cte

select *
from user_progress_overview

