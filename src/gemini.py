import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = "a890675c310938f7a44af21a68c217f19e8b1d9994336871ab5c56e417b6e1797593265a45b54254136a8421053483e735473951a7cd3c0698593217"

def generate_text(prompt):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,   

    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  return response.choices[0].text.strip() 

