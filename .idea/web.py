#-*- coding:GBK -*-
import os,sys,time,shutil, filecmp
print ("start backup database")

backup_sql_path="/opt/db/bak"
backup_war_path="/opt/war/bak"


DB_NAME="izejin"
PASSWD="google"
DB_HOST="localhost"
USER="root"
def writeLogs(filename,contents):
    f=open(filename,'a+');
    f.write(contents);
    f.close();
if not os.path.exists(backup_sql_path):     #判断backup_sql_path目录是否存在
    Msg = '-' * 30 + time.strftime('%Y-%m-%d %H:%M:%S') + '-' * 30 + '\n'   #输出日期

print (Msg)

