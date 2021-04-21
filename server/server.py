from flask import Flask, request, Response
from flask_cors import CORS
from flask import jsonify
import time
import re
import os
import openai

'''
    @hackathon
    @date: 4/21
'''

app = Flask(__name__)
CORS(app)

openai.api_key = ""

# POST method which sends the user input through OpenAI's 
# GPT-3 API. Then the API response gets cleaned by
# by format_response() and sent to the front-end.
@app.route('/', methods=['POST'])
def get_query():
    data = request.get_json()
    str_data = str(data["doctorInput"])
    base_prompt = "Please convert each of the following Medical Records into Simple Versions that patients can easily understand:\n\nMedical Record 1: \nYou have the possibility of coronary artery disease, which may require pharmacological treatment or some intervention, which can be of different types.\nSimple Version for Patient 1: \nYou have a chance of having a heart problem, and we have to do something about it.\n###\nMedical Record 2:  \nThe dose and treatment schedule (how often you have the drug or treatment) and the combination of treatments you have also affect what side effects you might experience. Side effects also vary in how severe they are: some people have mild side effects while others have more troublesome effects. Even when side effects are listed as 'common', it doesn't mean that everyone gets them.\nSimple Version for Patient 2: \nThe dose and treatment schedule and the combination of treatments you have also affect how bad a side effect you are going to have. Not everyone has a bad side effect even when it is listed as 'common'.\n###\nMedical Record 3: \nSlow healing DM ulcer on left medial metatarsal head, surgically debrided during hospitalization.\nSimple Version for Patient 3:\nThe doctor took out a small amount of bad skin on your foot when you were in the hospital, but it won't heal as fast as usual because you have diabetes.\n###\n"
    new_prompt = str_data + "\n"
    new_prompt = base_prompt + new_prompt
    print(new_prompt)
    response = openai.Completion.create(
      engine="davinci",
      prompt=new_prompt,
      temperature=0.40,
      max_tokens=120,
      top_p=1,
      frequency_penalty=0.20,
      presence_penalty=0,
      stop=["###"]
)
    str_response = str(response['choices'][0].text)
    str_response = format_response(str_response)
    
    print(str_response)
    return str_response

# Cleans the GPT-3 API response to remove duplicate
# outputs.
def format_response(response):
    simple_index = [m.start() for m in re.finditer('Simple', response)]
    if len(simple_index) > 1:
        response = response[0:simple_index[1]]
    print(simple_index)
    return response

'''
 #How to ping the GPT3 API and return the response as a string

 response = openai.Completion.create(
      engine="davinci",
      prompt="These are examples of products which have a product name, a short description, and a long description.\n\nProduct Name:Flipp\nShort Description:Instantaneous printing from your smartphone. Share and print photos instantly with a single click.\nLong Description:With Flipp, printing photos is now so simple, all you need to do is select the photos you want to print, which quantity of photos you want printed, and then pick up a nearby Flipp printer. With Flipp's revolutionary printing technology, there's no ink and no paper. Simply go to your local participating retail store, grab a nearby printer and place your order – all within seconds. Plus, there's no ink or paper to clutter up your home or office – keep it clean, neat and clutter-free! After ordering your photos from Flipp, they'll be ready in just minutes – hot off the press.\n###\nProduct Name:Zookso\nShort Description:The ultra-portable wireless speaker with powerful bass and crystal clear sound.\nLong Description:Zookso was designed to deliver a world class listening experience for music fans on the go. It delivers crystal clear highs and deep, rumbling lows in a waterproof, compact package that's as small as a can of soda. The Zookso Bluetooth Speaker is powered by a rechargeable battery that lasts up to 8 hours on a single charge and is even compatible with most devices' USB ports!\n###\nProduct Name:BonSano\nShort Description BonSano makes healthy food delicious so you can feed your child without guilt.\nLong Description:By combining all the proven nutrition of breast milk and baby food with the convenience of a toddler's favorite snacks, BonSano gives parents a tasty, healthy alternative to conventional snacks and meals that is pro-biotic enriched, kosher certified, gluten free and vegan friendly. With ingredients your child will love and no high-fructose corn syrup or artificial colors or flavors, BonSano is good for your child and good for you!\n###\nProduct Name:NoSandy\nShort Description:This is a sun umbrella for adults.\nLong Description:NoSandy is the world's first umbrella specifically designed to protect you against sand and dust when desert hiking, trekking and camping. Instead of a cloth canopy like other beach umbrellas, ours is made with a durable mesh material that safeguards you from the elements yet allows moisture to escape so it does not condense on the inside of its polyester canopy. With a sturdy aluminum pole and frame covered with soft plastic grips in unique camo patterns, it can be used as both an umbrella and a walking stick. Plus, its compact size (16 inches when closed) makes it easy to take along on any outdoor adventure!\n###\n",
      temperature=0.8,
      max_tokens=266,
      top_p=1,
      frequency_penalty=0.68,
      presence_penalty=0,
      stream=True,
      stop=["###"]
    )

    return str(response['choices'][0].text)
'''


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=False)
