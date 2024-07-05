select count(*) as FISH_COUNT,
       cast(DATE_FORMAT(time, "%m") as unsigned) as MONTH
  from FISH_INFO
 group
    by MONTH
 order
    by MONTH
