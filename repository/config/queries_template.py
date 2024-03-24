def query_insert(table_name: str, fields: str, values: str):
    return """
        INSERT INTO public."{table_name}"
                ({fields})
            VALUES
                ({values})
            RETURNING id
        """.format(table_name=table_name, fields=fields, values=values)


def query_insert_many(table_name: str, fields: str, values: str):
    return """
        INSERT INTO public."{table_name}"
                ({fields})
            VALUES
                {values}
        """.format(table_name=table_name, fields=fields, values=values)


def query_select(table_name: str, fields: str, filter_fields: str):
    query = """
        SELECT
            {}
        FROM
            public."{}"
        WHERE
            {}
        """.format(fields, table_name, filter_fields)

    if not filter_fields or 'group by' in filter_fields.lower():
        return query.replace('WHERE', '')

    return query


def query_update(table_name: str, fields: str, filter_fields: str):
    return """
        UPDATE
            public."{}"
            {}
        WHERE
            {}
    """.format(table_name, fields, filter_fields)


def query_delete(table_name: str, filter_fields: str):
    query = """
            DELETE
            FROM
                public."{}"
            WHERE
                {}
            """.format(table_name, filter_fields)

    if not filter_fields:
        return query.replace('WHERE', '')

    return query


def create_table(table_name: str, fields: str):
    return """
            CREATE TABLE IF NOT EXISTS public."{}" (
              {}
            )
    """.format(table_name, fields)
