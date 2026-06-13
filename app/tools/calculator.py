def calculate(expression: str):

    try:
        result = eval(expression)

        return str(result)

    except Exception as e:

        return f"Error: {e}"