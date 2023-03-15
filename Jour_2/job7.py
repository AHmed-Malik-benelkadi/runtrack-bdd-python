import mysql.connector

class EmployeDB:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE employes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255) NOT NULL,
                prenom VARCHAR(255) NOT NULL,
                salaire DECIMAL(10, 2) NOT NULL,
                id_service INT NOT NULL,
                FOREIGN KEY (id_service) REFERENCES services(id)
            )
        ''')
        self.conn.commit()

    def insert_employe(self, nom, prenom, salaire, id_service):
        sql = '''
            INSERT INTO employes (nom, prenom, salaire, id_service)
            VALUES (%s, %s, %s, %s)
        '''
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def get_employes(self):
        self.cursor.execute('SELECT * FROM employes')
        result = self.cursor.fetchall()
        return result

    def update_employe(self, id, nom=None, prenom=None, salaire=None, id_service=None):
        if nom:
            self.cursor.execute('UPDATE employes SET nom=%s WHERE id=%s', (nom, id))
        if prenom:
            self.cursor.execute('UPDATE employes SET prenom=%s WHERE id=%s', (prenom, id))
        if salaire:
            self.cursor.execute('UPDATE employes SET salaire=%s WHERE id=%s', (salaire, id))
        if id_service:
            self.cursor.execute('UPDATE employes SET id_service=%s WHERE id=%s', (id_service, id))
        self.conn.commit()

    def delete_employe(self, id):
        self.cursor.execute('DELETE FROM employes WHERE id=%s', (id,))
        self.conn.commit()
# Créer une instance de la classe EmployeDB
db = EmployeDB('localhost', 'user', 'password', 'ma_base_de_donnees')

# Créer la table "employes"
db.create_table()

# Insérer un employé
db.insert_employe('Doe', 'John', 3500.50, 1)

# Récupérer tous les employés
employes = db.get_employes()
for employe in employes:
    print(employe)

# Mettre à jour un employé
db.update_employe(1, salaire=4000.00)

# Supprimer un employé
db.delete_employe(1)

# Fermer la connexion
db.update_employe(1, {'nom': 'Smith', 'prenom': 'Jane', 'salaire': 4500.00, 'id_service': 2})

# Fermer la connexion
db.delete_all_employes()



# Path: Jour_2\job8.py

