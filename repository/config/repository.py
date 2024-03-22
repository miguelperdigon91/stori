from typing import List

from model.config.model_manager import ModelManager
from source.database import DataBase


class Repository:
    def __init__(self, table_name: str, fields: List[str]):
        self._data_base = DataBase()
        self._object_manager = ModelManager()
        self._fields = fields
        self._table_name = table_name

    def _get_field_name(self, index: int):
        return self._fields[index]

    def _get_custom_field_list(self, indexes: List[int]):
        return ', '.join([self._get_field_name(index) for index in indexes])

    def _get_field_list(self):
        return ', '.join(self._fields)
