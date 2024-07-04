SELECT USER_ID,product_id from ONLINE_SALE
group by USER_ID,product_id
having count(USER_ID) > 1
order by user_id, product_id desc