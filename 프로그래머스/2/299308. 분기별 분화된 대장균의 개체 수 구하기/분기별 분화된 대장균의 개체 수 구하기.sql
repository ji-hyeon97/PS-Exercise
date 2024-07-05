select 
  case
  when cast(DATE_FORMAT(DIFFERENTIATION_DATE, "%m") as UNSIGNED) < 4 then "1Q"
  when cast(DATE_FORMAT(DIFFERENTIATION_DATE, "%m") as UNSIGNED) < 7 then "2Q"
  when cast(DATE_FORMAT(DIFFERENTIATION_DATE, "%m") as UNSIGNED) < 10 then "3Q"
  else "4Q"
  END as QUARTER,
  count(*) as ECOLI_COUNT
  from ECOLI_DATA
  group 
     by QUARTER
  order
     by QUARTER