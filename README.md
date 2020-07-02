# Projeto para testar e aprender os comandos GIT

Primeiro deve-se criar um novo repositorio no Github. Depois clona
o repositorio (copia o https) e no terminal do pycharm digita o 
seguine comando no terminal:
```bash
git remote origin <url do projeto>
```
origin e o nome convencional que se da a um remoto.

Para trazer os arquivos do repositorio do Github para a maquina:
```
git fetch origin
git merge origin/master
```
Aqui o master refere-se ao branch, caso esteja trabalhando com 
outro, deve-se colocar o nome dele no lugar do master

Nesse momento ja posso começar a trabalhar com o projeto
e quando tiver algumas alteraçoes que desejo comittar, posso
fazer da seguinte forma:

```bash
git add . #ou o caminho do arquivo em que houve alteraçao
git commit
```
Para upar as alteraçoes no Github basta:
```bash
git push origin master
```
