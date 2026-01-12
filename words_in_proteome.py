def read_words(filename):
    words = []
    file = open(filename, "r")
    for line in file:
            word = line.strip("\n").upper()
            if len(word) >= 3:
                words.append(word)
    return words

def read_sequences(filename):
    f = open(filename, "r")
    proteome = {}
    current_id = ""
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current_id = line.split("|")[1]
            proteome[current_id] = ""
        else:
            proteome[current_id] += line
    f.close()
    return proteome


def search_words_in_proteome(words, proteome):
    result = {}
    for word in words:
        count_seq = 0
        count_occ = 0
        for seq in proteome.values():
            if word in seq:
                count_seq += 1
            count_occ += seq.count(word)
        if count_seq > 0:
            result[word] = [count_seq, count_occ]
            print(f"Le mot '{word}' est présent dans {count_seq} protéines et {count_occ} fois au total.")

    return result


def find_most_frequent_occurrence(matches):
    most_word = ""
    max_occ = 0
    for word, values in matches.items():
        occ = values[1]  # index 1 = nombre total d'occurrences
        if occ > max_occ:
            max_occ = occ
            most_word = word

    print(f"\n=> Le mot le plus fréquent est '{most_word}' avec {max_occ} occurrences dans tout le protéome.")


def find_most_frequent_word(matches, total_proteins):
    most_word = ""
    max_count = 0
    for word, count in matches.items():
        if count > max_count:
            max_count = count
            most_word = word

    print(f"=> {most_word} found in {max_count} sequences")

    percentage = (max_count / total_proteins) * 100
    print(f"Pourcentage du protéome contenant ce mot : {percentage:.2f}%")



words_list = read_words("english-common-words.txt")
print(f"Nombre de mots valides :", len(words_list))
print(words_list[:10])

proteins = read_sequences("uniprotkb_proteome_UP000005640_AND_revi_2025_11_12.fasta")
print("Nombre de séquences lues :", len(proteins))
print("Séquence de la protéine O95139 :", proteins["O95139"])

matches = search_words_in_proteome(words_list, proteins)
print("\nNombre de mots trouvés dans au moins une protéine :", len(matches))

matches = search_words_in_proteome(words_list, proteins)
print("\nNombre de mots trouvés dans au moins une protéine :", len(matches))

find_most_frequent_word(matches, len(proteins))

matches = search_words_in_proteome(words_list, proteins)

find_most_frequent_occurrence(matches)
