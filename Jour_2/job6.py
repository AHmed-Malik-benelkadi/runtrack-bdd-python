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
mycursor.execute("SELECT SUM(capacite) FROM salles")

# Récupération du résultat
resultat = mycursor.fetchone()[0]

# Affichage du résultat
print("La capacité totale des salles est de", resultat)

# Fermeture de la connexion à la base de données
mydb.close()
