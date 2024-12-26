import requests

url = "https://article-extractor-and-summarizer.p.rapidapi.com/summarize"

querystring = {"url":"https://time.com/6266679/musk-ai-open-letter/","lang":"en","engine":"2"}

headers = {
	"x-rapidapi-key": "5e025abfc4mshc9e6000b3545db6p1f9bacjsnf31bf453bf07",
	"x-rapidapi-host": "article-extractor-and-summarizer.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
