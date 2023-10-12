SELECT b.BOOK_ID,a.AUTHOR_NAME,DATE_FORMAT(b.PUBLISHED_DATE,"%Y-%m-%d")
from BOOK b
join AUTHOR a on b.AUTHOR_ID = a.AUTHOR_ID
where category = "경제"
order by published_date