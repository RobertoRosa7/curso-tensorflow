# O que é aprendizado de máquina?

> Aprendizado de máquina é o campo da programação de computadores de modo que else apredem sem explicitamente programá-los. - Arthur Samuel, 1959

### Por que usar aprendizado de máquina:

- Problemas para os quais as soluções atuais exigem muitos ajustes finos ou extensas listas de regras.
- Problemas complexos para os quais não existe uma boa solução.
  adaptabilidade de ambiente: um sistema de AM pode se adaptar a novos dados.
- Entendimento de problemas complexos e de grande quantidades de dados.

### Tipos de sistemas do aprendizado de máquina:

- **Aprendizado Supervisionado**: Principal característica é a existência de "labels" ou "rótulos" nos dados de treinamentos com a classificação

  - K-ésimo vizinho mais próximo.
  - Regressão Linear.
  - Regressão Logística.
  - Máquina de vetores de suporte (SVM).
  - Árvore de decisão e floresta aleatória.

- **Aprendizado não Supervisionado**:
  São dados de treinamentos não rotulados, sistema tenta aprender sem um professor.

  - Clusterização:
    - K-Means (clusterização por média)
    - DBScan (clusterização baseada em densidade de aplições com ruído)
    - Análise de cluster hierárquica (HCA)
    - Detecção de anomalias e de novidades
    - One-class SVM
  - Floresta de isolamento
  - Visualização e redução de dimensionalidade
  - Análise de Componentes Pricipais (ACP)
  - Kernel ACP
  - LLE (método de redução de dimensionalidade não linear)
  - t-SNE (método de incorporação estocástico de vizinhos distribuídos)
  - Aprendizado de regra por associação
  - Apriori
  - Eclat

- **Aprendizado Semisupervisionado**: Existe alguns dados de treinamentos rotulados e outros não.

- **Aprendizado por Reforço**: Também conhecido como aprendizado "agente" neste contexto a AM pode assistir selecionar e executar acões e obter "recompensas ou penalidades" na forma de recompensas negativas

- **Aprendizado em batch e online**: Aprendizado em batch é incapaz de aprender de forma incremental, primeiro é treinado offline e depois disponível online em produção, e não aprende mais nada, isso se chama aprendizado offline.

- **Aprendizado online**: No aprendizado online, um modelo é treinado e disponibilizado em produção e em seguida, continua aprendendo à medida que novos são recebidos. `out-of-core` o algoritmo faz upload de parte dos dados, executa uma etapa do treinamento nesses dados repete o processo até ele tenha sido executado em todos os dados.

- **Aprendizado por instância**: O sistema aprende por meio de memorização e depois generaliza em novos casos, ao aplicar uma medida de similiaridade a fim de compará-los a outros exemplos aprendido

- **Aprendizado por modelo**: Modelo de generalização que se basea em predições

### Princiapias desafios do aprendizado de máquina

Dados ruins ou algoritmos ruins

### Sobreajuste dos dados de treinamento (solução)

- _Simplificar o modelo com um que tenha menos parâmentros_
- _Reduzir o número de atributos nos dados de treinamento ou restringir_
- _Coletar mais dados de treinamento_
- _Reduzir_ o ruído nos dados de treinamento (outliiers, dados nulos ou incompletos)
  - _Pré-processamento:_ consite em limpar, transformar normalizar e padronizar os dados antes de usá-los.
  - _Validação cruzada:_ consiste em dividir os dados em subconjuntos e usar um delespara testar o modelo treinado com os demais.
  - _Regularização:_ consiste em adicionar um termo à **função de custo** do modelo que penaliza a complexidade do modelo e evita o **overfitting**. L1, L2, Dropout
  - _Aumento de dados_: consiste em gerar novos dados a partir dos existêntes.
    - _rotação_
    - _translação_
    - _ruído_

### Subajuste dos dados de treinamento (solução)

- _Selecionar novo modelo com mais parâmetros_
- _Alimentar o algoritmo de AM com melhores característica (feature engeneering)_
- _Reduzir hiperparâmetro de regularização_

### Teste e Validação

### Vocabulário:

- `out-of-core`: parte dos dados são passado para o aprendizado continuo.
- `taxa-de-aprendizagem`: é a rapidez com o AM deve se adaptar às mudanças dos dados.
- `generalização`: aprendizado baseado em instância e aprendizado baseado em modelo.
- `medida-de-similiaridade`: indica o quanto de características comuns são encontradas.
- `função-de-utilidade`: usado para decidir quais valores funcionarão melhor com o medelo.
- `função-de-avaliação`: usado para saber o quanto o bom é o modelo.
- `função-de-custo`: usando para saber o quanto ruim é o modelo.
- `viés de amostragem`: quantidade de amostragem muito grande.
- `ruído de amostragem`: quantidade de amostragem muito pequena.
- `feature engeneering`: processo no qual criá-se um conjunto de característica relevantes.
- `sobreajustes dos dados de treinamentos`: o modelo funciona muito bem nos dados de treinamento, mas não generaliza muito bem. Ocorre quando o modelo é muito complexo em relação à quantidade de dados e ao ruído dos dados de treinamentos.

### Equações:

> simples model linear:  
> satisfacao_de_vida = $\theta_0+\theta_1 2 \times  PIB$
