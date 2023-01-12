#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=10&category=20"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    questions = requests.get(URL).json()

    for question in questions.get("results"):
        print(question.get("question"))
        print(question.get("correct_answer"))

if __name__ == "__main__":
    main()

