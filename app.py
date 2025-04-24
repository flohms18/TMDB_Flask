from flask import Flask, request, render_template
import requests

app = Flask(__name__)

TMDB_API_KEY = '27beba95fd51654379e58b8e53c1c594'

@app.route('/', methods=['GET', 'POST'])
def home():
    search_results = []
    selected_movie = None

    if request.method == 'POST':
        movie_id = request.form.get('movie_id')
        if movie_id:
            # Fetch movie details by ID
            url = f'https://api.themoviedb.org/3/movie/{movie_id}'
            params = {'api_key': TMDB_API_KEY}
            response = requests.get(url, params=params)
            if response.ok:
                selected_movie = response.json()
    
    # Handle initial search
    query = request.args.get('query')
    if query:
        url = 'https://api.themoviedb.org/3/search/movie'
        params = {'api_key': TMDB_API_KEY, 'query': query}
        response = requests.get(url, params=params)
        if response.ok:
            data = response.json()
            search_results = data.get('results', [])

    return render_template('index.html', results=search_results, selected_movie=selected_movie)

if __name__ == '__main__':
    app.run(debug=True)
