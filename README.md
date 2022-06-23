# projet INSEE
– Ce projet permettra d'interroger l'API et extraire le SIRET des établissements en fonction de leurs Raison sociale et le Code postale
puis mettre à jour le fichier EXCEL en remplaçant les cellules dont les valeurs de SIRET sont nulles par le numéro trouvé avec la requête
d’interrogation qui combine deux critères :denominationUniteLegale  et  codePostalEtablissement



–parmi les packages qu'il faut installer pour démarrer ce projet en plus de api-insee on cite  : csv ,pandas ,api_insee.criteria pour utliser :
FieldExact et Periodic , openpyxl.

–Afin d'interroger cet API il faut en premier créer un compte consommateur sur api.insee.fr. Puis récupérer les clés consommateur et secrète.
Depuis le Terminal installer la bibliothèque python api-insee via la commande :pip install api-insee.
## Pré-requis :
Il faut au préalable avoir un python déjà installé dans la machine.

J'ai utilisé python 3 , les versions précédentes peuvent poser des problèmes .
#
OS X

Nous vous conseillons d'installer la distribution Anaconda. Elle contient tous les modules et packages nécessaires. Elle est disponible pour toutes les plateformes et possède une procédure d'installation assez simple. Vous pouvez la télécharger depuis http://continuum.io/downloads. Des détails pour l'installation peuvent être trouvés ici : http://docs.continuum.io/anaconda/install.html

Une fois installée, tapez ensuite

conda create -n cours-python

suivi de

source activate cours-python

Cette dernière active un environnement de python qui nous permet de ne pas modifier l'environnement général de votre ordinateur.


#
Linux
Ouvrez un terminal et tapez :
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
Mise en place d’un environnement virtuel :
sudo apt install -y python3-venv




# Installer les packages :

- tout simplement avec pip : qui est installer automatiquement sous python

exemple :
pip install api-insee

pip install openpyxl
 - ou en tapant dans le terminal :
 pip install -r requirements.txt
Cela installera les packages nécessaires .

# Fabriqué avec :
les logiciels que j'ai utilisé sont :

Visual Studio Code :  avec son éditeur de text avancé , son explorateur des fichiers qui permet de naviguer facilement et organiser correctement
mon projet , terminal intégré qui gère simultanément plusieurs lignes de commandes  en plus il peut même fonctionner avec GitHub


LibreOffice Calc
# Exécution de travail



   



