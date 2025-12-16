# Respostas do Trabalho - Pipeline de ML

## Identificação do Grupo

- **Integrantes:**
  1. Tiago André da Silveira Fialho
  2. Magno 
  3. Thiago Lobo Leite
  4. Lucia Helena 

---

## Parte 1: Resultados do Pipeline

### 1.1 O pipeline executou sem erros?
- [X] Sim. Apenas ocorreram dois Warnings: um sobre a remoção de import top-level do pandera em atualizações futuras, e outro sobre documentação de compatibilidade de bibliotecas com o pandera.
- [ ] Não

### 1.2 F1-Score obtido:
```
F1-Score: 0.4348
```

### 1.3 Cole aqui o output final do pipeline:

🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
INICIANDO PIPELINE DE ML
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀


[ETAPA 1/4] Carregando dados...
==================================================
EXPLORAÇÃO DOS DADOS
==================================================
--- SHAPE, TIPOS e HEAD ---
Shape do DataFrame: (5000, 8)

Tipos de Dados:
cliente_id              int64
idade                   int64
renda_mensal          float64
tempo_conta_meses       int64
num_produtos            int64
tem_cartao_credito      int64
score_credito         float64
respondeu_campanha      int64
dtype: object

Primeiras 5 linhas:
   cliente_id  idade  renda_mensal  ...  tem_cartao_credito  score_credito  respondeu_campanha
0           1     56      46917.46  ...                   1          600.0                   1
1           2     69      41274.41  ...                   0          758.2                   0
2           3     46      40649.98  ...                   1          595.7                   1
3           4     32      44336.79  ...                   1          584.3                   0
4           5     60      35301.68  ...                   0          797.8                   0

[5 rows x 8 columns]
==================================================

DISTRIBUIÇÃO DO TARGET
------------------------------

Distribuição da variável target (respondeu_campanha):
respondeu_campanha
0    0.5606
1    0.4394
Name: proportion, dtype: float64
--------------------------------------


Contagem dos valores de target
respondeu_campanha
0    2803
1    2197
Name: count, dtype: int64

Proporção dos valores de target
respondeu_campanha
0    0.5606
1    0.4394
Name: proportion, dtype: float64
------------------------------

[ETAPA 2/4] Validando dados...
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pandera/_pandas_deprecated.py:146: 
FutureWarning: Importing pandas-specific classes and functions from the
top-level pandera module will be **removed in a future version of pandera**.
If you're using pandera to validate pandas objects, we highly recommend updating
your import:

```
# old import
import pandera as pa

# new import
import pandera.pandas as pa
```

If you're using pandera to validate objects from other compatible libraries
like pyspark or polars, see the supported libraries section of the documentation
for more information on how to import pandera:

https://pandera.readthedocs.io/en/stable/supported_libraries.html

To disable this warning, set the environment variable:

```
export DISABLE_PANDERA_IMPORT_WARNING=True
```

  warnings.warn(_future_warning, FutureWarning)
Validando dados...
✅ Dados válidos!

[ETAPA 3/4] Treinando modelo...
Dados de treino: 4000 registros
Dados de teste: 1000 registros
Treinando modelo...
✅ Modelo treinado!
Modelo salvo em: models/modelo_campanha.pkl

[ETAPA 4/4] Avaliando modelo...

==================================================
RESULTADOS DA AVALIAÇÃO
==================================================

📊 MÉTRICAS:
   Accuracy:  0.5710 (57.10%)
   Precision: 0.5205
   Recall:    0.3733
   F1-Score:  0.4348

📋 MATRIZ DE CONFUSÃO:
   Verdadeiros Negativos (TN): 406
   Falsos Positivos (FP):      152
   Falsos Negativos (FN):      277
   Verdadeiros Positivos (TP): 165

==================================================
🎯 F1-SCORE FINAL: 0.4348
==================================================

✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
PIPELINE CONCLUÍDO COM SUCESSO!
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
```

---

## Parte 2: Interpretação dos Resultados

### 2.1 O modelo é bom ou ruim? Por quê?

O modelo é ruim. Como o próprio enunciado da questão suscita, o F1 de 0.4348 é mais baixo que um palpite aleatório, como o de jogar uma moeda. O recall de 0.3733 indica que o modelo só conseguiu identificar 37.33% dos clientes que responderam à pesquisa, ou seja, mais de 60% do público não foi alcançado. 


### 2.2 O dataset é balanceado ou desbalanceado? Como você descobriu?

O dataset é desbalanceado. A distribuição do TARGET de 56% e 44% (aproximadamente) indica isso (ver parte 1 do exercício), assim analisar apenas com base na acurácia não retorna o resultado mais robusto possível, o que o F1 faz. 


### 2.3 Por que usamos F1-Score e não apenas Accuracy neste caso?

Como analisado no item acima, o dataset é desbalanceado, e por isso o F1-Score é uma métrica mais adequada, sendo que o Accuracy. Caso o modelo previsse sempre 0, hipoteticamente, o accuracy  seria de mais de 56% (proporção majoritária), retornando resultados enganosos, já que mesmo sendo de 56% nunca encontraria um cliente para a campanha (mesmo eles existindo).

Por exemplo, se o modelo simplesmente previsse `0` para todos os clientes, ele teria uma acurácia de 56,06% (a proporção da classe majoritária). Isso parece razoável, mas o modelo seria inútil na prática, pois nunca identificaria um cliente interessado na campanha (seu recall seria 0).


## Parte 3: Validação de Dados

### 3.1 Liste as validações Pandera que você implementou:

1. cliente_id: Coluna do tipo inteiro, sem valores nulos mas únicos, condizente com o que se espera de uma chave identificadora.
2. idade: Coluna de inteiros, em um intervalo fechado entre 18 e 80 anos.
3. renda_mensal: Coluna de float e os valores devem estar no intervalo entre 1000.00 e 50000.00 (típico quando tratamentos de valores monetários).
4. score_credito: Coluna de float e os valores devem estar no intervalo entre 300.00 e 850.00.
5. respondeu_campanha: Coluna de inteiros entre 0 e 1, na prática o campo só recebe dois valores, 0 e 1, tal qual binários.


### 3.2 Por que validar dados ANTES de treinar o modelo?

A persistencia de dados fora de conformidade, diminui a confiablidade dos dados, prejudica a validação e consequentemente o treinamento do modelo, ocasionando uma percepção errada do usuário - podendo causar impacto negativo no negócio, em casos mais importantes.

Pensando em um ambiente de produção, os dados inválidos podem causar parada da aplicação, e pior, induzir o modelo a gerar previsões inadequadas ao negócio (um erro silencioso e que pode impactar direta e irreversivelmente a atividade da empresa).

---

## Parte 4: Versionamento

### 4.1 Liste os commits que vocês fizeram (copie do git log):

df0bbaf (HEAD -> main) refact: Exclusão do arquivo README (Enunciado e instruções para os exercícios).
e91f5ea docs: Resposta ao questionamento da Parte4.1
5628ec3 docs: Respostas aos questionamentos Parte1, Parte2 e Parte3.
d91a86f feat: Versão 1.0 da aplicação implantada.
f77de8c feat: Estrutura de arquivos implementada. Conforme modelo estabelecido.

### 4.2 Por que mensagens de commit descritivas são importantes?

Mensagens de commit padronizadas e descritivas são impotantes aspectos do versionamento de uma base de códigos. Sem essas características a manutenabilidade da base é importantemente comprometida. Permite que mesmo equipes que não tem familiaridade com aquele código entenda o que foi alterado, quando e por quem sem precisar analisar diretamente o código, facilitando a revisão do código, a localização de alterações prejudiciais, de features promovidas em momento errado ou mesmo saber onde realizar alterações quando necessário. Permitem ainda um rapido retorno da aplicação a um estado anterior, permitindo a entrada em produção com o isolamento do código indesejado.

---

**Data de entrega:** 16/12/2025
