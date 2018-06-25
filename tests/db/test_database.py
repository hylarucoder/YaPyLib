# coding=utf-8
from yapylib.helpers.db import Database


class TestDatabase(object):
    def setup_class(self):
        self.database = Database("sqlite:///:memory:", echo=True)

    def setup_method(self):
        print("setup_method called for every method")

    def teardown_method(self):
        print("teardown_method called for every method")

    def teardown_class(self):
        print("teardown_class called once for the class")

    def test_two(self):
        print("two")

    def test_bulk_delete(self):
        assert True

    def test_bulk_insert(self):
        assert True

    def test_bulk_update(self):
        assert True

    def test_bulk_upsert(self):
        assert True

    def test_delete(self):
        assert True

    def test_insert(self):
        assert True

    def test_list_table_names(self):
        assert True #'film_category' in self.database.list_table_names()

    def test_query(self):
        res = self.database.query("select 'SQLite'")
        assert 'SQLite' in res[0][0]

    def test_list_has_sequence(self):
        assert True

    def test_query_file(self):
        assert True

    def test_query_single_value(self):
        res = self.database.query_single_value("select 'SQLite'")
        assert 'SQLite' in res

    def test_table_exists(self):
        # assert self.database.table_exists('film_category')
        assert True

    def test_table_get_sequence_info(self):
        assert True

    def test_table_has_sequence(self):
        assert True

    def test_table_set_sequence_value(self):
        assert True

    def test_transaction(self):
        assert True

    def test_update(self):
        assert True

    def test_upsert(self):
        assert True
