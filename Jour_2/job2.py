import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Kiko2002=",
  database="LaPlateforme"
)

# Création du curseur
mycursor = mydb.cursor()

# Exécution de la requête
mycursor.execute("SELECT nom, capacite FROM salles")

# Récupération des résultats
resultats = mycursor.fetchall()

# Affichage des résultats
for resultat in resultats:
  print(resultat[0],':', resultat[1])

# Fermeture de la connexion à la base de données
mydb.close()
