import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from decision_tree import Value_Assignment 
from markov_chain import History_Assignment
from collections import defaultdict

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    backstory="backstory is fgreat"
    if request.method == "POST":
        gender_wordtonumber = defaultdict(lambda: 0)
        gender_wordtonumber["non-binary"] = 0
        gender_wordtonumber["female"] = 1
        gender_wordtonumber["male"] = 2

        species_wordtonumber = defaultdict(lambda: 0)
        species_wordtonumber["human"] = 0
        species_wordtonumber["druid"] = 1
        species_wordtonumber["mage"] = 2
        species_wordtonumber["sorcerer"] = 3
        species_wordtonumber["elf"] = 4
        species_wordtonumber["dwarf"] = 5

        name = request.form["name"]
        pronouns = request.form["pronouns"]
        age = request.form["age"]
        gender = gender_wordtonumber[request.form["gender"]]
        species = species_wordtonumber[request.form["species"]]

        traits = {}

        traits["age"] = age
        traits["gender"] = gender
        traits["species"] = species

        traits, values, states = Value_Assignment().decision_tree_values(traits)
        life_history = History_Assignment().make_Life_History(values, states)
        backstory = "name: " + name + ", pronouns: " + pronouns + ", traits: age: " + str(traits["age"]) + " gender: " + traits["gender"] + " species: " + traits["species"]\
                 + " values: mood: " + values["mood"] + " workethic: " + values["workethic"] + " intelligence: " + values["intelligence"] \
                 + " luck: " + values["luck"] + " magic: " + values["magic"] + ", states: career: " + states["careerfield"]\
                 + " education: " + states["education"] + " life-changing event: " + states["life-changing"] \
                 + " event: " + states["events2"] + " event: " + states["events"] + ", life history: " + life_history
        
        response = openai.Completion.create(
            model="text-davinci-003", #gpt-3.5-turbo text-davinci-003
            prompt=generate_prompt(backstory),
            max_tokens= 3200,
            temperature=0.9,
        )
        return redirect(url_for("index", result=response.choices[0].text, backstory=backstory))
    result = request.args.get("result")
    backstory = request.args.get("backstory")
    print(backstory)
    return render_template("index.html", backstory=backstory, result=result)


def generate_prompt(backstory):
    return """Write a backstory with at least three sentences, using the life history as order of events

Details: name: Lisanna, pronouns: she/her, traits: age: 21 gender: female species: human values: mood: compassionate workethic: ambitious intelligence: dumb luck: lucky magic: non-magical, states: career: bookbinder education: apprenticeship life-changing event: got knighted event: got embarrassed publicly event: received a medal, life history: apprenticeship, got knighted, received a medal, single, received a medal
Backstory: Lisanna is a 21-year-old woman who is very compassionate and ambitious. She did an apprenticeship to become a bookbinder. After finishing her apprenticeship, Lisanna got knighted by the king and received a medal. She did all this while being single. Then she received another medal.
Details: name: Drake, pronouns: he/him, traits: age: 67 gender: male species: sorcerer values: mood: cold workethic: lazy intelligence: dumb luck: lucky magic: magical, states: career: bounty hunter education: apprenticeship life-changing event: blessed by the gods event: got embarrassed publicly event: received a gift, life history: apprenticeship, received a gift, bounty hunter, got embarrassed publicly, bounty hunter
Backstory: Drake is a 67-year-old sorcerer. He is cold-hearted and lazy. Drake did an apprenticeship and became a bounty hunter after he received a gift. Drake got publicly embarrassed and reluctantly returned to his duty as a bounty hunter.
Details:  name: Alex, pronouns: they/them, traits: age: 34 gender: non-binary species: dwarf values: mood: cold workethic: lazy intelligence: smart luck: unlucky magic: non-magical, states: career: scholar education: learning on the go life-changing event: got deadly ill event: had a wish come true event: fell down a tree, life history: fell down a tree, scholar, got deadly ill, learning on the go, fell down a tree
Backstory: Alex is a 34-year-old dwarf. They are cold-hearted and lazy. When Alex was young, they fell down a tree. They became deadly ill. However, Alex kept learning on the go. Unfortunately, Alex fell down another tree.
Details: {}
Backstory:""".format(
        backstory.capitalize()
    )
