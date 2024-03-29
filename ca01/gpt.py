'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def get_pokemon_team(self, prompt, type):
        ''' Generate a GPT response for their balanced pokemon team based around their favorite type'''
        pre_prompt = "You will help me find the best balanced pokemon team centered around my favorite type. List them all logically including their stats, natures, and items. "
        type_prompt = "My favorite type is " + type + "."
        completion = openai.Completion.create(
            engine = self.model_engine,
            prompt = pre_prompt + prompt + type_prompt,
            max_tokens = 1024,
            n = 1,
            stop = None,
            temperature = 0.8
        )

        response = completion.choices[0].text
        return response
    
    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

    def poeminator(self, adjs):
        
        pre_prompt = "Make a poem that is "
        completion = openai.Completion.create(
            engine = self.model_engine,
            prompt = pre_prompt + adjs,
            max_tokens = 1024,
            n = 1,
            stop = None,
            temperature = 0.8
        )

        response = completion.choices[0].text
        return response

if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))