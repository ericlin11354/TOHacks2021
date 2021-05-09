import os
import openai
import requests
import random

from api_key import push_key


def get_query(feed_in, engine, max_tokens, stop):
    out = openai.Completion.create(
        engine=engine,
        prompt=feed_in,
        max_tokens=max_tokens,
        stop=stop,
        temperature=0.3,
        frequency_penalty=0.7
    )
    return out


def gen_text(content):
    feed = "Short story ideas:\n"
    for i in range(1, 4):
        feed += str(i) + ". " + content[random.randint(0, 171)]
    feed += "4."

    output = get_query(feed, "curie", 100, "\n")
    text = output.choices[0].text
    return text


push_key()
openai.api_key = os.getenv("OPENAI_API_KEY")

file = "WP.txt"  # 172 lines
with open(file) as f:
    content_list = f.readlines()

for _ in range(5):
    text_out = gen_text(content_list)
    print("- " + text_out)


