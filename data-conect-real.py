import psycopg2
from faker import Faker


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="senha",
    )

cursor = conn.cursor()

# fake = Faker('pt_BR')

# n=10
# for i in range(n):
#     codigo = i+10
#     nome = 'produto_'+str(i+1)
#     preco = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=5, max_value=1000)
#     comandoSQL = """INSERT INTO public.produto ("codigo", "nome", "preco") VALUES (%s, %s, %s)"""
#     registro = (codigo, nome, preco)
#     cursor.execute(comandoSQL, registro)
#     conn.commit()

#     conn.close

# cursor.close()