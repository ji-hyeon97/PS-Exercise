select ID, NAME, HOST_ID
  from PLACES
  where HOST_ID
     in (select HOST_ID
           from PLACES
          group
             by HOST_ID
         having count(*) > 1
        )
  order 
  by ID