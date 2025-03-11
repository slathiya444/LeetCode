-- Write your PostgreSQL query statement below
delete from Person
where id not in (
\tselect min(id)
\tfrom Person p
\tgroup by email
);