import psycopg2

try:
    conn = psycopg2.connect(
    host = "localhost",
    port ="5435",
    database = "postgres-remindme", 
    user="remind", password = "123456")
    print('Connected.')

except Exception:
    print('Connection Failed')


if conn is not None:
    
    print('Connection YAY!')

    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE user (id serial, first_name VARCHAR(150)NOT NULL, email VARCHAR(150)UNIQUE NOT NULL, password varchar(150) NOT NULL, PRIMARY KEY(id));')

    cursor.execute('CREATE TABLE usuarios  (nome VARCHAR(15) NOT NULL, nickname VARCHAR(30)NOT NULL, senha VARCHAR(30)NOT NULL,  PRIMARY KEY(nickname) );')
    print('Sua tabela usuario foi criada!')

    conn.commit()
    cursor.close()
    conn.close()