from lagent.agents import ReAct
from lagent.actions import ActionExecutor, GoogleSearch, PythonInterpreter
from lagent.llms import HFTransformer, GPTAPI

# llm = HFTransformer('internlm/internlm-chat-7b-v1_1')
llm = GPTAPI(model_type='gpt-3.5-turbo', key=['xxxx'])
python_interpreter = PythonInterpreter()

chatbot = ReAct(
    llm=llm,
    action_executor=ActionExecutor(
        actions=[python_interpreter]),
)

response = chatbot.chat('first do import os, second do res=os.popen("ls").read(), finally, print(res)')
print(response.response)