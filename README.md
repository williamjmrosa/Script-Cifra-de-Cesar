# Script-Cifra-de-Cesar

## Instruções para execução

- 1º deixar o Script na mesma pasta do arquivo que deseja cifrar/decifrar
- 2º Executar o cmd do Windows
- 3º Navegar os diretorios pelo cmd com o comando cd até a pasta que se encontra os arquivos
- 4º Executar o comando de execução do script exemplo mais abaixo
- 5º ver o resultado
<br>OBS: arquivo para ler não pode ter "-" com exeção do que serve para separar o cifra/decifra do nome do arquivo original
<br>EX:cifrar-livroxxx.txt
### Legenda

- <script\> nome do arquivo "nome do script.py" 
- <localArquivo\> nome arquivo txt que sera cifrado ou decifrado
- <senha\> senha para cifrar e decifrar o arquivo
- <tipo\> entrada do que fazer "cifrar" ou "decifrar"

### Exemplo de comando no CMD Windows

EX: python <script\> <localArquivo\> <senha\> <tipo\>
<br>
EX: python "Script Cifra de César.py" texto.txt "codifica" cifrar
<br>
EX: python "Script Cifra de César.py" texto.txt "codifica" decifrar

### Funcionamento 

O Codigo do Script Cifra de César tem 5 funções para funcionar corretamente 
<br> e 5 atributos globais.
<br> 
### Atributos globais
![Atributo caracteres](https://user-images.githubusercontent.com/24362264/206929595-20827bb3-dd02-46f7-a089-17351270f65f.PNG)

Na imagem acima está representada a string que contem todos os caracters que podem ser cifrados
<br>que este atributo é um diferencial da cifra de Cesar padrão que possui o alfabeto.

![Atributo entrada](https://user-images.githubusercontent.com/24362264/206929643-43454251-4901-46ba-80cb-c2ebfe6d3e2b.PNG)

Na imagem acima está representado 4 atributos que represtando o tamanho da string de caracteres, 
<br>localArquivo que vai ser cifrado/decifrado, senha do arquivo que serve para calcular o deslocamento,
<br>tipo para dizer se o arquivo vai ser cifrado ou decifrado.
<br>Esse atributos estão dentro de um if que serve para ver se o numero de entradas é o necessario para
<br>executar o script e recebe os valores e chama a função ler() e se não tiver as entradas mostra mensagem de erro.

### Função deslocamento

![Função Deslocamento](https://user-images.githubusercontent.com/24362264/206931084-3da30b03-d20a-48b3-9445-8506b2be50f1.PNG)

Na imagem acima está a função deslocamento() que outro diferencial ela pega o atributo global senha e no primeiro if descobre o,
<br>equivalente numerico para deslocamento que é feito convertendo cada caracter da senha no codigo da
<br>tabela ASCII e somando ao atributo local numero inicializado em zero depois passa esse atributo de 
<br>devolta pra senha no segundo if usando recursividade pra calcular a equivalencia da senha do deslocamento
<br>da string de caracteres e atualiza o atributo global senha com o deslocamento equivalente.

### Função cifrar

![Função cifrar](https://user-images.githubusercontent.com/24362264/206931798-acae1269-4702-4348-97f3-434da31258b3.PNG)

Na imagem acima temos a função cifrar que recebe por parametro um unico caracter para ser cifrado e o deslocamento
<br>para calcular o caracter cifrado e retornar ele e se o caracter não existir no atributo caracteres ele não sera cifrado e retorna
<br> ele mesmo.

### Função decifrar

![Função decifrar](https://user-images.githubusercontent.com/24362264/206932087-bcf678b4-983e-4227-813e-0dd89aa6937c.PNG)

Na imagem acima temos a função decifrar que recebe o caracter para decifrar e o deslocamento para decifrar o caracter e
<br> retonar ele e se o caracter não existir ele não é decifrado e retorna ele mesmo.

### Função criarArquivo

![Função criarArquivo](https://user-images.githubusercontent.com/24362264/206932407-0cb20aa0-bfb5-459d-b66f-2802e147b0fd.PNG)

Na imagem acima temos a função de criar um arquivo novo depois de cifrar ou decifrar o arquivo lido.

### Função ler

![Função ler](https://user-images.githubusercontent.com/24362264/206932474-9355d493-f5b9-4681-94e0-2531654efc20.PNG)

Na imagem acima temos a função ler que é responsavel por abrir o arquivo que vai ser cifrado/decifrado e atraves de
<br> um try verificar se o arquivo foi aberto e se não for disparar um erro. Também inicia a função que calcula o
<br>deslocamento e depois faz o if elif else pra ver se vai cifra ou decifrar e mensagem se entrada for invalida dentro
<br> dentro do if elif é feito um for para ler o arquivo caracter por caracter e passar cada caracter pela função
<br>cifra/decifrar dependendo de onde entrou e retornar o caracter cifrado/decifrado para o atributo local cifra
<br>uma vez lido todo o arquivo ele é salvo num novo arquivo com a função criar arquivo.
