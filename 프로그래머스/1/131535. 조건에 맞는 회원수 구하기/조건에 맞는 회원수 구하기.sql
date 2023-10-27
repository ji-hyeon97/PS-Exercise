SELECT count(*)as USERS from USER_INFO
where DATE_FORMAT(joined, "%Y") = 2021
and age >= 20
and age <= 29