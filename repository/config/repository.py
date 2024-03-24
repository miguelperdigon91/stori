from typing import List, get_type_hints

from model.config.model_manager import ModelManager
from repository.config.queries_template import query_delete, create_table
from source.database import DataBase


class Repository:
    def __init__(self, implementer_class):
        self._data_base = DataBase()
        self._object_manager = ModelManager()
        self._implementer_class = implementer_class
        self._table_name = implementer_class.__name__

    def delete_all(self):
        query = query_delete(self._table_name, '')

        self._data_base.execute_query(query)

    def create_table(self):
        sql_type = {
            int: "BIGINT",
            float: "DOUBLE PRECISION",
            str: "CHARACTER VARYING"
        }

        fields = []

        attributes = self._implementer_class.__annotations__
        for attr, attr_type in attributes.items():
            data_type = sql_type[attr_type]

            fields.append('{} {}'.format(attr.replace('_', ''), data_type))

        query = create_table(
            self._table_name,
            ', '.join(fields)
        )

        self._data_base.execute_query(query)
