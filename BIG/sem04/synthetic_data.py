import random
from faker import Faker
from py2neo import Graph, Node, Relationship

fake = Faker()
graph = Graph("bolt://neo4j:7687", auth=("neo4j", "adminpass"))

# Nastavení počtu uživatelů, příspěvků a vztahů
NUM_USERS = 10 #1000
NUM_POSTS = 50 #5000
NUM_RELATIONSHIPS = 20 #2000

# Vymazání existujících dat
graph.run("MATCH (n) DETACH DELETE n")

# Vytváření uživatelů
users = []
for i in range(NUM_USERS):
    user = Node("User", name=fake.name(), age=random.randint(18, 70), location=fake.city())
    graph.create(user)
    users.append(user)

# Vytváření příspěvků
posts = []
for i in range(NUM_POSTS):
    user = random.choice(users)
    post = Node("Post", content=fake.text(), created_at=fake.date_time_this_year())
    graph.create(post)
    graph.create(Relationship(user, "CREATED", post))
    posts.append(post)

# Vytváření vztahů mezi uživateli (FOLLOWING)
for i in range(NUM_RELATIONSHIPS):
    user_a = random.choice(users)
    user_b = random.choice(users)
    if user_a != user_b:
        graph.create(Relationship(user_a, "FOLLOWS", user_b))

# Vytváření komentářů
for i in range(NUM_POSTS // 2):
    user = random.choice(users)
    post = random.choice(posts)
    comment = Node("Comment", content=fake.sentence(), created_at=fake.date_time_this_year())
    graph.create(comment)
    graph.create(Relationship(user, "COMMENTED", comment))
    graph.create(Relationship(comment, "ON", post))

print("Data byla úspěšně vygenerována.")