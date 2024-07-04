  select MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") as DATE_OF_BIRTH
    from MEMBER_PROFILE
   where DATE_FORMAT(DATE_OF_BIRTH, "%m") = 3
     and TLNO is not null
     and GENDER = "W"
order by MEMBER_ID