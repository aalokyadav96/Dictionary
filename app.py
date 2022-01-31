from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    word = request.form['text']
    of_lang = request.form['srclang']
    to_lang = request.form['language']
    meaning = ["Meaning"]
    is_a = ["Noun"]
    antonyms = ["Antonym"]
    synonyms = ["Synnym"]
    similar_words = ["Similar"]
    word_forms = ["Noun", "Verb"]
    listen = ["speak"]

    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'results.html',
        meaning=meaning,
        word=word,
        of_lang=of_lang,
        to_lang=to_lang,
        is_a = is_a,
        antonyms = antonyms,
        synonyms = synonyms,
        similar_words = similar_words,
        
    )


























