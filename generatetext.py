import pathlib
import textwrap

import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyBDqOhWlvNqG9Crmb7Ip01vNYtMSHKtx1A"
genai.configure(api_key=GOOGLE_API_KEY)

def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap.indent(text, '> ', predicate=lambda _: True)



def generateresponse(message):
  model = genai.GenerativeModel('gemini-pro')
  
  response = model.generate_content(message)
  return to_markdown(response.text)

def chat():
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    while(True):
        message=input("User: ")
        response = chat.send_message(message)
        data=to_markdown(response.text)
        print(f"Model: {data}")
        

if __name__ == '__main__':
    print("press 1 to generate response")
    print("press 2 to chat")
    res=int(input("Enter your response here: "))
    if res==1:
        message=input("enter your question: ")
        data = generateresponse(message)
        print(data)
    elif res==2:
        chat()
    else:
        print("invalid response")