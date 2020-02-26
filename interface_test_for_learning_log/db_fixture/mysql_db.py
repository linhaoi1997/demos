from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
import logging

logger = logging.getLogger(__name__)
# 读取文件设置
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = base_dir + "/db_config.ini"
DEFAULT_SQL_PATH = base_dir + "/db_fixture/original_data.sql"
print(DEFAULT_SQL_PATH)
cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# 封装mysql基本操作,两种方式初始化数据，清空表插入数据/清空表导入sql文件

class DB:
    def __init__(self):
        try:
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)
            logger.info("connect to database : %s" % (host + ':' + db))
        except OperationalError as e:
            logger.error("Mysql Error %d : %s" % (e.args[0], e.args[1]))

    # 清除表数据
    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()
        logger.info("clear all data from %s" % table_name)

    # 插入表数据 INSERT INTO students (class_id, name, gender, score) VALUES (2, '大牛', 'M', 80);
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + "(" + key + ") VALUES (" + value + ")"
        logger.info("execute sql : '%s'" % real_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)

        self.conn.commit()

    def close(self):
        self.conn.close()

    def import_data(self, path=DEFAULT_SQL_PATH):

        with open(path, 'r', encoding='utf8') as f:
            sql_list = []
            # 只处理drop，set,和insert语句,所以只适用于相表里插入数据，具体配置不太清楚
            for line in f.readlines():
                line = line.strip()
                if line.startswith('SET'):
                    # print(line)
                    sql_list.append(line.replace('\n', ''))
                elif line.startswith('DROP'):
                    # 由于外键关系删不掉表的情况下把所有底下资料移除就ok了，因为不删掉表所以不执行创建表操作
                    sql_list.append(line.replace('DROP', 'TRUNCATE').replace(' IF EXISTS', '').replace('\n', ''))
                elif line.startswith('INSERT'):
                    sql_list.append(line.replace('\n', ''))
                else:
                    pass
        with self.conn.cursor() as cursor:
            for real_sql in sql_list:
                logger.info("execute sql : '%s'" % real_sql)
                cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
                cursor.execute(real_sql)
        self.conn.commit()


if __name__ == "__main__":
    db = DB()
    table_name = 'learning_logs_topic'
    table_name2 = 'learning_logs_entry'
    data = {'text': "test_for_pymsql",
            'date_added': '2019-12-16 13:50:40.395332',
            'owner_id': 1,
            }
    db.clear(table_name)
    db.clear(table_name2)
    db.import_data()
    db.close()
    pass
