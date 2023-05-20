from flask import Flask, render_template, request, jsonify
from model import get_next_move

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    board = request.json['board']
    next_move = get_next_move(board)
    return jsonify({'row': next_move[0], 'column': next_move[1]})

if __name__ == '__main__':
    app.run(debug=True)
