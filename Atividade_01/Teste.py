import sqlite3

DB_NAME = 'universidades_cesar.db'

def pesquisar():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        print("\n=== SISTEMA DE BUSCA DE UNIVERSIDADES ===")
        termo = input("Digite o nome (ou parte do nome) da faculdade: ")

        query = "SELECT nome, pais, estado_provincia, site_web FROM universidades WHERE nome LIKE ?"
        cursor.execute(query, (f'%{termo}%',))
        
        resultados = cursor.fetchall()

        if resultados:
            print(f"\n✅ Foram encontradas {len(resultados)} faculdade(s):")
            print("-" * 50)
            for r in resultados:
                print(f"🏛️  Nome: {r[0]}")
                print(f"🌍 País: {r[1]}")
                print(f"📍 Estado: {r[2] if r[2] else 'Não informado'}")
                print(f"🌐 Site: {r[3]}")
                print("-" * 50)
        else:
            print(f"\n❌ Nenhuma faculdade encontrada com o nome '{termo}'.")
            print("Dica: Tente um nome mais curto (ex: em vez de 'Universidade Federal', tente apenas 'Federal')")

        conn.close()
    except Exception as e:
        print(f"❌ Erro ao acessar o banco: {e}")

if __name__ == "__main__":
    pesquisar()