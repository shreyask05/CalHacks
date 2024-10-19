# main.py

from actionList import get_actionlist, print_ActionList, split_text
from pydantic import ValidationError

context_path = "/fixtures/page_source.html"

# Read the HTML file
with open(context_path, 'r', encoding='utf-8', errors='replace') as file:
    html_string = file.read()

# Split the context into smaller parts to avoid exceeding the input length
chunked_context = split_text(html_string, 5000)  # Adjust max_length based on API limits

# Groq client setup
client = Groq(
    api_key="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",
)


# Get and print the Action List
try:
    webapp = get_actionlist("some-webapp-name")  # Ensure correct argument
    print_ActionList(webapp)
except ValidationError as e:
    print(f"ValidationError: {e}")

