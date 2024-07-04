  select hf.flavor
    from FIRST_HALF hf
    join ICECREAM_INFO ii
      on hf.FLAVOR = ii.FLAVOR
   where hf.TOTAL_ORDER > 3000
     and ii.INGREDIENT_TYPE = "fruit_based"
order by TOTAL_ORDER desc