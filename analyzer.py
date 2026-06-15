def run_code(df, code):

    local_vars = {"df": df}

    try:
        exec(code, {}, local_vars)

        if "result" in local_vars:
            return local_vars["result"]

        return "No result variable found."

    except Exception as e:
        return f"Error: {str(e)}"