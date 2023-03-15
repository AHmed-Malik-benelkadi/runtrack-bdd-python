import mysql.connector

# se connecter à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Kiko2002=",
  database="LaPlateforme"
)

# créer un curseur pour exécuter des requêtes SQL
mycursor = mydb.cursor()

# exécuter la requête pour récupérer tous les étudiants
mycursor.execute("SELECT * FROM etudiants")

# afficher les résultats
for etudiant in mycursor.fetchall():
    print(etudiant)

