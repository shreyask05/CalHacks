# main.py

from CalHacks.actionList import get_actionlist, print_ActionList, split_text
from pydantic import ValidationError
from lavague.core import WorldModel, ActionEngine
from lavague.core.agents import WebAgent
from lavague.drivers.selenium import SeleniumDriver
from lavague.contexts.gemini import GeminiContext
import json
import os
from dotenv import load_dotenv, find_dotenv
import concurrent.futures
import time

def UXENGINE(url):
    print("we made it to groq")
    load_dotenv(find_dotenv())

    context_path = "APP.html"

    # Read the HTML file
    with open(context_path, 'r', encoding='utf-8', errors='replace') as file:
        html_string = file.read()

    # Split the context into smaller parts to avoid exceeding the input length
    chunked_context = split_text(html_string, 5000)  # Adjust max_length based on API limits


    # Get and print the Action List
    try:
        get_actionlist(chunked_context)  # Ensure correct argument
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
    agent.get(url)
    
    def run_agent(description):
        agent.run(description)
    
    for item in groq_output_json['items']:
        print("---------------SWARM ACTIVATED--------------------------\n")
        agent.run(item["description"])

    # for item in groq_output_json['items']:
    #     description = item["description"]
    #     with concurrent.futures.ThreadPoolExecutor() as executor:
    #         future = executor.submit(run_agent, description)
    #         try:
    #             # Wait for agent.run to finish, with a timeout of 20 seconds
    #             future.result(timeout=10)
    #         except concurrent.futures.TimeoutError:
    #             print(f"Skipping item due to timeout: {description}")

