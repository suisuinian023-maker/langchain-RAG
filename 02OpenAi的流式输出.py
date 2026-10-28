import os
from xmlrpc import client

from openai import OpenAI
from openai.types import completion
from openai.types.vector_store_search_response import Content

client = OpenAI(
    base_url="http://localhost:11434/v1"
)
completion = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[
        {"role": "system", "content": "你是一个pyhome专家 话特别多"},  # 定义模型的行为和规则
        {"role": "assistant", "content": "好的我是编程专家并且话特别多"},  # 设定模型的回答由用户决定
        {"role": "user", "content": "你是谁，能做什么？"},  # 用户的提问
    ],
    stream=True  # 开启流式的输出
)
for chunk in completion:
    print(chunk.choices[0]
          .delta.content, end="",  # 每一段之间一空格分隔
          flush=True  # 立刻刷新缓冲区
          )
