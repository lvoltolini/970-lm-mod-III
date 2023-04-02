# %% [markdown]
# # Pacotes necessários:
# 
# ### Verificar se a máquina possui os pacotes necessários para rodar o programa.

# %%
# Esta função encerra o programa.
def fatal_error():
    input('O programa encontrou um erro fatal e não pode continuar. Pressione uma tecla para encerrar o programa: ')
    quit()
    
# Dicionário com os pacotes para baixar.

packages_install_names = {
    'pandas' : 'pandas',
    'numpy' : 'numpy',
    'os' : 'os',
    'sys' : 'sys',
    'matplotlib.pyplot' : 'matplotlib',
    'seaborn' : 'seaborn',
    'statsmodels' : 'statsmodels',
    'scipy' : 'scipy',
    'pypfopt': 'PyPortfolioOpt',
    'functools' : 'functools'    
}


# %% [markdown]
# ### Função para checar os pacotes

# %%
# Verificando se importlib está instalado

try: import importlib
except: fatal_error

# Esta função verifica os pacotes necessários.

def check_packages(packages):
    for package in packages:
        try: importlib.import_module(package)
        except: print(f'Erro: O pacote {packages[package]} não está instalado. Tente instalá-lo utilizando o comando pip3 install {package} ')
        else: print(f'Sucesso ao importar o pacote {package}.')
        
# Agora, verificamos se algum pacote possui erro:

check_packages(packages_install_names)

# %% [markdown]
# # Importando os pacotes
# ### Primeiro definimos os pacotes e os seus aliases.

# %%
# Dict de pacotes: 

packages_import_names = {
    'pandas' : 'pd',
    'numpy' : 'np',
    'os' : 'os',
    'sys' : 'sys',
    'matplotlib.pyplot' : 'plt',
    'seaborn' : 'sns',
    'statsmodels' : 'sm',
    'scipy.linalg' : 'ln',
    'pypfopt': 'pypfopt',
    'functools' : 'functools'    
}

# Função para importar os pacotes:

def import_packs(packages):
    for package, alias in packages.items():
        globals()[alias] = importlib.import_module(package)
        print(f'Sucesso ao importar {package} as {alias}.')
        
        
# Loop para os imports:

import_packs(packages_import_names)
    

# %%
from Data import cadastro, inv1, inv2


