import pandas as pd
dataframe = pd.read_excel('Dataset.xlsx', header=None, names=["Speaker", "Utterance"])
CHI_UT = dataframe[dataframe["Speaker"] == "CHI: "]["Utterance"]
indeces = CHI_UT.index
word_dict = {}

# Go through every word of every utterance and get input for the classification
for num, utterance in enumerate(CHI_UT):
    utterance = utterance.replace(" .", "")
    words = utterance.split(" ")
    while("" in words): # Get rid of empty elements
        words.remove("")
    if indeces[num] == 0:
        print("------------")
        print(f"{dataframe[:indeces[num] + 3]}")
    else:
        print("------------")
        print(f"{dataframe[indeces[num] - 2:indeces[num] + 1]}")
    for n, word in enumerate(words):
        print(n)
        pre = " ".join(words[:n])
        post = " ".join(words[n+1:])
        classification = input(f"\n\n\n{num}) {pre} \033[4m{word}\033[0m {post}\n")
        if classification not in word_dict.keys():
            word_dict[classification] = [word]
        else:
            word_dict[classification].append(word)
print(word_dict)

annotated = pd.DataFrame(columns=["Word", "Classification"])
for key in word_dict.keys():
    for word in word_dict[key]:
        row = [word, key]
        annotated.loc[len(annotated)] = row
    print(key, ": ", len(word_dict[key]))

annotated.to_csv("annotated.csv")