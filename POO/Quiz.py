# Classe 
# class User → é uma classe, ou seja, um molde que serve para criar usuários.
class User:
    # self é a referência ao próprio objeto
    # def __init__ → é um método que define como o usuário vai ser criado, com os dados que ele precisa (ID, nome, etc.).
    # self → é a referência ao próprio usuário que está sendo criado. Serve para guardar e acessar os dados dele.
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0 # seguidores
        self.following = 0 # seguido


    def follow(self, user):
        user.followers += 1
        user.following += 1

# Criação do objeto
# user_1 = User(...) → cria um usuário de verdade a partir do molde.
user_1 = User(user_id="001", username="Jesus Cristo")
user_2 = User(user_id="002", username="João Batista")
user_3 = User(user_id="003", username="Rei Davi")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
