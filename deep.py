from openai import OpenAI
a=input("Enter the text: ")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
  
  )
completion = client.chat.completions.create(

  model="deepseek/deepseek-r1:free",
  messages=[
    {
      "role": "user",
  
      "content": "{}".format(a)
    }
  ]
)

print(completion.choices[0].message.content)
