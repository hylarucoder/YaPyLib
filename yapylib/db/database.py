from sqlalchemy import create_engine, inspect, text
import os

DATABASE_URL = os.environ.get('DATABASE_URL')


class Database(object):
    """
    数据库
    专为日常简单操作 PostgreSQL 封装
    """

    def __init__(self, db_url=None, **kwargs):
        self.db_url = db_url or DATABASE_URL
        if not self.db_url:
            raise ValueError("You must provide a db url")
        self._engine = create_engine(self.db_url, **kwargs)
        # connect to the database.
        self.db = self._engine.connect()
        self.open = True
        # init other attributes for short cut access

        self.db_name = str(self._engine.url).split("/")[-1]
        pass

    def close(self):
        self.db.close()
        self.open = False

    def __enter__(self):
        return self

    def __exit__(self, exc, val, traceback):
        self.close()

    """
    ===> 针对表
    """

    def list_table_names(self):
        return inspect(self._engine).get_table_names()

    def table_exists(self, table_name):
        """True if table exists in the database"""
        return self._engine.has_table(table_name)

    """
    ===> 针对表中的序列
    """

    def table_has_sequence(self, table_name=None, seq_name=None):
        """
        :param table_name:
        :param seq_name:
        :return:
        """
        query = """SELECT EXISTS (SELECT 1 FROM pg_class
                WHERE upper(relkind)='S' AND relname='%s')""" % seq_name
        return self.query_single_value(query)

    def table_get_sequence_info(self, table_name=None, seq_name=None):
        return True

    def table_set_sequence_value(self, table_name=None, seq_name=None):
        return True

    def _get_next_seq_val(self, seq_name):
        return self.query_single_value("select nextval('\"%s\"')" % seq_name)

    def _get_min_row_id(self, seq_name):
        return self.query_single_value("select nextval('\"%s\"')" % seq_name)

    def _guess_sequence_params(self, seq_name):
        return self.query_single_value("select nextval('\"%s\"')" % seq_name)

    def _get_max_row_id(self, table, pk_name, min_value, increment):
        """
        :param seq_name:
        :return:
        """
        query = """
          SELECT "{pk_name}"
          FROM {table}
          WHERE mod("{pk_name}" , {increment})={mod_result}
          ORDER BY "{pk_name}" DESC LIMIT 1
          """.format(pk_name=pk_name,
                     table=table,
                     increment=increment,
                     mod_result=(min_value % increment))

        result = self.query(query)
        if result is None:
            return 0
        else:
            return result[0]

    def _set_current_sequence_value(self, seq_name, value):
        """
        :param seq_name:
        :param value:
        :return:
        """
        return self.query("select setval('\"%s\"', %d, True)" % (seq_name, value))  # noqa

    def _get_current_sequence_value(self, seq_name):
        """
        :param seq_name:
        :return:
        """
        return self.query_single_value("select currval('\"%s\"')" % seq_name)

    def list_all_tables_sequence_info(self, table_seq_kv):
        sequence_info = {}

        for table, seq_name in table_seq_kv.items():
            first_value = self._get_next_seq_val(seq_name)
            min_value = self._get_min_row_id(seq_name)
            increment = self._guess_sequence_params(seq_name)
            max_value = self._get_max_row_id(seq_name)
            if first_value > 1:
                self._set_current_sequence_value(
                    seq_name, first_value - increment)
            current_value = self._get_current_sequence_value(seq_name)
            sequence_info[seq_name] = {
                'table_name': table,
                'seq_name': seq_name,
                'min_value': min_value,
                'increment': increment,
                'max_value': max_value,
                'current_value': current_value,
                'broken': current_value < max_value
            }

        return sequence_info

    """
    ===> 针对表中的索引
    """

    """
    ===> 查询 增删改查
    ===> 查询语句
    """

    def query_single_value(self, query):
        """
        TODO: 查询
        """
        res = self.db.execute(query).fetchone()
        return res[0]

    def query(self, query, fetchall=False, **params):
        """
        TODO: 查询
        """
        # 如果不加text的话,一般像pgsql这种对语法支持比较多的容易被
        cursor = self.db.execute(text(query), **params)
        return list(cursor)

    def insert(self, query):
        """
        TODO: 插入
        """
        self.db.execute(text(query))

    def update(self, query):
        """
        TODO: 更新
        """
        self.db.execute(text(query))

    def upsert(self, query):
        """
        TODO: 如果存在则更新,如果不存在则插入
        """
        self.db.execute(text(query))

    def delete(self, query):
        """
        TODO: 删除
        """
        self.db.execute(text(query))

    def bulk_insert(self, query):
        """
        TODO: 批量插入
        """
        self.db.execute(text(query))

    def bulk_update(self, query):
        """
        TODO: 批量更新
        """
        self.db.execute(text(query))

    def bulk_upsert(self, query):
        """
        TODO: 批量upsert
        """
        self.db.execute(text(query))

    def bulk_delete(self, query):
        """
        TODO: 批量删除
        """
        self.db.execute(text(query))

    def query_file(self, query):
        """
        TODO: 执行文件中SQL
        """
        pass

    def transaction(self):
        """
        TODO: 个人认为这玩意还是
        """
        pass
    """
    ===> 一些Helper方法
    """

    def autofix_sequence_error(self):
        """
        TODO: 修复 navicat 迁移 records 带来的 sequence 问题
        """
        pass
