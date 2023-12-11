from py2neo import Graph, Node, Relationship
from flask import Flask, render_template
from random import choice


app = Flask(__name__)
graph = Graph("bolt://neo4j:7687", auth=("neo4j", "adminpass"))

logged_user = "Pepa"


def mock_data(graph):
    tx = graph.begin()
    pepa = Node("Person", name="Pepa", age=34, hobbies=["programming", "running"])
    jana = Node("Person", name="Jana", age=30, hobbies=["cats", "running"])
    michal = Node("Person", name="Michal", age=38, hobbies=["partying", "cats"])
    alena = Node("Person", name="Alena", age=32, hobbies=["kids", "cats"])
    richard = Node("Person", name="Richard", age=33, hobbies=["partying", "cats"])
    users = [pepa, jana, michal, alena, richard]

    pepovi_se_libi_jana = Relationship(pepa, "LIKES", jana)
    jane_se_libi_pepa = Relationship(jana, "LIKES", pepa)
    michalovi_se_libi_alena = Relationship(michal, "LIKES", alena)
    alene_se_nelibi_michal = Relationship(alena, "DISLIKES", michal)
    richardovi_se_libi_alena = Relationship(richard, "LIKES", alena)
    relationships = [pepovi_se_libi_jana, jane_se_libi_pepa, michalovi_se_libi_alena, alene_se_nelibi_michal, richardovi_se_libi_alena]

    for user in users:
        graph.create(user)

    for relationship in relationships:
        graph.create(relationship)


def get_logged_user_profile(graph, username):
    return graph.run(f"""
        MATCH (user:Person)
        WHERE user.name = '{username}'
        RETURN user.name, user.age, user.hobbies
    """).data()[0]
    
            
def get_matches(graph, username):
    return graph.run(f"""
        MATCH (friend:Person)-[:LIKES]->(user:Person)-[:LIKES]->(friend:Person) 
        WHERE user.name = '{username}'
        RETURN friend.name, friend.age, friend.hobbies
    """).data()


def available_matches(graph, username):
    return graph.run(f"""
        MATCH (user:Person)
        MATCH (friend:Person)
        WHERE user.name = '{username}'
        AND NOT (user:Person)-[:LIKES]->(friend:Person)
        AND NOT (friend:Person)-[:DISLIKES]->(user:Person)
        AND NOT (user:Person)-[:DISLIKES]->(friend:Person)
        AND NOT friend.name = '{username}'
        RETURN friend.name, friend.age, friend.hobbies
    """).data()


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/matches")
def matches():
    matches = get_matches(graph, logged_user)
    return render_template("matches.html", profiles=matches)


@app.route("/matching")
def matching():
    potential_matches = available_matches(graph, logged_user)
    if potential_matches:
        random_profile = choice(potential_matches)
    else:
        random_profile = None
    return render_template("matching.html", profile=random_profile)


@app.route("/profile")
def profile():
    logged_user_info = get_logged_user_profile(graph, logged_user)
    return render_template("profile.html", profile=logged_user_info)


if __name__ == "__main__":
    #mock_data(graph)
    app.run(debug=True, host="0.0.0.0", port=5000)