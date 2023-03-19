'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>CS103 Team 37 GPT Demo</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <br>  
        <a href="{url_for('pokemonteam')}">Find the best pokemon team </a>
        <br>
        <a href="{url_for('team')}"> About CS103 Team 37 </a> 

    '''

@app.route('/team')
def team():
    ''' Displays all team members and their bios'''
    return f'''
        <h1> CS103 Team 37 </h1>
        <h3> Marco Borja </h3>
        <a> Marco is a Physics Major and Computer Science Minor. He coded the pokemon team generator page. And set up the /team, and /pokemonteam_about pages. </a>
        <a href="{url_for('pokemonteam')}"> Pokemon Team Generator </a>
        <h3> Noah Goble </h3>
        
        <h3> Alice Zeng </h3>
        
        <br>
        <a href={url_for('index')}>Return to main menu</a>
    '''

@app.route('/pokemonteam_about')
def pokemon_team_about():
    ''' Display about pokemon team'''
    return f'''
        <h1> About the pokemon team generator </h1>
        <a> This generates a personalized pokemon team around your favorite type. You can also add your personal preferences as well. </a>
        <br>
        <br>
        <a href={url_for('index')}>Return to main menu</a>
        <br>
        <a href="{url_for('pokemonteam')}"> Return to team generation </a>
    '''
@app.route('/pokemonteam', methods=['GET','POST'])
def pokemonteam():
    '''
        Handle the get request for a balanced pokemon team
        and post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        type = request.form['favetype']
        prompt = prompt
        answer = gptAPI.get_pokemon_team(prompt,type)
        return f'''
        <h1>Generated Pokemon Team</h1>
        <pre>Here is your generated pokemon team based around {type} type pokemon </pre>
        <pre style="bgcolor:yellow">Additional information: {prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('pokemonteam')}> make another query</a>
        <br>
        <br>
        <a href={url_for('index')}>Return to main menu</a>
        <br>
        <a href={url_for('pokemon_team_about')}> About</a>
        '''
    else:
        return f'''
        <h1>Personalized Pokemon Team Finder</h1>
        <form method="post">
            <label for="favetype">Select your favorite pokemon type</label>
            <select name="favetype" id="type">
            <option value="normal" selected>Normal</option>
            <option value="fire">Fire</option>
            <option value="water">Water</option>
            <option value="grass">Grass</option>
            <option value="electric">Electric</option>
            <option value="ice">Ice</option>
            <option value="fighting">Fighting</option>
            <option value="poison">Poison</option>
            <option value="ground">Ground</option>
            <option value="flying">Flying</option>
            <option value="pyschic">Psychic</option>
            <option value="bug">Bug</option>
            <option value="rock">Rock</option>
            <option value="ghost">Ghost</option>
            <option value="dark">Dark</option>
            <option value="dragon">Dragon</option>
            <option value="steel">Steel</option>
            <option value="fairy">Fairy</option>
            </select>
            <br>
            <br>
            Enter additional information about your balanced pokemon (ie. favorite pokemon, playstyle)
            <br>
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
            <br>
            <br>
            <a href={url_for('index')}>Return to main menu</a>
            <br>
            <a href={url_for('pokemon_team_about')}> About</a>
        </form>
        '''

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        <br>
        <br>
        <a href={url_for('index')}>Return to main menu</a>
        <br>
        '''
    else:
        return f'''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        <a href={url_for('index')}>Return to main menu</a>
        <br>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)