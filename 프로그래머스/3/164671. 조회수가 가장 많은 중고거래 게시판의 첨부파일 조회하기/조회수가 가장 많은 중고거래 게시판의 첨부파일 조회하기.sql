SELECT CONCAT('/home/grep/src/', b.BOARD_ID, '/', f.FILE_ID, f.FILE_NAME, f.FILE_EXT) as FILE_PATH
  FROM USED_GOODS_FILE f
  JOIN (
       SELECT b.BOARD_ID
         FROM USED_GOODS_BOARD b
        ORDER 
           BY VIEWS DESC
        LIMIT 1) b
    ON b.BOARD_ID = f.BOARD_ID
 order
    by f.FILE_ID desc
