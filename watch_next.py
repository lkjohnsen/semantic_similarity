import spacy

nlp = spacy.load('en_core_web_md')


def read_file():
    """Reads the movies.txt file and returns the lines from the file.

    Returns:
        list: Descriptions of each of the movies from the text file.
    """
    with open("movies.txt", "r", encoding="utf-8") as movies_file:
        lines = movies_file.readlines()

        return lines


def stored_movies():
    """All the movies and their details are stored in a dictionary, which is returned.

    Returns:
        dict: key:value pairs where key is the movie_name and value is the movie_descr
    """

    lines = read_file()
    movie_dict = {}
    for line in lines:
        movie_name, movie_descr = line.split(":")
        movie_name = movie_name.strip()
        movie_descr = movie_descr.replace("\n", "")
        movie_dict[movie_name] = movie_descr

    return movie_dict


def similarity_check(movie_dictionary, description):
    """This function takes in two arguments: movie_dictionary and description.
    The movie descriptions in the movie_dictionary is then compared against the description
    of the movie "Planet Hulk", and the most semantically similar movie is returned.

    Args:
        movie_dictionary (dict): The dictionary contains information about the movie name and
                                 the description of the movie
        description (str): A string with the description of the movie "Planet Hulk"

    Returns:
        str: A string with the most similar movie
    """

    # Constructing a Doc object
    description_to_compare = nlp(description)

    highest_similarity = 0
    most_similar_movie = ""

    print("\nSimilarity check results:")
    print("-" * 28)
    for movie_name, descr in movie_dictionary.items():

        similarity = nlp(descr).similarity(description_to_compare)
        print(f"{movie_name} - {similarity}")

        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_movie = movie_name
    print("-" * 28)

    return most_similar_movie


def movie_description():
    """ Returns the variable "planet_hulk" which is a string with the description of the
    Movie 'Planet Hulk'.
    """

    planet_hulk_descr = """
    Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
    the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the
    Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold
    into slavery and trained as a gladiator.
    """

    return planet_hulk_descr


def main():
    """Initiates the program by making function calls, and printing the result of the most
    similar movie match.
    """

    movie_dictionary = stored_movies()
    description_to_cf = movie_description()
    most_similar_movie = similarity_check(movie_dictionary, description_to_cf)

    print(f"\nThe most similar movie is: {most_similar_movie}")


main()
