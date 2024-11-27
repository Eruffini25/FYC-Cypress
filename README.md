# Install node et npm
## Vérifier version et installation
```shell
node --version 
npm --version
```
## Install node js et npm
Node js : https://nodejs.org/en
```shell
$env:Path -split ';'
$env:Path += ";C:\Program Files\nodejs"
$env:Path += ";C:\Users\xxxxxx\AppData\Roaming\npm"
```

# Install Cypress
## Initialiser le projet 
```shell
npm init -y
```
## Install Cypress
```shell
npm install cypress
```

# Ouvrir Cypress
```shell
npx cypress open
```

