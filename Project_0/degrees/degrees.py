import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # Initializing a frontier
    frontier = QueueFrontier()
    # Explored nodes
    explored = set()
    # Nodes with connection to parent/source nodes
    nodes = set()


    # Start node
    start = Node(source, None, people[source]['movies'])
    #Checking that start and goal are not the same person
    if source == target:
        return None
    
    # Frontier stores start node 
    frontier.add(start)
    NodeIsExplored = False

    # Using frontier to explore other nodes
    while not frontier.empty():
        # the node being explored is parent to next node: Firstly start node is parent leading to other nodes
        parentNode = frontier.remove()
        explored.add(parentNode)

        # get movies (i.e. action ) that the node has been in
        actions = parentNode.action

        # go through actions to find if there is any other actor that has been in the movie
        for movieID in actions:
             connectedStars = movies[movieID]['stars']

             for star in connectedStars:
                NodeIsExplored = False
                childNode = Node(star,parentNode,people[star]['movies'])

                # is child node the goal? 
                if childNode.state == target:
                    
                    # We will have to trace back the path and reverse it to find the original path traced to reach this state
                    
                    # Initialize a empty list
                    path = []

                    while childNode.parent != None:
                        movie = set(childNode.parent.action) & set(childNode.action) 
                        movieStar = movie.pop()
                        path = path + [(movieStar,childNode.state)]

                        # Move to next parent node up the shortest path
                        childNode = childNode.parent
                    # path from target to source obtained. Reverse to get path from source to target
                    path.reverse()
                    return path
                
                # To check if we have been in a node before or not
                # If the node is already explored we won't again add it to frontier to explore it further
                for exploredNode in explored:
                    if childNode.state == exploredNode.state():
                        NodeIsExplored = True
                
                # if node is not explored before, we will explore it further so we will push it in frontier
                if not NodeIsExplored:
                    frontier.add(childNode)

                childNode = None

                ## End of actions to connect from parent to child nodes






def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
