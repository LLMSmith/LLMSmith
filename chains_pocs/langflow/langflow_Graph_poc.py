import langflow
import json

with open("basic_example.json", "r") as f:
    graph = json.load(f)

x = langflow.graph.graph.base.Graph(graph["data"]["nodes"], graph["data"]["edges"])
x.build()