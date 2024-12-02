import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Désactiver les avertissements liés à la désactivation de la vérification SSL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def obtenir_token():
    url = 'https://parfums-esgi.store/api/login'
    payload = {
        'username': 'XXXXX',
        'password': 'XXX'
    }
    try:
        # Envoyer la requête POST sans vérifier le certificat SSL
        response = requests.post(url, json=payload, verify=False)
        if response.status_code == 200:
            data = response.json()
            token = data.get('token')
            if token:
                print(f"Jeton d'authentification : {token}")
            else:
                print("Le jeton n'a pas été trouvé dans la réponse.")
        else:
            print(f"Échec de la connexion : {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")

if __name__ == "__main__":
    obtenir_token()
