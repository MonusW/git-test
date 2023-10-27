import openai
import os

# 只需要在python里设置代理即可
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

openai.api_key = ''


def test_openai(string):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": string}]
    )
    return completion['choices'][0]['message']['content'].strip()

ans = test_openai("用C语言实现快速排序")

print(ans)
