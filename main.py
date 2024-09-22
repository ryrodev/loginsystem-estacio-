import mysql.connector
from mysql.connector import Error

def conectar():
    """Conecta ao banco de dados MySQL."""
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Endereço do servidor MySQL
            database='login_system',  # Nome do banco de dados
            user='root',  # Usuário do MySQL
            password='sua_senha'  # Senha do MySQL
        )
        if connection.is_connected():
            print("Conexão realizada com sucesso!")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def verificar_login(username, password):
    """Verifica as credenciais de login no banco de dados."""
    try:
        connection = conectar()
        if connection:
            cursor = connection.cursor()
            # Consulta para verificar o login
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            if user:
                print(f"Login bem-sucedido! Bem-vindo, {username}.")
            else:
                print("Login falhou. Verifique suas credenciais.")
            cursor.close()
            connection.close()
    except Error as e:
        print(f"Erro durante o login: {e}")

if __name__ == "__main__":
    # Solicita o nome de usuário e senha do usuário
    username_input = input("Digite o nome de usuário: ")
    password_input = input("Digite a senha: ")

    # Verifica o login
    verificar_login(username_input, password_input)
