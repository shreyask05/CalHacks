import json
import requests
import os
from groq import Groq
from pydantic import BaseModel, ValidationError


class Action(BaseModel):
    action_name: str
    description: str

class ActionList(BaseModel):
    webapp: str
    actions: list[Action]    

# context_path = "APP.html"
# with open(context_path, 'r', encoding='utf-8', errors='replace') as file:
#     html_string = file.read()

def split_text(text: str, max_length: int) -> list[str]:
    """Splits the input text into chunks of specified maximum length."""
    # Split the text into words
    words = text.split()
    chunks = []
    current_chunk = ""

    for word in words:
        # Check if adding the next word would exceed the max length
        if len(current_chunk) + len(word) + 1 <= max_length:  # +1 for the space
            if current_chunk:  # If not the first word, add a space
                current_chunk += " "
            current_chunk += word
        else:
            # Add the current chunk to the list and start a new chunk
            chunks.append(current_chunk)
            current_chunk = word  # Start new chunk with the current word

    # Add the last chunk if there is any content left
    if current_chunk:
        chunks.append(current_chunk)

    return chunks

# Split the context into smaller parts to avoid exceeding the input length
#chunked_context = split_text(html_string, 5000)  # Adjust the max_length based on your API's limits

client = Groq(
    api_key="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",
)
def get_actionlist(chunked_context) -> ActionList:
    if os.path.exists('log.json'):
        os.remove('log.json')
    f = open("log.json", "a")
    # Loop through each chunk of the context
    for chunk in chunked_context:
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an Action List database that outputs Action Lists in JSON. Action Lists are composed of 3 actions a user would perform on the website. Actions are strictly goal-oriented, succinct, and relating to the user's experience. Each Action must be separated by a comma. Output absolutely nothing else except the list of actions.",
                    # f"The JSON object must use the schema: {json.dumps(ActionList.model_json_schema(), indent=2)}",
                },
                {
                    "role": "user",
                    "content": f"Fetch an Action List for: {chunk}",
                }, ],
            model="llama3-8b-8192",
            temperature=0, 
            stream=False,
            # response_format= {"type": "json_object"},
        )

        result = {}
        result['items'] = []
        for item in chat_completion.choices[0].message.content[1 : -1].split(','):
            result['items'].append({
                "description" : item,
            })
        json.dump(result, f, indent=4)
        # f.write(str(result))
        f.close()

        return
        # Validate and return the Action List for this chunk
        # return ActionList.model_validate_json(chat_completion.choices[0].message.content)

def print_ActionList(actionlist: ActionList):
    print("Action List", actionlist.webapp)
    print("\nActions:")
