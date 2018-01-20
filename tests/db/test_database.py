# coding=utf-8
from yapylib.db.database import Database


class TestDatabase(object):
    def setup_class(self):
        self.db = Database("postgresql://twocucao:pass123@localhost:5432/dvdrental")

    def setup_method(self):
        print("setup_method called for every method")

    def teardown_method(self):
        print("teardown_method called for every method")

    def teardown_class(self):
        print("teardown_class called once for the class")

    def test_two(self):
        print("two")

    def test_bulk_delete(self):
        assert False

    def test_bulk_insert(self):
        assert False

    def test_bulk_update(self):
        assert False

    def test_bulk_upsert(self):
        assert False

    def test_delete(self):
        assert False

    def test_insert(self):
        assert False

    def test_list_table_names(self):
        assert 'film_category' in self.db.list_table_names()

    def test_query(self):
        print("""assert 'PostgreSQL' in res[0][0]""")
        res = self.db.query("select version();")
        assert 'PostgreSQL' in res[0][0]

    def test_list_has_sequence(self):
        assert False

    def test_query_file(self):
        assert False

    def test_query_single_value(self):
        res = self.db.query_single_value("select version();")
        assert 'PostgreSQL' in res

    def test_table_exists(self):
        assert self.db.table_exists('film_category')
        assert False

    def test_table_exists(self):
        assert self.db.table_exists('films')

    def test_table_get_sequence_info(self):
        assert False

    def test_table_has_sequence(self):
        assert False

    def test_table_set_sequence_value(self):
        assert False

    def test_transaction(self):
        assert False

    def test_update(self):
        assert False

    def test_upsert(self):
        assert False
