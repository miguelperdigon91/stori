def query_insert(table_name, fields, values):
    return """
        INSERT INTO public."{table_name}"
                ({fields})
            VALUES
                ({values})
            RETURNING id
        """.format(table_name=table_name, fields=fields, values=values)


def query_insert_many(table_name, fields, values):
    return """
        INSERT INTO public."{table_name}"
                ({fields})
            VALUES
                {values}
        """.format(table_name=table_name, fields=fields, values=values)


def query_select(table_name, fields, filter_fields):
    return """
        SELECT
            {}
        FROM
            public."{}"
        WHERE
            {}
        """.format(fields, table_name, filter_fields)


def query_update(table_name, fields, filter_fields):
    return """
        UPDATE
            public."{}"
            {}
        WHERE
            {}
    """.format(table_name, fields, filter_fields)


def query_delete(table_name, filter_fields):
    return """
            DELETE
            FROM
                public."{}"
            WHERE
                {}
            """.format(table_name, filter_fields)
