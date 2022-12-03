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
Depois temos a função deslocamento() responsavel por calcular o deslocamento,
<br> usando o atributo "<b>senha</b>" a função deslocamento() primeiro faz um if para verificar
<br> se atributo "<b>senha</b>" e uma string se for uma string tem um for para passar por cada
<br> caracter dessa string e ver qual o valor dele na tabela ASCII tendo esse valor ele é somado<br>
num atributo chamado "<b>numero</b>" que foi inicializado em 0 antes do for uma vez passado pelo for
<br> o atributo "<b>senha</b>" recebe o atributo numero "<b>numero</b>" e depois disso possui outro if
que é responsavel para descobrir qual é deslocamento que a senha tem dentro em relação ao atributo "<b>tamanho</b>"
<br>como uma função recursiva.
