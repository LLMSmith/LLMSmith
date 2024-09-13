import langflow
import json

with open("basic_example.json", "r") as f:
    graph = json.load(f)

langflow.interface.run.build_langchain_object(graph["data"])