import json

websites = {
    "websites" : [
        {
        "url": "https://www.seznam.cz/"
    },
    {
        "url": "https://www.google.com/"
    },
    {
        "url": "https://www.python.org/"
    },
]
}

with open("websites_dict.json", "w") as file:
    json.dump(websites, file)