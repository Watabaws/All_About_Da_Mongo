from flask import Flask, render_template, request, redirect, flash, Markup, url_for, jsonify
import requests, os
from util import database, misc, giphy

app = Flask(__name__)

@app.route("/")
def home():


if __name__ == "__main__":
    app.debug = True
    app.run()
