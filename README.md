
Setup of VSCode, Git, Python, GitHub Copilot
Go checkout this setup guide for setting VSCode, Git, Python and GitHub Copilot (installing and sign in).

Generating Groq API keys
Sign-up for a Groq Cloud account - console.groq.com
Log in to the groq console. 
<img width="1439" height="738" alt="groq_console" src="https://github.com/user-attachments/assets/d6ff5e07-6219-4550-8246-100ddaca491f" />


On the right side navigation panel, click on API Keys
Click on Create API Key, give a name and generate the API key.
Make sure to save/store the API Key somewhere safe, cause you won't be able to copy or view the api key after that.
It'll give you the entire env variables with value copy and paste it in your .env file.
To know the available models and details about them checkout - model docs

Generating Langsmith API keys
Sign-up for a Langsmith account - langsmith.com
Log in to the langsmith. alt text
Click on Set up tracing
Click on generate api key and copy configure environment section. Langsmith Trace Project setup
Create a .env file (if it's not already present), this should be present in the root of your project folder.
Paste the configure environment variables that you copied in step 4, without the export keyword. Also remove the OPENAI_API_KEY variable in the .env (only use when you have a key from OpenAI). So what you paste in your .env file will look somewhat similar to what's shown below:
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=lsv2_pt_505038....
LANGSMITH_PROJECT=pr-standard-gift-77
To start viewing the traces
Now you can run your python script, just make sure after pasting you kill all the terminal and start the terminal. Run the python script, once you get the llm response. You can go back to langsmith console,

under the tracing projects
select the project for which you saved in .env
you'll be able to see the llm call made and the response
alt text

Validation Steps & Troubleshooting
1. VSCode
Validation Command:

code --version
Success: Shows VSCode version. If Error:

Ensure VSCode is installed.
If code is not found, add VSCode to your PATH (see Command Palette > "Shell Command: Install 'code' command in PATH").
2. Git
Validation Command:

git --version
Success: Shows Git version. If Error:

Install Git from git-scm.com.
If installed but not found, check your PATH variable.
3. Python
Validation Command:

python --version
or

python3 --version
Success: Shows Python version (preferably 3.x). If Error:

Download and install Python from python.org.
If wrong version, update Python.
If not found, check your PATH variable.
4. GitHub Copilot
Validation Steps:

In VSCode, go to Extensions and search for "GitHub Copilot".
Ensure it is installed and enabled.
Sign in with your GitHub account.
Validation Command:

Open the Copilot Chat panel (View > Copilot > Chat).
Send a sample query, such as:
 How do I write a Python function to add two numbers?
If Copilot responds with a code suggestion or answer, it is working.
If Error:

Make sure you are signed in to GitHub.
Check your internet connection.
If extension is missing, install from VSCode Extensions Marketplace.
If chat panel does not respond, reload VSCode or reinstall the extension.
Step-by-Step Project Setup for Beginners (Windows-first, Mac/Linux in brackets)
1. Create a Folder for Your Project
Right-click on your Desktop or in File Explorer and choose New > Folder.
Name it (e.g., my_python_project).
Open this folder.
2. Open VSCode and Select Your Project Folder
Open VSCode from your Start Menu.
Click File > Open Folder...
Select your project folder and click Select Folder. (Mac: VSCode > File > Open...)
You should see your folder name in the VSCode sidebar.
3. Verify GitHub Copilot (GHCP) is Working
In VSCode, click View > Copilot > Chat.
In the chat panel, type a question (e.g., "How do I write a Python function to add two numbers?") and press Enter.
If Copilot responds, it's working.
If not, check you are signed in to GitHub and Copilot is installed (see Extensions sidebar).
4. Switch to Agent Mode
In Copilot Chat panel, below the input box you'll see a drop down that'll have one of the following written - "Ask", "Agent", "Edits". You can click on the drop-down and select "Agent" if it's not already in that mode OR You can use keyboard shortcuts Ctrl + Shift + I (for Mac: Command + Shift + I) to open GHCP in Agent mode.
Look for a message or indicator that agent mode is active. Check the screenshot below:
alt text

Set default terminal to git bash
Ctrl + Shift + P and then type Terminal: Select Default Profile as you type it'll suggest the command. Click on it.
You'll be able to see all the terminal you can use - git bash, cmd, powershell, etc.
Set git bash as your default terminal.
5. Prompt GHCP Agent Mode to create simple langchain application
In Copilot Chat (Agent Mode), describe what you want your Python app to do.
Sample Prompt:
Create a simple python terminal application that has a chat based (user query and response) flow using langchain and langchain-groq library for building this application. 
The api keys for llm and model name should come from a config file, use dotenv where needed to load the env variables.
Create requirements.txt file with the libraries needed for the application
Copilot will suggest code file, config and a requirements.txt file.
Note: This is based on above prompt, files or structure can be different

Prompting guideline

Always write clear and specific instructions with all required context.
In case of complex use case, break down the task and prompt one task at a time.
You can also feed the errors to ghcp to fix the errors.
In case you are stuck or not getting the right response. You can checkout the code and config file in the Langchain folder -

chat_terminal.py
config.py
requiremets.txt
6. Create a Python Virtual Environment (venv)
In VSCode, open a new terminal (View > Terminal).
Type:
python -m venv venv
(Mac/Linux: use python3 -m venv venv)
You should see a new folder called venv in your project.
7. Activate the Virtual Environment
In the terminal (git bash), type:

source venv/Scripts/activate
Cmd -

venv\Scripts\activate
Powershell -

venv\Scripts\Activate.ps1
(Mac/Linux: source venv/bin/activate)

Your terminal prompt should now start with (venv).

alt text

8. Install Required Libraries from requirements.txt
Make sure requirements.txt is in your project folder. And in terminal as well you are in your project folder path. Type pwd in the terminal to verify, you are in the root folder inside which the requirements.txt file is present.

In the terminal, type:

pip install -r requirements.txt
(Mac/Linux: use pip3 if needed)

Alternatively, you can install single packages or libraries using -

pip install packageName
in place of packageName the actual name of the package should be present.

Note: You can find packages from pypi website, or in your browser type the package name and add pypi the first result should take you to the right place. You can copy paste the intall command directly from the site.

You should see messages that packages are being installed.

To check, type:

pip list
(Mac/Linux: use pip3 list)

9. Set Python Interpreter in VSCode
In VSCode, press Ctrl+Shift+P (Mac: Cmd+Shift+P).
Type Python: Select Interpreter and select it.
Choose the interpreter that shows your project folder and venv.
You should see the selected interpreter at the bottom left of VSCode.
10. Run Your Python Application
In VSCode, open your main Python file (e.g., main.py).
Click the green Run button at the top right, or right-click in the editor and choose Run Python File in Terminal.
You should see the output in the terminal below.
If there are errors, check the terminal messages for hints.
11. Troubleshooting
In case you run into some issues, examine the error message and try to troubleshoot.
If that doesn't work, tap in your trusty sidekick - Claude.ai
Enter a prompt like this
Debug issues in my code

## My code
{Paste your code here - don't put in apikeys/secrets though}


## Error in terminal
{Paste the actual error from terminal/command prompt here}
Try out the recommendations from Claude.
Objective
The main objective is for you to be able to send a request to the llm in the form of generic questions and you are able to get responses on your terminal, and also to check how it gets traced on langsmith to gain insights and metrics on your application.

Sample qns to verify output
Note: The qn and response should also be present in your langsmith project configured.

What's the capital of India? Ans. Capital of India is Delhi

Explain OOPs concepts? Ans. Object-Oriented Programming (OOP) Concepts ==============================================

Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of objects and classes. It provides a way to design, organize, and structure code in a modular and reusable manner. ....

Please note: if you ask qns based on realtime eg. What's the time now? or what's the weather in Pune?. You'll get incorrect responses since the LLM's have a knowledge cutoff date, it can only respond based on the data it was trained on.# LangChain-LLM
This repository contains simple python application that uses Langchain &amp; Groq to make a simple LLM call and returns the response. There should be a Question asked to the user on the CLI. And the response should be returned on the CLI. This should continue happening in a loop.
