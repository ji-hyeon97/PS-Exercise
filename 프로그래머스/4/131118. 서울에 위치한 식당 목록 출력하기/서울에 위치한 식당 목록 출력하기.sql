  select ri.REST_ID, ri.REST_NAME, ri.FOOD_TYPE, ri.FAVORITES, ri.ADDRESS, round(avg(rr.REVIEW_SCORE),2) as SCORE
    from REST_REVIEW rr
    join REST_INFO ri
      on ri.REST_ID = rr.REST_ID
   where ADDRESS like "서울%"
group by ri.REST_ID
order by SCORE desc, ri.FAVORITES desc
 
 
    