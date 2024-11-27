# Install node et npm
## Vérifier version et installation
node --version 
npm --version
## Install node js et npm
Node js : https://nodejs.org/en
$env:Path -split ';'
$env:Path += ";C:\Program Files\nodejs"
$env:Path += ";C:\Users\xxxxxx\AppData\Roaming\npm"

# Install Cypress
## Initialiser le projet 
npm init -y
## Install Cypress
npm install cypress
## Ouvrir Cypress
npx cypress open
