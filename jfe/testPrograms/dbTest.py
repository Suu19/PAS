from unittest.mock import DEFAULT
import psycopg2

conn=psycopg2.connect("dbname=JFEQRLabel user=postgres password=admin")

command="create table jfe_data1 (id SERIAL PRIMARY KEY, qrcode_data varchar(500) UNIQUE NOT NULL, kikaku varchar(100), sunpou varchar(100), nagasa varchar(100), honsuu varchar(100), shitsuryou varchar(100), kouhann varchar(100), kessoku_bangou varchar(100), jicqa varchar(100), qa0306011 varchar(100), kikaku_hantei int, sunpou_hantei int, nagasa_hantei int,honsuu_hantei int, kessoku_bangou_hantei int, suuchi_keisan_hantei int,sougou_hantei int) "


#sql="insert into jfe_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,a,a,a,a,a,a,a,a,a,b,b,b,b,b,b)

try:
    cur=conn.cursor()
    cur.execute("insert into jfe_data(qrcode_data,kikaku,sunpou,nagasa,honsuu,shitsuryou,kouhann,kessoku_bangou,jicqa,qa0306011,kikaku_hantei,sunpou_hantei,nagasa_hantei,honsuu_hantei,kessoku_bangou_hantei,suuchi_keisan_hantei,sougou_hantei) values('168170202S001SS400 90X90X6 12.000 24AB','SS400','90X90X6','12','24','2386','N3746','168170202S001','JICQA','QA0306011',0,0,0,0,0,0,0)")
    #cur.execute(command)
    cur.close()
    conn.commit()
    #print("created")
    print("inserted")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()



