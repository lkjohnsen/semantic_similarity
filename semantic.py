import spacy
nlp = spacy.load('en_core_web_md')


def word_similarity():
    word1 = nlp("cat")
    word2 = nlp("monkey")
    word3 = nlp("banana")
    word4 = nlp("circus")
    print(f"{word1} - {word2}: {word1.similarity(word2)}")
    print(f"{word3} - {word2}: {word3.similarity(word2)}")
    print(f"{word3} - {word1}: {word3.similarity(word1)}")
    print(f"{word4} - {word1}: {word4.similarity(word1)}")
    print(f"{word4} - {word2}: {word4.similarity(word2)}")
    print(f"{word4} - {word3}: {word4.similarity(word3)}")


def working_w_vectors():
    print()
    print("Working with vectors:")

    tokens = nlp(
        'cat apple monkey banana flower soil bees kitten puppy book paper pen')

    for token1 in tokens:
        for token2 in tokens:
            print(f"{token1.text} - {token2.text}: {token1.similarity(token2)}")


def sentence_similarity():
    print()
    print("Similarity between longer sentences:")

    sentence_to_compare = "Why is my cat on the car"

    sentences = ["where did my dog go",
                 "I've lost my car in my car",
                 "I'd like my boat back",
                 "I will name my dog Diana",
                 ]

    model_sentence = nlp(sentence_to_compare)

    print(f"Comparing to: '{sentence_to_compare}'")
    for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        print(f"{sentence} - {similarity}")


def main():
    word_similarity()
    working_w_vectors()
    sentence_similarity()


main()


# COMMENTS
# COMPULSORTY TASK 1
# QUESTION 1:
# ● Write a note about what you found interesting about the similarities
#   between cat, monkey and banana and think of an example of your own.

# ANSWER:
#   - The words "cat" and "monkey" seem to have a fairly good match with 0.5929929675536907.
#     I'm thinking this has to do with both of the words is a type of animal,
#     and therefor is semantically similar or related.
#
#   - The words "banana" and "monkey" also have some similarity with 0.4041501317354622.
#     This is less than for two animal type words, but could be related to the fact that monkeys are
#     often associates with eating bananas, as their main diet consists of eating fruits.

#   - The words "banana" and "cat" has a low resembelance match with 0.22358827466989753.
#     The two words don't have much of a semantical relationship.

#   - The extra word that I have added "circus" has a fairly low resembelance match with the animal words,
#     but a bit higer with the word "monkey" (0.3977627887506635) than "cat" (0.22756253100077126).
#     This could be because monkeys are sometimes used at circuses, and perhaps cats too, but less
#     common. It has very low resembelance with the word "banana" with only 0.08752352921535249 match.


# QUESTION 2:
# ● Run the example file with the simpler language model ‘en_core_web_sm’
#   and write a note on what you notice is different from the model
#   'en_core_web_md'.

# ANSWER:
#   - When running the example file with the simpler language model there's a difference in
#     the accuracy from the medium model. The 'en_core_web_md' model seems better at finding entities
#     than the smaller ‘en_core_web_sm’ model.

#     Here are some of the most noticable differences I came across:

#     'en_core_web_md'      -   ‘en_core_web_sm’        DIFFERENCE BETWEEN THE MODELS

#   -------------Complaints similarity---------------
#     0.8350770380943701    -   0.5090129538857674      DIFFERENCE = 0.3260640842
#     0.8145959567773281    -   0.4497374989081487      DIFFERENCE = 0.3648584579

#   -------------Recipes similarity---------------
#     0.8206931822271948    -   0.5845283005158871      DIFFERENCE = 0.2361648817
#     0.8761883563680793    -   0.6028836058675155      DIFFERENCE = 0.2733047505

#   -------------Recipes similarity---------------
#     0.7398681679268514    -   0.3016250881950343      DIFFERENCE = 0.4382430797
#     0.7114560945673947    -   0.1365426628896247      DIFFERENCE = 0.5749134317
