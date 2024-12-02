import requests
import html


DATA_API_URL = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"

# local backup question data
local_question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can kill a small dog.", "answer": "True"}
]

# attempt to fetch data from the API
try:
    response = requests.get(DATA_API_URL, timeout=5)
    response.raise_for_status()  # raise an error for HTTP issues
    data = response.json()
    
    # check if API response contains valid data
    if data["response_code"] == 0 and "results" in data:
        # transform the API data into the same format as local_question_data
        question_data = [
            {"text": html.unescape(item["question"]), "answer": item["correct_answer"]}
            for item in data["results"]
        ]
    else:
        # use local data if API response is invalid
        print("API returned invalid data. Falling back to local questions.")
        question_data = local_question_data
except Exception as e:
    # use local data if an error occurs (e.g., no internet, timeout, bad response)
    print(f"Error fetching data from API: {e}")
    print("Falling back to local questions.")
    question_data = local_question_data
