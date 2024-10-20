import numpy as np
np.float_ = np.float64
import chromadb
import json
from sentence_transformers import SentenceTransformer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import google.generativeai as genai
import media
import os


def first_impression(url):
    print("First Impression")
    client = chromadb.Client()
    collection = client.get_or_create_collection('characters')

    embedding_model = SentenceTransformer('./CalHacks/distilroberta')

    with open('./CalHacks/characters.json') as f:
        characters = json.load(f)['characters']

    ids = []
    documents = []
    names = []
    for i in range(0, len(characters)):
        ids.append(str(i))
        documents.append(characters[i]['description'])
        names.append({"name" : characters[i]['name']})

    embeddings = embedding_model.encode(documents)

    collection.add(
    ids=ids,
    embeddings=embeddings.tolist(),
    documents=documents,
    metadatas=names
    )

    testers_from_gemini = "Tech genius who is highly knowledgeable about computers and programming, A non-STEM college student, 70-year-old grandmother, average middle-aged guy who is practical and straightforward"
    tester_descriptions = testers_from_gemini.split(",")
    result_names = []
    result_descriptions = []
    for desc in tester_descriptions:
        print("Description: ", desc)
        desc_embedding = embedding_model.encode([desc])

        results = collection.query(
            query_embeddings=desc_embedding.tolist(),
            n_results=3  # Number of similar results to retrieve
        )
        result_names.append(results['metadatas'][0][0]['name'])
        result_descriptions.append(results['documents'][0][0])
        print(results['documents'][0])
        
    def capture_screenshot(url, output_file):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.save_screenshot(output_file)
        driver.quit()

    def get_html(url, output_file):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        page_source = driver.page_source
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(page_source)

    output_file = "screenshot.png"
    capture_screenshot(url, output_file)
    get_html(url, "page_source.html")
    print(f"Screenshot saved as {output_file}")

    genai.configure(api_key='AIzaSyDfbUu98zV2jFzuu45Tj4xnME_1jFHZfWg')

    myfile = genai.upload_file("screenshot.png")
    impressions = []
    for user_index in range(0, len(result_names)):
        # print(f"{myfile=}")
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = "Pretend you are " + result_names[user_index] + ". "
        prompt = prompt + result_descriptions[user_index] + "\n"
        prompt = prompt + "Assuming you have just been given this website to use. Give me feedback (what's good and what's bad) about the user experience of this website. Make the feedback as personal as possible. Give me a maximum of 200 words, and write a single paragraph."
        result = model.generate_content(
            [myfile, "\n\n", prompt]
        )
        impressions.append({
            "name": result_names[user_index],
            "summary": result_descriptions[user_index].split(".")[0],
            "feedback": result.text
        })
        # impressions[result_names[user_index]] = result.text
        print(f"{result.text=}")
    
    if os.path.exists("./CalHacks/first_impressions.json"):
        os.remove("./CalHacks/first_impressions.json")
    
    f = open("./CalHacks/first_impressions.json", "a")
    json.dump(impressions, f, indent=4)
    print(impressions)