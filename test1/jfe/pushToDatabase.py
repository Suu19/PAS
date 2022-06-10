from views import getImageName
import psycopg2

conn=psycopg2.connect(host="127.0.0.1",port=5432,database="dvdrental",user="postgres",password="admin")

imagesFiles=getImageName('C:\\Users\\nawthae\\test1\\static\\*')

cur=conn.cursor()
ok='OK'
ng='NG'


for i,image in enumerate(imagesFiles):
    cur.execute("INSERT INTO pushtodatabase  VALUES (%s,%s,%s,%s)",(i+1,image,ok,ng))
    


conn.commit()
cur.close()
conn.close()