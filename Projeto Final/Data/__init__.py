import pandas as pd
from os import getcwd

path = getcwd() + '//Data//'

cadastro = pd.read_csv(path + 'cadastro.csv')
inv1 = pd.read_csv(path + 'investimento_parte1.csv')
inv2 = pd.read_csv(path + 'investimento_parte2.csv')

