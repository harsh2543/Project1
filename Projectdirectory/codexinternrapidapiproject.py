from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# RapidAPI credentials
RAPIDAPI_KEY = "5e025abfc4mshc9e6000b3545db6p1f9bacjsnf31bf453bf07"
RAPIDAPI_HOST = "article-extractor-and-summarizer.p.rapidapi.com"

@app.route('/')
def home():
    """
    Renders the main page with an input form for users to submit article URLs.
    """
    return render_template('index2.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    """
    Fetches the summary of an article from RapidAPI and returns it as JSON.
    """
    url = request.json.get('url')  # URL from the client

    if not url:
        return jsonify({"error": "Please provide a valid URL."}), 400

    # API endpoint and query parameters
    api_url = "https://article-extractor-and-summarizer.p.rapidapi.com/summarize"
    querystring = {"url": url, "lang": "en", "engine": "2"}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }

    try:
        response = requests.get(api_url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        summary = data.get("summary", "Summary not available.")
        return jsonify({"summary": summary})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch summary: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
