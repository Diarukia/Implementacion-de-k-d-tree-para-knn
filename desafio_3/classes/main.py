from classes.class_kd_tree.kd_tree import kd__tree
import pandas as pd


def read_csv():
    df = pd.read_csv ('./Desafio3.csv')
    return df

def genre_to_numeric_dict(genre_list):
    genre_dict = dict()
    count = 0
    for i in genre_list:
        genre_dict[i] = count
        count += 1
    return genre_dict


def _main_(arguments):
    df_movies = read_csv()
    genre_list = df_movies.prime_genre.unique()
    genre_dict = genre_to_numeric_dict(genre_list)
    current_kd_tree = kd__tree(df_movies,genre_dict)
    vecinos = current_kd_tree.run(int(arguments[0]))
    current_kd_tree.imprimir_datos(vecinos)


