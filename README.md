# Spacy Word and Sentence Similarity

This is a simple Python script that demonstrates how to use Spacy to compute word and sentence similarity.

## Contents

1. Prerequisites
2. Usage
3. Code Description
   - word_similarity()
   - working_w_vectors()
   - sentence_similarity()
4. Main function

## Prerequisites

This code requires the following packages to be installed:

- Spacy

To install Spacy, you can run:
`pip install spacy`

In addition, you will also need to download a Spacy model. In this example, we are using the en_core_web_md model. To download this model, you can run:

`python -m spacy download en_core_web_md`

## Usage

To use this code, simply run the main() function:
`python3 semantic.py`

This will output the word and sentence similarity results to the console.

## Code Description

The code consists of three functions:

1. **word_similarity():** This function demonstrates how to compute the similarity between different words using the Spacy model. In this example, we are comparing the similarity between the words "cat", "monkey", "banana", and "circus".
2. **working_w_vectors():** This function demonstrates how to work with word vectors using the Spacy model. In this example, we are computing the similarity between all pairs of words in a given sentence.
3. **sentence_similarity():** This function demonstrates how to compute the similarity between longer sentences using the Spacy model. In this example, we are comparing a single sentence to a list of other sentences to see which one is most similar.

The **main()** function simply calls each of these functions in turn and prints the results to the console.

# Movie Similarity Checker

This is a Python script that uses spaCy, a free and open-source library for advanced Natural Language Processing (NLP), to compare the similarity of movie descriptions in a given text file to a description of the movie "Planet Hulk". The script outputs the name of the most semantically similar movie in the text file.

## Contents

1. Installation
2. Usage
3. File descriptions

## Installation

To run this script, you need to install spaCy and download the "en_core_web_md" model:
`pip install spacy`
`python3 -m spacy download en_core_web_md`

## Usage

1. Place the movie descriptions in a text file named "movies.txt". The file should be formatted with each line containing the name of a movie followed by a colon and then the movie's description.
2. Run the script using the following command:
   `python3 watch_next.py`

3. The script will output the most semantically similar movie to "Planet Hulk" based on the descriptions provided in the text file.

## File descriptions

- **watch_next.py:** The main Python script that loads the spaCy model, reads the text file with movie descriptions, compares the descriptions to the description of "Planet Hulk", and returns the name of the most semantically similar movie.

- **movies.txt:** A sample text file containing movie names and their descriptions.
