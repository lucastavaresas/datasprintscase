# datasprintscase
Teste Técnico de Engenharia de Dados para estágio data sprints

Afim de resolver a primeira questão dada, tive o seguinte raciocínio:   
Transformar a string em uma lista, logo em seguida fazer um loop que vá em todos os indexes contando a quantidade de letras iguais ao respectivo index, logo
ápos isto verificar se em algum index contado teria o valor 1, significando em apenas uma letra igual, e retornar esse index na lista fazendo com que saísse o resultado desejado.

OBS: como foi pedido apenas a primeira letra que não se repete, não tivermos que nos preocupar com as demais, e como um loop segue a ordem da lista o primeiro index que resultasse em 1 seria o resultado desejado.


Afim de resolver a segunda questão dada, tive o seguinte raciocínio:    
Primeiro era se necessário importar nosso arquivo csv, podemos fazer isso utilizando o pandas.read_csv(), logo ápos senti a necessidade de visualizar os dados afim de ter uma noção aonde nossa média de cada espécie ficaria, e como os dados se comportavam entre se. Utilizando a biblioteca Seaborn utilizei o seaborn.pairplot() para termos uma visão mais geral dos dados, e para trabalharmos com a média o melhor tipo de plotagem seria o seaborn.boxplot(), pórem por preferência pessoal também utilizei o seaborn.scatterplot(). Logo em seguida usei o Describe para ter uma ideia melhor do respectivo dado, separei os dados em df0 (para setosa), df1 (para versicolor) e df2 (para virginica) fiz as medias pedidas (utilizando df.mean()) na qual chamei de petal_length_media_setosa, petal_length_media_versicolor e petal_length_media_virginicas, e finalmente printei todos os resultados utilizando a função print.
