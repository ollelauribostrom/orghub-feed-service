from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
  return jsonify({ 'message': 'Feed service up and running' })
