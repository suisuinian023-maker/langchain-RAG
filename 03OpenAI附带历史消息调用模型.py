from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1"
)
completion = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[
        {"role": "system", "content": "你是一个pyhome专家 回答很简洁"},  # 定义模型的行为和规则
        {"role": "user", "content": "小红有两只狗"},
        {"role": "assistant", "content": "好的"},  # 设定模型的回答由用户决定
        {"role": "user", "content": "小刚有五只狗"},
        {"role": "assistant", "content": "好的"},  # 设定模型的回答由用户决定
        {"role": "user", "content": "总共有几只狗"},  # 用户的提问
    ],
    stream=True  # 开启流式的输出
)
for chunk in completion:
    print(chunk.choices[0]
          .delta.content, end="",  # 每一段之间一空格分隔
          flush=True  # 立刻刷新缓冲区
          )
