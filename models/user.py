class Usuario:
    def __init__(self, id, nome, senha):
        self.id= id
        self.nome = nome
        self.senha = senha

lst_usuarios=[]
user=Usuario("1","adm", "123")
lst_usuarios.append(user)
user=Usuario("2","laura", "321")
lst_usuarios.append(user)
