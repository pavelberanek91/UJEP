from py2neo import Graph, Node, Relationship

graph = Graph("bolt://neo4j:7687", auth=("neo4j", "adminpass"))
            
def print_matches(graph, username):
    for record in graph.run(f"""
                         MATCH (friend:Person)-[:LIKES]->(user:Person)-[:LIKES]->(friend:Person) 
                         WHERE user.name = '{username}'
                         RETURN user.name, friend.name
                         """):
        print(record["friend.name"])

def main():
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

    print("Matches for Pepa:")
    print_matches(graph, "Pepa")
    print("Matches for Jana:")
    print_matches(graph, "Jana")
    print("Matches for Michal:")
    print_matches(graph, "Michal")
    print("Matches for Alena:")
    print_matches(graph, "Alena")
    print("Matches for Richard:")
    print_matches(graph, "Richard")

if __name__ == "__main__":
    main()