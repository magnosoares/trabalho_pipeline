"""
Pipeline - Etapa 1: Carregar e Explorar Dados
"""
import pandas as pd


def carregar_dados(caminho_arquivo):
    """
    Carrega o dataset de clientes.
    
    Args:
        caminho_arquivo: caminho para o CSV
        
    Returns:
        DataFrame com os dados
    """
    # TODO 1: Use pd.read_csv() para carregar o arquivo
    df = pd.read_csv(caminho_arquivo)
    
    return df


def explorar_dados(df):
    """
    Mostra informações básicas sobre o dataset.
    
    Args:
        df: DataFrame a ser explorado
    """
    print("=" * 50)
    print("EXPLORAÇÃO DOS DADOS")
    print("=" * 50)
    
    # TODO 2: Mostre o shape do DataFrame (linhas, colunas)
    print("\nShape do DataFrame")
    print(f"Shape: {df.shape}")
    
    # TODO 3: Mostre os tipos de cada coluna
    print("\nTipos das Colunas")
    print(df.dtypes)

    # TODO 4: Mostre as 5 primeiras linhas
    print("\nPrimeiros registros do DataFrame")
    print(df.head())
    
    print("\n" + "=" * 100)


def verificar_target(df, coluna_target='respondeu_campanha'):
    """
    Verifica a distribuição da variável target.
    
    Args:
        df: DataFrame
        coluna_target: nome da coluna target
    """
    print("-" * 50)
    print("DISTRIBUIÇÃO DO TARGET")
    print("-" * 50)
    
    # TODO 5: Mostre a contagem de cada valor do target
    print("\nContagem de cada valor do target")
    print(df[coluna_target].value_counts())
    
    # TODO 6: Mostre a proporção (percentual) de cada valor
    print("\nProporção de cada valor do target")
    print(df[coluna_target].value_counts(normalize=True))
        
    print("\n" + "-" * 50)


# Teste local (executar este arquivo diretamente)
if __name__ == "__main__":
    df = carregar_dados("data/clientes_campanha.csv")
    if df is not None:
        explorar_dados(df)
        verificar_target(df)
    else:
        print("ERRO: DataFrame não foi carregado. Complete o TODO 1!")
