def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    best_value = float('-inf')

    for key in a_dictionary:
        if a_dictionary[key] > best_value:
            best_value = a_dictionary[key]
            best_key = key

        return best_key
scores = {'Jayden': 61, 'leon': 32, 'Mei': 98, 'Bill': 96}
print(best_score(scores))
