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
if not os.path.exists(backup_sql_path):     #�ж�backup_sql_pathĿ¼�Ƿ����
    Msg = '-' * 30 + time.strftime('%Y-%m-%d %H:%M:%S') + '-' * 30 + '\n'   #�������

print (Msg)

