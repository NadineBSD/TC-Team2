try:
    connection = psycopg2.connect(
        database="Training camp DB",     # Nom de la base de données
        user="postgres",         # Nom d'utilisateur PostgreSQL
        password="",     # Remplacez par votre mot de passe PostgreSQL
        host="localhost",        # Adresse du serveur PostgreSQL
        port="5432"              # Port PostgreSQL (5432 par défaut)
    )
    print("Connexion établie avec succès !")
except psycopg.Error as e:
    print("Erreur lors de la connexion à la base de données :", e)