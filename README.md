        ALUNOS: 
    Joao Pedro H Neves
    Davi Fiori

ENGENHARIA DE SOFTWARE - FAG Toledo 6º Período

main.py:



a) O histograma sugere distribuição simétrica ou assimétrica?

O histograma do teor alcoólico no vinho sugere uma distribuição assimétrica.

    Justificativa: A cauda da distribuição se estende mais para a direita, 
    indicando uma assimetria positiva (ou à direita). 
    A maior parte dos vinhos se concentra em teores alcoólicos mais baixos 
    (em torno de 9.5% a 10%), com uma frequência decrescente para valores mais altos de álcool.

b) Há outliers de pH em alguma classe de quality? Comente.

Não, o gráfico boxplot fornecido não mostra a presença de 
outliers de pH em nenhuma das classes de qualidade do vinho.

    Justificativa: No código em Python utilizado para gerar este gráfico, 
    o parâmetro showfliers=False foi utilizado na função sns.boxplot(). 
    Este parâmetro instrui a biblioteca a não exibir os outliers no gráfico. 
    Portanto, embora possam existir outliers nos dados originais, eles foram 
    deliberadamente omitidos da visualização.

