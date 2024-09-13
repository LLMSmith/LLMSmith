## Usage

### Experiments in Paper

pip install related packages：

```
pip install treelib
```

Install pycg

```
pip install pycg==0.0.7
```

pip install specific version of frameworks in paper：

```
pip install langchain==0.0.232 
pip install llama-index==0.7.13
pip install pandasai==0.8.0
pip install langflow==0.2.7
pip install griptape==0.17.1
pip install lagent==0.1.1
pip install metagpt==0.7.3
pip install vanna==0.3.3
pip install langroid==0.1.224
```

To launch static analysis，clone the corresponding source code.

### Code Running

To scan the frameworks, using `chain_paper.py`, except for metagpt and vanna：

```
python3 chain_paper.py --package=xxx --dir='xxx'
```

As for Metagpt, vanna, please use `chain_develop.py`:

```
python3 chain_develop.py --package=xxx --dir='xxx'
```

The command to scan the targeted package:

```
python3 chain_paper.py --package=pandasai --dir='./pandas-ai-0.8.1'
python3 chain_paper.py --package=langchain --dir='./langchain'
python3 chain_paper.py --package=llama_index --dir='./llama_index_0.7.13' 
python3 chain_paper.py --package=lagent --dir='./lagent'
python3 chain_paper.py --package=griptape --dir='./griptape'
python3 chain_paper.py --package=langflow --dir='./langflow/src/backend'
python3 chain_develop.py --package=vanna --dir='./vanna/src'
python3 chain_develop.py --package=metagpt --dir='./metagpt'
```

Example output:

```
pandasai:
➜  scanner orgpy chain_paper.py --package=pandasai --dir='./pandas-ai-0.8.1'                                                    
exec
[+] Current initial file: pandasai/__init__.py
[DEBUG] ---->  pandasai/__init__.py
[DEBUG] ---->  pandasai/middlewares/base.py
[DEBUG] ---->  pandasai/helpers/openai_info.py
exec
└── pandasai/__init__.py/run_code_0
    └── pandasai/__init__.py/run_0
        └── pandasai/__init__.py/__call___0

eval
[+] Current initial file: pandasai/__init__.py
[DEBUG] ---->  pandasai/__init__.py
[DEBUG] ---->  pandasai/middlewares/base.py
[DEBUG] ---->  pandasai/helpers/openai_info.py
[DEBUG] ---->  pandasai/__init__.py
[DEBUG] ---->  pandasai/middlewares/base.py
[DEBUG] ---->  pandasai/helpers/openai_info.py
[DEBUG] ---->  pandasai/__init__.py
[DEBUG] ---->  pandasai/middlewares/base.py
[DEBUG] ---->  pandasai/helpers/openai_info.py
[DEBUG] ---->  pandasai/__init__.py
[DEBUG] ---->  pandasai/middlewares/base.py
[DEBUG] ---->  pandasai/helpers/openai_info.py
eval
├── pandasai/__init__.py/_get_prompt_0
│   ├── pandasai/__init__.py/_retry_run_code_0
│   │   └── pandasai/__init__.py/run_code_1
│   │       └── pandasai/__init__.py/run_3
│   ├── pandasai/__init__.py/conversational_answer_0
│   │   └── pandasai/__init__.py/run_2
│   └── pandasai/__init__.py/run_0
│       └── pandasai/__init__.py/__call___0
└── pandasai/__init__.py/run_code_0
    └── pandasai/__init__.py/run_1

[+] Current initial file: pandasai/helpers/anonymizer.py
subprocess.run
[RESULT]: --------> pandasai
--------------------------------------------------
[TOTAL] Total time costs: 0.977337121963501
[TOTAL] Total call chain: 5
--------------------------------------------------
[TOTAL] Total number of cross file: 5
[AVG] Average cross file number: 1.0
[MAX] Max cross file number: 1
--------------------------------------------------
[TOTAL] Total call chain length: 20
[AVG] Average call chain length: 4.0
[MAX] Max call chain length: 5
--------------------------------------------------
[*] Implicit call number: 0
```

```
langchain:
➜  scanner orgpy chain_paper.py --package=langchain --dir='./langchain'                                                           
exec
[+] Current initial file: langchain/experimental/cpal/models.py
[+] Current initial file: langchain/tools/python/tool.py
[INFO] implicit function:  langchain/tools/python/tool.py/PythonAstREPLTool._run_0
[DEBUG] ---->  langchain/tools/__init__.py
[DEBUG] ---->  langchain/tools/python/tool.py
[DEBUG] ---->  langchain/agents/agent_toolkits/spark/base.py
[DEBUG] ---->  langchain/agents/agent_toolkits/pandas/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/spark/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/agent_toolkits/pandas/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/agent_toolkits/pandas/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/agent_toolkits/pandas/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/agent_toolkits/pandas/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/spark/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
exec
└── langchain/tools/python/tool.py/PythonAstREPLTool._run_0
    ├── langchain/agents/agent_toolkits/pandas/base.py/_get_functions_multi_prompt_0
    │   └── langchain/agents/agent_toolkits/pandas/base.py/_get_functions_prompt_and_tools_1
    │       └── langchain/agents/agent_toolkits/pandas/base.py/create_pandas_dataframe_agent_3
    ├── langchain/agents/agent_toolkits/pandas/base.py/_get_functions_single_prompt_0
    │   └── langchain/agents/agent_toolkits/pandas/base.py/_get_functions_prompt_and_tools_0
    │       └── langchain/agents/agent_toolkits/pandas/base.py/create_pandas_dataframe_agent_2
    ├── langchain/agents/agent_toolkits/pandas/base.py/_get_multi_prompt_0
    │   └── langchain/agents/agent_toolkits/pandas/base.py/_get_prompt_and_tools_0
    │       └── langchain/agents/agent_toolkits/pandas/base.py/create_pandas_dataframe_agent_0
    │           └── langchain/agents/agent_toolkits/csv/base.py/create_csv_agent_0
    ├── langchain/agents/agent_toolkits/pandas/base.py/_get_single_prompt_0
    │   └── langchain/agents/agent_toolkits/pandas/base.py/_get_prompt_and_tools_1
    │       └── langchain/agents/agent_toolkits/pandas/base.py/create_pandas_dataframe_agent_1
    └── langchain/agents/agent_toolkits/spark/base.py/create_spark_dataframe_agent_0

[+] Current initial file: langchain/utilities/python.py
[DEBUG] ---->  langchain/python.py
[DEBUG] ---->  langchain/tools/__init__.py
[DEBUG] ---->  langchain/tools/python/tool.py
[DEBUG] ---->  langchain/agents/load_tools.py
[DEBUG] ---->  langchain/agents/agent_toolkits/python/base.py
[DEBUG] ---->  langchain/utilities/__init__.py
[DEBUG] ---->  langchain/utilities/python.py
[INFO] implicit function:  langchain/chains/pal/base.py/PALChain._call_0
[DEBUG] ---->  langchain/chains/pal/base.py
[DEBUG] ---->  langchain/__init__.py
[DEBUG] ---->  langchain/experimental/cpal/base.py
[DEBUG] ---->  langchain/agents/load_tools.py
[DEBUG] ---->  langchain/chains/loading.py
[DEBUG] ---->  langchain/chains/__init__.py
[DEBUG] ---->  langchain/chains/pal/base.py
[DEBUG] ---->  langchain/chains/loading.py
exec
└── langchain/utilities/python.py/PythonREPL.run_0
    └── langchain/chains/pal/base.py/PALChain._call_0
        └── langchain/chains/loading.py/_load_pal_chain_0

[+] Current initial file: langchain/prompts/loading.py
[DEBUG] ---->  langchain/prompts/loading.py
exec
└── langchain/prompts/loading.py/_load_prompt_from_file_0
    └── langchain/prompts/loading.py/load_prompt_0
        └── langchain/prompts/loading.py/_load_few_shot_prompt_0

[+] Current initial file: langchain/graphs/hugegraph.py
eval
[+] Current initial file: langchain/tools/python/tool.py
[INFO] implicit function:  langchain/tools/python/tool.py/PythonAstREPLTool._run_0
[DEBUG] ---->  langchain/tools/__init__.py
[DEBUG] ---->  langchain/tools/python/tool.py
[DEBUG] ---->  langchain/agents/agent_toolkits/spark/base.py
[DEBUG] ---->  langchain/agents/agent_toolkits/pandas/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/spark/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/agent_toolkits/pandas/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/agent_toolkits/pandas/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/agent_toolkits/pandas/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/agent_toolkits/pandas/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/spark/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
[DEBUG] ---->  langchain/agents/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/__init__.py
[DEBUG] ---->  langchain/agents/agent_toolkits/csv/base.py
eval
└── langchain/tools/python/tool.py/PythonAstREPLTool._run_0
    ├── langchain/agents/agent_toolkits/pandas/base.py/_get_functions_multi_prompt_0
    │   └── langchain/agents/agent_toolkits/pandas/base.py/_get_functions_prompt_and_tools_1
    │       └── langchain/agents/agent_toolkits/pandas/base.py/create_pandas_dataframe_agent_3
    ├── langchain/agents/agent_toolkits/pandas/base.py/_get_functions_single_prompt_0
    │   └── langchain/agents/agent_toolkits/pandas/base.py/_get_functions_prompt_and_tools_0
    │       └── langchain/agents/agent_toolkits/pandas/base.py/create_pandas_dataframe_agent_2
    ├── langchain/agents/agent_toolkits/pandas/base.py/_get_multi_prompt_0
    │   └── langchain/agents/agent_toolkits/pandas/base.py/_get_prompt_and_tools_0
    │       └── langchain/agents/agent_toolkits/pandas/base.py/create_pandas_dataframe_agent_0
    │           └── langchain/agents/agent_toolkits/csv/base.py/create_csv_agent_0
    ├── langchain/agents/agent_toolkits/pandas/base.py/_get_single_prompt_0
    │   └── langchain/agents/agent_toolkits/pandas/base.py/_get_prompt_and_tools_1
    │       └── langchain/agents/agent_toolkits/pandas/base.py/create_pandas_dataframe_agent_1
    └── langchain/agents/agent_toolkits/spark/base.py/create_spark_dataframe_agent_0

[+] Current initial file: langchain/chains/flare/base.py
subprocess.run
[+] Current initial file: langchain/utilities/bash.py
[INFO] implicit function:  langchain/utilities/bash.py/BashProcess.run_0
[DEBUG] ---->  langchain/tools/shell/tool.py
[DEBUG] ---->  langchain/utilities/bash.py
[DEBUG] ---->  langchain/utilities/__init__.py
[DEBUG] ---->  langchain/chains/llm_bash/base.py
[DEBUG] ---->  langchain/tools/shell/tool.py
subprocess.run
└── langchain/utilities/bash.py/BashProcess._run_0
    └── langchain/utilities/bash.py/BashProcess.run_0
        └── langchain/tools/shell/tool.py/_get_default_bash_processs_0

[+] Current initial file: langchain/llms/beam.py
[INFO] implicit function:  langchain/llms/beam.py/Beam._deploy_0
[DEBUG] ---->  langchain/llms/__init__.py
[DEBUG] ---->  langchain/llms/beam.py
[DEBUG] ---->  langchain/llms/beam.py
subprocess.run
├── langchain/llms/beam.py/Beam._deploy_0
└── langchain/llms/beam.py/_deploy_0

[RESULT]: --------> langchain
--------------------------------------------------
[TOTAL] Total time costs: 5.527137994766235
[TOTAL] Total call chain: 15
--------------------------------------------------
[TOTAL] Total number of cross file: 30
[AVG] Average cross file number: 2.0
[MAX] Max cross file number: 3
--------------------------------------------------
[TOTAL] Total call chain length: 64
[AVG] Average call chain length: 4.266666666666667
[MAX] Max call chain length: 6
--------------------------------------------------
[*] Implicit call number: 5
```

```
llamaindex:
➜  scanner orgpy chain_paper.py --package=llama_index --dir='./llama_index_0.7.13'                                                       
exec
[+] Current initial file: llama_index/program/predefined/evaporate/extractor.py
[DEBUG] ---->  llama_index/program/predefined/evaporate/extractor.py
exec
└── llama_index/program/predefined/evaporate/extractor.py/run_fn_on_nodes_0
    └── llama_index/program/predefined/evaporate/extractor.py/extract_datapoints_with_fn_0

[+] Current initial file: llama_index/query_engine/pandas_query_engine.py
[DEBUG] ---->  llama_index/indices/struct_store/json_query.py
[DEBUG] ---->  llama_index/query_engine/pandas_query_engine.py
exec
└── llama_index/query_engine/pandas_query_engine.py/default_output_processor_0

eval
[+] Current initial file: llama_index/indices/query/query_transform/feedback_transform.py
[+] Current initial file: llama_index/agent/react/output_parser.py
[+] Current initial file: llama_index/query_engine/pandas_query_engine.py
[DEBUG] ---->  llama_index/indices/struct_store/json_query.py
[DEBUG] ---->  llama_index/query_engine/pandas_query_engine.py
eval
└── llama_index/query_engine/pandas_query_engine.py/default_output_processor_0

subprocess.run
[RESULT]: --------> llama_index
--------------------------------------------------
[TOTAL] Total time costs: 1.1556739807128906
[TOTAL] Total call chain: 3
--------------------------------------------------
[TOTAL] Total number of cross file: 3
[AVG] Average cross file number: 1.0
[MAX] Max cross file number: 1
--------------------------------------------------
[TOTAL] Total call chain length: 7
[AVG] Average call chain length: 2.3333333333333335
[MAX] Max call chain length: 3
--------------------------------------------------
[*] Implicit call number: 0
```

```
lagent:
➜  scanner orgpy chain_paper.py --package=lagent --dir='./lagent'                                                                  
exec
[+] Current initial file: lagent/actions/python_interpreter.py
[DEBUG] ---->  lagent/actions/builtin_actions.py
[DEBUG] ---->  lagent/actions/base_action.py
[DEBUG] ---->  lagent/actions/google_search.py
[DEBUG] ---->  lagent/actions/action_executor.py
[DEBUG] ---->  lagent/actions/llm_qa.py
[DEBUG] ---->  lagent/actions/python_interpreter.py
[DEBUG] ---->  lagent/actions/builtin_actions.py
[DEBUG] ---->  lagent/actions/base_action.py
[DEBUG] ---->  lagent/actions/google_search.py
[DEBUG] ---->  lagent/actions/action_executor.py
[DEBUG] ---->  lagent/actions/llm_qa.py
[DEBUG] ---->  lagent/actions/python_interpreter.py
[DEBUG] ---->  lagent/actions/builtin_actions.py
[DEBUG] ---->  lagent/actions/base_action.py
[DEBUG] ---->  lagent/actions/google_search.py
[DEBUG] ---->  lagent/actions/action_executor.py
[DEBUG] ---->  lagent/actions/llm_qa.py
[DEBUG] ---->  lagent/actions/python_interpreter.py
[DEBUG] ---->  lagent/agents/react.py
[DEBUG] ---->  lagent/agents/autogpt.py
[DEBUG] ---->  lagent/agents/rewoo.py
[DEBUG] ---->  lagent/actions/base_action.py
[DEBUG] ---->  lagent/actions/action_executor.py
[DEBUG] ---->  lagent/actions/python_interpreter.py
[DEBUG] ---->  lagent/llms/huggingface.py
[DEBUG] ---->  lagent/actions/builtin_actions.py
[DEBUG] ---->  lagent/actions/base_action.py
[DEBUG] ---->  lagent/actions/google_search.py
[DEBUG] ---->  lagent/actions/action_executor.py
[DEBUG] ---->  lagent/actions/llm_qa.py
[DEBUG] ---->  lagent/actions/python_interpreter.py
[DEBUG] ---->  lagent/actions/builtin_actions.py
[DEBUG] ---->  lagent/actions/base_action.py
[DEBUG] ---->  lagent/actions/google_search.py
[DEBUG] ---->  lagent/actions/action_executor.py
[DEBUG] ---->  lagent/actions/llm_qa.py
[DEBUG] ---->  lagent/actions/python_interpreter.py
exec
└── lagent/actions/python_interpreter.py/exec_code_0
    ├── lagent/actions/python_interpreter.py/__init___0
    │   └── lagent/actions/python_interpreter.py/__call___0
    │       └── lagent/actions/base_action.py/run_0
    │           └── lagent/actions/action_executor.py/__call___1
    └── lagent/actions/python_interpreter.py/_call_0

eval
[+] Current initial file: lagent/agents/autogpt.py
[+] Current initial file: lagent/actions/python_interpreter.py
[DEBUG] ---->  lagent/actions/builtin_actions.py
[DEBUG] ---->  lagent/actions/base_action.py
[DEBUG] ---->  lagent/actions/google_search.py
[DEBUG] ---->  lagent/actions/action_executor.py
[DEBUG] ---->  lagent/actions/llm_qa.py
[DEBUG] ---->  lagent/actions/python_interpreter.py
eval
└── lagent/actions/python_interpreter.py/eval_code_0
    └── lagent/actions/python_interpreter.py/_call_0

[+] Current initial file: lagent/llms/huggingface.py
subprocess.run
[RESULT]: --------> lagent
--------------------------------------------------
[TOTAL] Total time costs: 2.3270230293273926
[TOTAL] Total call chain: 3
--------------------------------------------------
[TOTAL] Total number of cross file: 5
[AVG] Average cross file number: 1.6666666666666667
[MAX] Max cross file number: 3
--------------------------------------------------
[TOTAL] Total call chain length: 12
[AVG] Average call chain length: 4.0
[MAX] Max call chain length: 6
--------------------------------------------------
[*] Implicit call number: 0
```

```
griptape:
➜  scanner orgpy chain_paper.py --package=griptape --dir='./griptape'    
exec
[+] Current initial file: griptape/utils/python_runner.py
[DEBUG] ---->  griptape/tools/calculator/tool.py
[DEBUG] ---->  griptape/utils/python_runner.py
[DEBUG] ---->  griptape/utils/__init__.py
[DEBUG] ---->  griptape/tools/calculator/tool.py
exec
└── griptape/utils/python_runner.py/PythonRunner.run_0
    └── griptape/tools/calculator/tool.py/calculate_0

eval
[+] Current initial file: griptape/utils/python_runner.py
[DEBUG] ---->  griptape/tools/calculator/tool.py
[DEBUG] ---->  griptape/utils/python_runner.py
[DEBUG] ---->  griptape/utils/__init__.py
[DEBUG] ---->  griptape/tools/calculator/tool.py
eval
└── griptape/utils/python_runner.py/PythonRunner.run_0
    └── griptape/tools/calculator/tool.py/calculate_0

subprocess.run
[+] Current initial file: griptape/tools/base_tool.py
[DEBUG] ---->  griptape/tasks/toolkit_task.py
[DEBUG] ---->  griptape/tools/base_tool.py
[DEBUG] ---->  griptape/tools/computer/tool.py
[DEBUG] ---->  griptape/drivers/memory/conversation/dynamodb_conversation_memory_driver.py
[DEBUG] ---->  griptape/drivers/embedding/openai_embedding_driver.py
[DEBUG] ---->  griptape/drivers/prompt/base_multi_model_prompt_driver.py
[DEBUG] ---->  griptape/drivers/vector/pinecone_vector_store_driver.py
[DEBUG] ---->  griptape/drivers/sql/sql_driver.py
[DEBUG] ---->  griptape/memory/structure/conversation_memory.py
[DEBUG] ---->  griptape/structures/agent.py
[DEBUG] ---->  griptape/structures/structure.py
subprocess.run
└── griptape/tools/base_tool.py/install_dependencies_0
    └── griptape/tools/base_tool.py/__attrs_post_init___0

[RESULT]: --------> griptape
--------------------------------------------------
[TOTAL] Total time costs: 2.7314350605010986
[TOTAL] Total call chain: 3
--------------------------------------------------
[TOTAL] Total number of cross file: 5
[AVG] Average cross file number: 1.6666666666666667
[MAX] Max cross file number: 2
--------------------------------------------------
[TOTAL] Total call chain length: 9
[AVG] Average call chain length: 3.0
[MAX] Max call chain length: 3
--------------------------------------------------
[*] Implicit call number: 0
```

```
vanna:
➜  scanner orgpy chain_develop.py --package=vanna --dir='./vanna/src'                                                               
exec
[+] Current initial file: vanna/base/base.py
[DEBUG] ---->  vanna/remote.py
[DEBUG] ---->  vanna/__init__.py
[DEBUG] ---->  vanna/flask/__init__.py
[DEBUG] ---->  vanna/flask/assets.py
[DEBUG] ---->  vanna/ZhipuAI/ZhipuAI_Chat.py
[DEBUG] ---->  vanna/vannadb/vannadb_vector.py
[DEBUG] ---->  vanna/base/base.py
exec
└── vanna/base/base.py/get_plotly_figure_0
    └── vanna/base/base.py/ask_0

eval
[RESULT]: --------> vanna
--------------------------------------------------
[TOTAL] Total time costs: 1.4105820655822754
[TOTAL] Total call chain: 1
--------------------------------------------------
[TOTAL] Total number of cross file: 1
[AVG] Average cross file number: 1.0
[MAX] Max cross file number: 1
--------------------------------------------------
[TOTAL] Total call chain length: 3
[AVG] Average call chain length: 3.0
[MAX] Max call chain length: 3
--------------------------------------------------
[*] Implicit call number: 0
```

```
metagpt:
➜  scanner orgpy chain_develop.py --package=metagpt --dir='./metagpt'  
exec
[+] Current initial file: metagpt/tools/web_browser_engine_playwright.py
[+] Current initial file: metagpt/actions/run_code.py
[DEBUG] ---->  metagpt/repo_parser.py
[DEBUG] ---->  metagpt/subscription.py
[DEBUG] ---->  metagpt/software_company.py
[DEBUG] ---->  metagpt/team.py
[DEBUG] ---->  metagpt/learn/google_search.py
[DEBUG] ---->  metagpt/tools/search_engine_ddg.py
[DEBUG] ---->  metagpt/tools/metagpt_oas3_api_svc.py
[DEBUG] ---->  metagpt/tools/search_engine_serpapi.py
[DEBUG] ---->  metagpt/tools/web_browser_engine_playwright.py
[DEBUG] ---->  metagpt/tools/search_engine.py
[DEBUG] ---->  metagpt/tools/web_browser_engine.py
[DEBUG] ---->  metagpt/tools/search_engine_serper.py
[DEBUG] ---->  metagpt/tools/tool_registry.py
[DEBUG] ---->  metagpt/tools/search_engine_googleapi.py
[DEBUG] ---->  metagpt/tools/web_browser_engine_selenium.py
[DEBUG] ---->  metagpt/tools/openapi_v3_hello.py
[DEBUG] ---->  metagpt/tools/metagpt_text_to_image.py
[DEBUG] ---->  metagpt/tools/libs/sd_engine.py
[DEBUG] ---->  metagpt/tools/libs/web_scraping.py
[DEBUG] ---->  metagpt/memory/longterm_memory.py
[DEBUG] ---->  metagpt/provider/spark_api.py
[DEBUG] ---->  metagpt/provider/postprocess/base_postprocess_plugin.py
[DEBUG] ---->  metagpt/provider/postprocess/llm_output_postprocess.py
[DEBUG] ---->  metagpt/roles/engineer.py
[DEBUG] ---->  metagpt/roles/qa_engineer.py
[DEBUG] ---->  metagpt/roles/searcher.py
[DEBUG] ---->  metagpt/roles/assistant.py
[DEBUG] ---->  metagpt/roles/role.py
[DEBUG] ---->  metagpt/roles/invoice_ocr_assistant.py
[DEBUG] ---->  metagpt/roles/tutorial_assistant.py
[DEBUG] ---->  metagpt/roles/researcher.py
[DEBUG] ---->  metagpt/roles/di/ml_engineer.py
[DEBUG] ---->  metagpt/roles/di/data_interpreter.py
[DEBUG] ---->  metagpt/utils/repair_llm_raw_output.py
[DEBUG] ---->  metagpt/utils/cost_manager.py
[DEBUG] ---->  metagpt/actions/rebuild_class_view.py
[DEBUG] ---->  metagpt/actions/rebuild_sequence_view.py
[DEBUG] ---->  metagpt/actions/write_code.py
[DEBUG] ---->  metagpt/actions/summarize_code.py
[DEBUG] ---->  metagpt/actions/research.py
[DEBUG] ---->  metagpt/actions/skill_action.py
[DEBUG] ---->  metagpt/actions/write_test.py
[DEBUG] ---->  metagpt/actions/debug_error.py
[DEBUG] ---->  metagpt/actions/design_api.py
[DEBUG] ---->  metagpt/actions/__init__.py
[DEBUG] ---->  metagpt/actions/write_review.py
[DEBUG] ---->  metagpt/actions/action.py
[DEBUG] ---->  metagpt/actions/execute_task.py
[DEBUG] ---->  metagpt/actions/write_prd.py
[DEBUG] ---->  metagpt/actions/write_docstring.py
[DEBUG] ---->  metagpt/actions/prepare_interview.py
[DEBUG] ---->  metagpt/actions/run_code.py
[DEBUG] ---->  metagpt/actions/write_code_an_draft.py
[DEBUG] ---->  metagpt/actions/talk_action.py
[DEBUG] ---->  metagpt/actions/write_tutorial.py
[DEBUG] ---->  metagpt/actions/write_prd_review.py
[DEBUG] ---->  metagpt/actions/generate_questions.py
[DEBUG] ---->  metagpt/actions/prepare_documents.py
[DEBUG] ---->  metagpt/actions/search_and_summarize.py
[DEBUG] ---->  metagpt/actions/write_code_review.py
[DEBUG] ---->  metagpt/actions/write_teaching_plan.py
[DEBUG] ---->  metagpt/actions/project_management.py
[DEBUG] ---->  metagpt/actions/action_node.py
[DEBUG] ---->  metagpt/actions/write_code_plan_and_change_an.py
[DEBUG] ---->  metagpt/actions/design_api_review.py
[DEBUG] ---->  metagpt/actions/invoice_ocr.py
[DEBUG] ---->  metagpt/actions/di/write_analysis_code.py
[DEBUG] ---->  metagpt/actions/di/write_plan.py
[DEBUG] ---->  metagpt/actions/di/ask_review.py
[DEBUG] ---->  metagpt/actions/di/execute_nb_code.py
[DEBUG] ---->  metagpt/actions/di/ml_action.py
[DEBUG] ---->  metagpt/actions/di/debug_code.py
[DEBUG] ---->  metagpt/prompts/summarize.py
[DEBUG] ---->  metagpt/environment/base_env.py
[DEBUG] ---->  metagpt/environment/android_env/android_ext_env.py
[DEBUG] ---->  metagpt/environment/werewolf_env/werewolf_env.py
[DEBUG] ---->  metagpt/environment/mincraft_env/mincraft_env.py
[DEBUG] ---->  metagpt/environment/mincraft_env/process_monitor.py
[DEBUG] ---->  metagpt/environment/mincraft_env/mincraft_ext_env.py
[DEBUG] ---->  metagpt/strategy/planner.py
exec
└── metagpt/actions/run_code.py/run_text_0
    └── metagpt/actions/run_code.py/run_0

eval
[+] Current initial file: metagpt/utils/serialize.py
[DEBUG] ---->  metagpt/schema.py
[DEBUG] ---->  metagpt/utils/serialize.py
[DEBUG] ---->  metagpt/schema.py
eval
└── metagpt/utils/serialize.py/actionoutput_str_to_mapping_0
    └── metagpt/schema.py/check_instruct_content_0

[+] Current initial file: metagpt/utils/common.py
[+] Current initial file: metagpt/actions/skill_action.py
[+] Current initial file: metagpt/strategy/tot.py
[DEBUG] ---->  metagpt/tools/azure_tts.py
[DEBUG] ---->  metagpt/roles/assistant.py
[DEBUG] ---->  metagpt/roles/role.py
[DEBUG] ---->  metagpt/actions/rebuild_class_view.py
[DEBUG] ---->  metagpt/prompts/summarize.py
[DEBUG] ---->  metagpt/prompts/metagpt_sample.py
[DEBUG] ---->  metagpt/prompts/di/write_analysis_code.py
[DEBUG] ---->  metagpt/strategy/solver.py
[DEBUG] ---->  metagpt/strategy/tot.py
[DEBUG] ---->  metagpt/tools/azure_tts.py
[DEBUG] ---->  metagpt/roles/assistant.py
[DEBUG] ---->  metagpt/roles/role.py
[DEBUG] ---->  metagpt/actions/rebuild_class_view.py
[DEBUG] ---->  metagpt/prompts/summarize.py
[DEBUG] ---->  metagpt/prompts/metagpt_sample.py
[DEBUG] ---->  metagpt/prompts/di/write_analysis_code.py
[DEBUG] ---->  metagpt/strategy/solver.py
[DEBUG] ---->  metagpt/strategy/tot.py
eval
└── metagpt/strategy/tot.py/generate_thoughts_0
    ├── metagpt/strategy/tot.py/_dfs_0
    │   └── metagpt/strategy/tot.py/solve_0
    │       └── metagpt/strategy/tot.py/solve_2
    └── metagpt/strategy/tot.py/generate_and_evaluate_nodes_0
        └── metagpt/strategy/tot.py/_bfs_build_0
            └── metagpt/strategy/tot.py/solve_1
                └── metagpt/strategy/tot.py/solve_3

[RESULT]: --------> metagpt
--------------------------------------------------
[TOTAL] Total time costs: 16.225709915161133
[TOTAL] Total call chain: 4
--------------------------------------------------
[TOTAL] Total number of cross file: 5
[AVG] Average cross file number: 1.25
[MAX] Max cross file number: 2
--------------------------------------------------
[TOTAL] Total call chain length: 17
[AVG] Average call chain length: 4.25
[MAX] Max call chain length: 6
--------------------------------------------------
[*] Implicit call number: 0
```
