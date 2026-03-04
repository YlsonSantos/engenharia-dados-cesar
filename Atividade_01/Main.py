import requests
import sqlite3

url = "http://universities.hipolabs.com/search?country=Brazil"
response = requests.get(url)
response.raise_for_status()
dados = response.json()

def salvar_dados(lista_universidades):
    conn = sqlite3.connect('universidades_cesar.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS universidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE,
            pais TEXT,
            codigo_iso TEXT,
            estado_provincia TEXT,
            site_web TEXT
        )
    ''')

    for uni in lista_universidades:
        cursor.execute('''
            INSERT OR REPLACE INTO universidades (nome, pais, codigo_iso, estado_provincia, site_web)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            uni['name'], 
            uni['country'], 
            uni['alpha_two_code'], 
            uni.get('state-province'),
            uni['web_pages'][0] if uni['web_pages'] else None
        ))

    conn.commit()
    conn.close()
    print("Processo concluído: Dados persistidos.")

salvar_dados(dados)