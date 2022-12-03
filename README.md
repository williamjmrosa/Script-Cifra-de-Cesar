# Script-Cifra-de-Cesar

## Instruções para execução

- 1º deixar o Script na mesma pasta do arquivo que deseja cifrar/decifrar
- 2º Executar o cmd do Windows
- 3º Navegar os diretorios pelo cmd com o comando cd até a pasta que se encontra os arquivos
- 4º Executar o comando de execução do script exemplo mais abaixo
- 5º ver o resultado


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
<br>
e um if else para vefiricar a falta de entradas.
<br>
No inicio do codigo em um atributo chamado "<b>caracteres</b>" ele é uma string que
<br>
tem quase todos os caracteres visiveis da tabela ASCII que também é um dos 
<br>
diferenciais da cifra césar padrão onde só tem o alfabeto de a-z.
<br>
o codigo também tem 4 outros atributos esses atributos são eles "<b>tamanho</b>" que 
<br>
receber o tamanho da string de "<b>caracteres</b>", o atributo "<b>localArquivo</b>" 
<br>
recebe o nome do arquivo de texto, o atributo "<b>senha</b>" recebe uma palavra 
<br>
ou frase que servira para calcular o deslocamento para cifrar e decifrar o arquivo,
<br>
 o atributo "<b>tipo</b>" recebe a palavra cifrar ou decifrar.
<br>
<br>Depois temos a função <b>deslocamento()</b> responsavel por calcular o deslocamento,
<br> usando o atributo "<b>senha</b>" a função "<b>deslocamento</b>" primeiro faz um if para verificar
<br> se atributo "<b>senha</b>" e uma string se for uma string tem um for para passar por cada
<br> caracter dessa string e ver qual o valor dele na tabela ASCII tendo esse valor ele é somado
<br> num atributo chamado "<b>numero</b>" que foi inicializado em 0 antes do for uma vez passado pelo for
<br> o atributo "<b>senha</b>" recebe o atributo numero "<b>numero</b>" e depois disso possui outro if
<br> que é responsavel para descobrir qual é deslocamento que a senha tem dentro em relação ao<br>
atributo "<b>tamanho</b>" como uma função recursiva.
<br><br>Depois a função <b>cifrar(caracter,desloca)</b> essa função recebe um "<b>caracter</b> do arquivo de texto,
<br> e o "<b>desloca</b>" que é a "<b>senha</b>" após calcular o deslocamento com essas informações 
<br> é e visto o equivalente a letra passada e retornada a nova e se não existir a a letra no atributo
<br>"<b>caracteres</b>" ele retorna a propria letra.
<br><br>A proxima é a função "<b>decifrar(caracter,desloca)</b>" ela faz o mesmo que a função cifrar, mas quando
<br>faz o deslocamento em vez de soma sobtrair o deslocamento
<br><br>A função "<b>criarArquivo(nome,texto_cifrado)</b>" tem o atributo "<b>nome</b>" que é o nome do
<br>arquivo a ser criado e o atributo <b>texto_cifrado</b> que é o texto que foi cifrado ou decifrado,
<br>para ser salvo no arquivo.
<br><br>A função "<b>ler()</b>" é responsavel por pegar os atributos inseridos via linha de comando quando
<br>o script foi executado e começar a trabalhar com eles primeiro chamando a função "<b>deslocamento()</b>"
<br> pra calcular o deslocamento do atributo "<b>senha</b>",depois abrir o arquivo usando o 
<br>atributo "<b>locaArquivo</b>" sendo verificado se arquivo existe senão existir volta 
<br>mensagem de "<b>Arquivo não existe</b>" e o script encerra a execução,
<br>caso exista é feito um if para verificar se é para cifrar se for tem um for
<br> que lê o arquivo caracter a caracter e passa passa para função cifrar que retorna o caracter
<br> cifrado e passa um atributo chamado "<b>cifra</b>" o elif faz a mesma coisa que o if só que
<br> verificado para decifrar e o else é causa não tenha a entra da certa
<br> retorna a mensagem "<b>Entrado do que fazer errada</b>" e termina a exucução do script.
