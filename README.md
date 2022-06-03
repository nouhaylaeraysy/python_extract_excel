# python_extract_excel
– Ce projet permettra d'interroger l'API et extraire le SIRET des établissements en fonction de leurs Raison sociale et le Code postale
puis mettre à jour le fichier EXCEL en remplaçant les cellules dont les valeurs sont nulles par le numéro SIRET trouvé  par la requête
d’interrogation qui combine deux critères :denominationUniteLegale  et  codePostalEtablissement



–parmi les packages qu'il faut installer pour démarrer ce projet en plus de api-insee on cite  : csv ,pandas ,numpy ,api_insee.criteria pour utliser :
FieldExact et Periodic , openpyxl.

–Afin d'interroger cet API il faut en premier créer un compte consommateur sur api.insee.fr. Puis récupérer les clés consommateur et secrète.
Depuis le Terminal installer la bibliothèque python api-insee via la commande :pip install api-insee.
# Pré-requis :
il faut au préalable avoir  python déjà installé dans la machine.

# Installer les packages : 

- tout simplement avec pip : qui est installer automatiquement sous python 

exemple : 
pip install api-insee

pip install openpyxl


# Fabriqué avec :
les logiciels que j'ai utilisé sont : 

Visual Studio Code :  avec son éditeur de text avancé , son explorateur des fichiers qui permet de naviguer facilement et organiser correctement 
mon projet , terminal intégré qui gère simultanément plusieurs lignes de commandes  en plus il peut même fonctionner avec GitHub


LibreOffice Calc



   

