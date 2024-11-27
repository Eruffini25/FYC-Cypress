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
Cliquer E2E testing 
Choisir le navigateur
Cliquer sur Scaffold example specs

# Création du fichier pour test API
```shell
cd .\cypress\e2e\
New-Item -Path .\api-tests -ItemType Directory
New-Item -Path .\api-tests\api_test.cy.js -ItemType File
```

