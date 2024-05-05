"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import csv
import re
from backend import fit
from backend import backend


genai.configure(api_key="AIzaSyCnGQXDYajtgIrxlSSxdCmnGKxhn_62J6U")


# Global declaration
# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# convo = model.start_chat(history=[
# ])
# convo.send_message("What architectures are used in Gemini and ChatGPT?")
# print(convo.last.text)

age = 0
bmi = 0
health_advice = ""

def rec_param(age, bmi, ha):
    age = age
    bmi = bmi
    health_advice = ha


def prompt(age, bmi, health_advice):
    # start_time = time.time()
    steps, calorie = fit.fit_track()
    messages_chatgpt=[{"role": "system", "content":'''You are an health advisor. You need to give
                       health advice to a person based on their BMI and age. The answer you should generate
                       should contain the following information:
                        1. Give a heading 'Health Report : ' and then under that give about their BMI,
                        steps and calories burnt today. Then explain about the health condition, 
                       based on thei BMI whether the person is healthy or not.
                        Also briefly explain their health condition and softly so that they couldnot 
                       get their feelings hurt.
                        2. Give a heading 'Measures to be taken : ' and then under that give the 
                       measures to be taken based on their health condition. Like what need to be 
                       done to be healthy, based on their BMI.
                        3. Give a heading 'Food diet to be followed : ' and consider 
                       the person is from India, give indian food diet for that person for balanced food diet 
                       for healthy and fitness
                        4. Give a heading 'Workouts to be done : ' and give suitable workouts 
                       for the person to loss weight who are overweight/ obese and gain weight 
                       for those who are Underweight.
                        5. At last give them motivation for the person that they should spend time
                        on their body and mind to be healthy.'''},
                  {"role": "user", "content": f"{{'steps': {steps}, 'calories': {calorie}, 'age': {age}, 'bmi': {bmi}, 'bmi_result': '{health_advice}'}}"}
 ]
    def transform_to_gemini(messages_chatgpt):
        messages_gemini = []
        system_promt = ''
        for message in messages_chatgpt:
            if message['role'] == 'system':
                system_promt = message['content']
            elif message['role'] == 'user':
                messages_gemini.append({'role': 'user', 'parts': [message['content']]})
            elif message['role'] == 'assistant':
                messages_gemini.append({'role': 'model', 'parts': [message['content']]})
        if system_promt:
            messages_gemini[0]['parts'].insert(0, f"*{system_promt}*")

        return messages_gemini
    messages = transform_to_gemini(messages_chatgpt)
    response = model.generate_content(messages)
    print(response.text)
    response_text = response.text
    # response_text = re.sub(r'\*', '', response.text)
    backend.report_card(response_text, bmi, health_advice, steps, calorie)
    print(response_text)
    