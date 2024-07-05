select COUNT(*) as FISH_COUNT, 
       fni.FISH_NAME
  from FISH_INFO fi
  join FISH_NAME_INFO fni
    on fi.FISH_TYPE = fni.FISH_TYPE
 group
    by fi.FISH_TYPE, fni.FISH_NAME
 order 
    by FISH_COUNT desc