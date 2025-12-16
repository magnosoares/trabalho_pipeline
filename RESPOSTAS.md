# Respostas do Trabalho - Pipeline de ML

## Identificação do Grupo

- **Integrantes:**
  1. Nome: Magno Santana Soares
  2. Nome: Lucia Helena Dutra Magalhães
  3. Nome: Thiago Lobo Leite
  4. Nome: Tiago André da Silveira Fialho

---

## Parte 1: Resultados do Pipeline

### 1.1 O pipeline executou sem erros?
<!-- Marque com X a opção correta -->
- [X] Sim
- [ ] Não

### 1.2 F1-Score obtido:
<!-- Copie o valor exibido ao final da execução -->
```
F1-Score: 0.4043
```

### 1.3 Cole aqui o output final do pipeline:
<!-- Execute: python main.py e copie a saída -->
```
(cole o output aqui)
```
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
INICIANDO PIPELINE DE ML
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀


[ETAPA 1/4] Carregando dados...
====================================================================================================
EXPLORAÇÃO DOS DADOS
====================================================================================================

Shape do DataFrame
Shape: (5000, 8)

====================================================================================================

Tipos das Colunas
cliente_id              int64
idade                   int64
renda_mensal          float64
tempo_conta_meses       int64
num_produtos            int64
tem_cartao_credito      int64
score_credito         float64
respondeu_campanha      int64
dtype: object

====================================================================================================

Primeiros registros do DataFrame
   cliente_id  idade  renda_mensal  tempo_conta_meses  num_produtos  tem_cartao_credito  score_credito  respondeu_campanha
0           1     56      46917.46                229             4                   1          600.0                   1
1           2     69      41274.41                  9             3                   0          758.2                   0
2           3     46      40649.98                 25             2                   1          595.7                   1
3           4     32      44336.79                217             5                   1          584.3                   0
4           5     60      35301.68                225             4                   0          797.8                   0

====================================================================================================
----------------------------------------------------------------------------------------------------

DISTRIBUIÇÃO DO TARGET
----------------------------------------------------------------------------------------------------

Contagem de cada valor do target
respondeu_campanha
0    2803
1    2197
Name: count, dtype: int64

----------------------------------------------------------------------------------------------------

Proporção de cada valor do target
respondeu_campanha
0    0.5606
1    0.4394
Name: proportion, dtype: float64

----------------------------------------------------------------------------------------------------

[ETAPA 2/4] Validando dados...
C:\workspacePCDF\202510_Pós MBA IA\02_Pipeline de dados em Python\trabalho_alunos\venv\Lib\site-packages\pandera\_pandas_deprecated.py:146: FutureWarning: Importing pandas-specific classes and functions from the
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
====================================================================================================
Validando dados...
====================================================================================================
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
   Accuracy:  0.5550 (55.50%)
   Precision: 0.4951
   Recall:    0.3416
   F1-Score:  0.4043

📋 MATRIZ DE CONFUSÃO:
   Verdadeiros Negativos (TN): 404
   Falsos Positivos (FP):      154
   Falsos Negativos (FN):      291
   Verdadeiros Positivos (TP): 151

==================================================
🎯 F1-SCORE FINAL: 0.4043
==================================================

✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
PIPELINE CONCLUÍDO COM SUCESSO!
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅

📝 Anote o F1-Score no arquivo RESPOSTAS.md: 0.4043
---

## Parte 2: Interpretação dos Resultados

### 2.1 O modelo é bom ou ruim? Por quê?
É ruim porque o F1-Score é menor que 0.5, ou seja, é pior que um classificador aleatório. O modelo não está nem identificando bem os positivos, nem sendo preciso quando identifica.


### 2.2 O dataset é balanceado ou desbalanceado? Como você descobriu?
Trata-se de um dataset balanceado, já que a variável target (respondeu_campanha), com dois valores possíveis, tem uma distribuição de 56% / 44%, próxima de 50% / 50%.


### 2.3 Por que usamos F1-Score e não apenas Accuracy neste caso?
Uma acurácia de 55.5% pode parecer indicar que o modelo acerta acima da média, mas a mesma acurácia seria observada se o modelo simplesmente previsse apenas 0 (que tem uma frequência de 56,06%).

---

## Parte 3: Validação de Dados

### 3.1 Liste as validações Pandera que você implementou:

1. cliente_id: Column(int, nullable=False, unique=True)
2. idade: Column(int, Check.in_range(18, 80))
3. renda_mensal: Column(float, Check.in_range(1000.0, 50000.0))
4. score_credito: Column(float, Check.in_range(300.0, 850.0))
5. respondeu_campanha: Column(int, Check.isin([0, 1]))

### 3.2 Por que validar dados ANTES de treinar o modelo?
Dados inválidos poderiam distorcer o resultado, identificando padrões incoerentes, inconsistentes e, consequentemente, inúteis.

---

## Parte 4: Versionamento

### 4.1 Liste os commits que vocês fizeram (copie do git log):
<!-- Execute: git log --oneline e cole aqui -->
```
(cole o output do git log aqui)
```

### 4.2 Por que mensagens de commit descritivas são importantes?

Mensagens de commit padronizadas e descritivas são impotantes aspectos do versionamento de uma base de códigos. Sem essas características a manutenabilidade da base é importantemente comprometida. Permite que mesmo equipes que não tem familiaridade com aquele código entenda o que foi alterado, quando e por quem sem precisar analisar diretamente o código, facilitando a revisão do código, a localização de alterações prejudiciais, de features promovidas em momento errado ou mesmo saber onde realizar alterações quando necessário. Permitem ainda um rapido retorno da aplicação a um estado anterior, permitindo a entrada em produção com o isolamento do código indesejado.
---

**Data de entrega:** 16/12/2025
