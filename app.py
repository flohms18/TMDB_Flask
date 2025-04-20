from flask import Flask, request, render_template
import requests

app = Flask(__name__)

TMDB_API_KEY = '27beba95fd51654379e58b8e53c1c594'

@app.route('/')
def home():
    query = request.args.get('query')
    results = []
    if query:
        url = 'https://api.themoviedb.org/3/search/movie'
        params = {'api_key': TMDB_API_KEY, 'query': query}
        response = requests.get(url, params=params)
        if response.ok:
            data = response.json()
            results = data.get('results', [])

    return render_template('index.html',results=results)

if __name__ == '__main__':
    app.run(debug=True)
