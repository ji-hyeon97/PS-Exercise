select ID,
       (select count(ID)
          from ECOLI_DATA
         where ed.ID = PARENT_ID) as CHILD_COUNT
  from ECOLI_DATA ed
 order
    by ID