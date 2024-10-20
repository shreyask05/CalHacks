# main.py

from actionList import get_actionlist, print_ActionList, split_text
from pydantic import ValidationError
from lavague.core import WorldModel, ActionEngine
from lavague.core.agents import WebAgent
from lavague.drivers.selenium import SeleniumDriver
from lavague.contexts.gemini import GeminiContext
import json
from dotenv import load_dotenv, find_dotenv

def UXENGINE():
    load_dotenv(find_dotenv())

    context_path = "./fixtures/page_source.html"

    # Read the HTML file
    with open(context_path, 'r', encoding='utf-8', errors='replace') as file:
        html_string = file.read()

    # Split the context into smaller parts to avoid exceeding the input length
    chunked_context = split_text(html_string, 5000)  # Adjust max_length based on API limits


    # Get and print the Action List
    try:
        webapp = get_actionlist("some-webapp-name")  # Ensure correct argument
        print_ActionList(webapp)
    except ValidationError as e:
        print(f"ValidationError: {e}")

    # Initialize Context
    context = GeminiContext(llm="models/gemini-1.5-pro", mm_llm="models/gemini-1.5-flash")

    selenium_driver = SeleniumDriver()

    # Build Action Engine and World Model from Context
    action_engine = ActionEngine.from_context(context=context, driver=selenium_driver)
    world_model = WorldModel.from_context(context)

    # Build agent & run query
    agent = WebAgent(world_model, action_engine)

    with open('log.json') as f:
        groq_output_json = json.load(f)
    agent.get("https://my.ucla.edu/")
    for item in groq_output_json['items']:
        agent.run(item["description"])
