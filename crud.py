import psycopg2


class AppDB:
    def __init__(self):
        pass

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(
                user='postgres',
                host="localhost",
                database="postgres",
                password="senha"
            )
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao conectar: ", error)

    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            sql_select_query = """select * from public.produto"""

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Falha ao selecionar dados: ", error)

        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
            return registros

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO public.produto ("codigo", "nome", "preco") values (%s, %s, %s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso!")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao inserir dados: ", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o postgre foi fechada.")

    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            sql_select_query = """select * from public.produto where "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)

            if record:
                sql_update_query = """Update public.produto set "nome" = %s, "preco" = %s where "codigo" = %s"""
                cursor.execute(sql_update_query, (nome, preco, codigo))
                self.connection.commit()
                count = cursor.rowcount
                print(count, "Registro atualizado com sucesso!")
                sql_select_query = """select * from public.produto where "codigo" = %s"""
                cursor.execute(sql_select_query, (codigo,))
                record = cursor.fetchone()
                print(record)
            else:
                print("Registro não encontrado")
        except (Exception, psycopg2.Error) as error:
            print('Error', error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o postgre foi fechada.")

    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = """Delete from public.produto where "codigo" = %s"""
            cursor.execute(sql_delete_query, (codigo,))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso!")
        except (Exception, psycopg2.Error) as error:
            print('Error', error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o postgre foi fechada.")
