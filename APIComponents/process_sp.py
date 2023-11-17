class ExecuteStoredProcedure:
    @classmethod
    def call_insert_procedure(cls, procedure_name, params, conn):
        cursor = conn.cursor()
        json_list = []
        procedure_name = procedure_name
        if params:
            param_markers = ", ".join(["%s" for _ in params])
            sql_query = "CALL " + procedure_name + "(" + param_markers + ")"
            cursor.execute(sql_query, params)
            conn.commit()
        cursor.close()
        conn.close()
        return json_list
