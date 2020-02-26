from db_fixture.mysql_db import DB
import os

BASEDIR = os.path.dirname(os.path.dirname(__file__))
DEFAULT_SQL_PATH = BASEDIR + "/db_fixture/original_data.sql"
# 可以像这样表逐条插入，适用于小范围数据
data = {
    "learning_logs_topic": [
        {'text': "test_for_pymsql",
         'date_added': '2019-12-16 13:50:40.395332',
         'owner_id': 1,
         }, ]
}


# 可以读取sql文件更方便一些，但是也不适用于特别大的数据
def init_data(path=DEFAULT_SQL_PATH):
    db = DB()
    db.import_data(path)
    db.close()


if __name__ == "__main__":

    init_data(DEFAULT_SQL_PATH)
