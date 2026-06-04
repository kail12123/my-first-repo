from flask import Flask, render_template, jsonify

app = Flask(__name__)

# City data with photos from internet and coordinates
CITIES = {
    'Almaty': {
        'lat': 43.2380,
        'lng': 76.9502,
        'photo': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop',
        'description': 'Largest city in Kazakhstan'
    },
    'Astana': {
        'lat': 51.1694,
        'lng': 71.4491,
        'photo': 'https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=400&h=300&fit=crop',
        'description': 'Capital of Kazakhstan'
    },
    'Karaganda': {
        'lat': 49.8047,
        'lng': 72.8926,
        'photo': 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=400&h=300&fit=crop',
        'description': 'Industrial city'
    },
    'Shymkent': {
        'lat': 42.3088,
        'lng': 69.5952,
        'photo': 'https://images.unsplash.com/photo-1538823010655-faa8f0b7cfb0?w=400&h=300&fit=crop',
        'description': 'Ancient southern city'
    },
    'Aktobe': {
        'lat': 50.2839,
        'lng': 57.1700,
        'photo': 'https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=400&h=300&fit=crop',
        'description': 'Western Kazakhstan'
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map_page():
    return render_template('map.html', cities=CITIES)

@app.route('/api/cities')
def get_cities():
    return jsonify(CITIES)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
