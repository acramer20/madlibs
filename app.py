"""Madlibs Stories."""
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
story2 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """In a galaxy called {place}, there lived a {adjective} {noun}. This {adjective} loved to {verb} with {plural_noun} every evening at 9:00 PM."""
)

@app.route('/')
def show_home():
    return render_template('home.html')

@app.route('/form')
def show_form():
    story_choice = request.args['stories']
    if story_choice == 'story1':
        form= 'form.html'
    else:
        form= 'form_2.html'
    return render_template(form)

@app.route('/story')
def show_story():
    answers = {
    'place': request.args['place'],
    'noun': request.args['noun'],
    'verb': request.args['verb'],
    'adjective':request.args['adj'],
    'plural_noun':request.args['plural_noun']
    }
    return render_template('story.html', answers=answers, story=story1)

@app.route('/story_2')
def show_story2():
    answers = {
    'place': request.args['place'],
    'noun': request.args['noun'],
    'verb': request.args['verb'],
    'adjective':request.args['adj'],
    'plural_noun':request.args['plural_noun']
    }
    return render_template('story_2.html', answers=answers, story=story2)