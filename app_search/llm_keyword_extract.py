import g4f
import json
import random

g4f.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

prompt = """
Hi, Right now I have some descriptions from GitHub repositories and I want to go through them to **summarize** keywords or key phrases from them. Because I want to see what are the commonalities between them, and these commonalities can help me to find more similar apps, so can you help me to roughly summarize 10 keywords in terms of both functionality, and framework?
Don't describe words that are particularly useless, such as learning resources. Try to expand the vocabulary, e.g. if the extracted function is csv, try expanding it to data analysis, and other vocabulary as well, which will be more helpful.
I will provide you with some project descriptions in the format:
[serial number]: [description].
"""

dess = set()

for query in ['create_csv_agent', 'create_pandas_dataframe_agent', 'create_spark_dataframe_agent', 'PandasQueryEngine', 'PandasAI']:
    with open(f"./result/github_data/{query}.json", "r") as f:
        res = json.load(f)
    details = res['details']
    items = list(details.values())
    for item in items:
        if item['description']:
            des = item['description']
            dess.add(des)
cnt = 0
for des in dess:
    des = item['description']
    prompt += f'{str(cnt)}: {des}\n'
    cnt += 1


# streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')