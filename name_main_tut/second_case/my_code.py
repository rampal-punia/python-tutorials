
def add_n_elements(a_list, n):
    result = sum(a_list[:n])
    print(result)


def dict_to_list(a_dict):
    sup_heros = a_dict.get('superheros')
    actors = a_dict.get('actors')

    sup_heros_fname = "sup_heros.txt"
    write_to_txt(sup_heros_fname, sup_heros)

    actors_fname = "actors.txt"
    write_to_txt(actors_fname, actors)


def write_to_txt(filename, text):
    with open(filename, 'w') as f:
        for name in text:
            f.writelines(f"{name}\n")


if __name__ == "__main__":
    a_list = [2, 4, 5, 3, 6, 4, 7, 4, 6, 9, 1, 90, "shaktiman"]
    add_n_elements(a_list, n=2)

    a_dict = {
        'superheros': ['krrish', 'thor', 'shaktiman', 'spiderman',  'ironman'],
        'actors': ['amitabh', 'anil', 'arnold', 'tom cruise',  'leonardo'],
    }
    dict_to_list(a_dict)
