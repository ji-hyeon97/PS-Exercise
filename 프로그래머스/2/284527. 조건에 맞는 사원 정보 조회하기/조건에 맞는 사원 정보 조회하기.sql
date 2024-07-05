   select sum(g.SCORE) as SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
     from HR_DEPARTMENT d
     join HR_EMPLOYEES e
       on d.DEPT_ID = e.DEPT_ID
     join HR_GRADE g
       on g.EMP_NO = e.EMP_NO
    where g.year = 2022
 group by e.EMP_NO
 order by SCORE desc
    limit 1