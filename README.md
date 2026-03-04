# Engenharia de Dados e Big Data - CESAR School 
Este repositório armazena as atividades desenvolvidas na disciplina de Engenharia de Dados e Big Data.

## 📁 Atividade 01: Extração e Persistência de Dados (API Hipolabs)

O objetivo desta atividade foi extrair dados JSON de universidades e persistir em um banco relacional (SQLite).

### 1. Modelagem Proposta

A tabela `universidades` contém os campos: `id` (PK), `nome` (Unique), `pais`, `codigo_iso`, `estado_provincia` e `site_web`. 

**Decisão Técnica:** Para garantir a normalização (3NF) em escala real, domínios e sites seriam movidos para tabelas separadas (1:N), evitando campos multivalorados e redundância de strings.

### 2. Estratégia para Escala (Múltiplos Países)

Para lidar com dados de vários países mantendo a consistência e performance:
* **Idempotência:** Uso de `INSERT OR REPLACE` para evitar duplicidade em re-execuções.
* **Tratamento de Nulos:** Uso do método `.get()` para o campo `state-province`, garantindo a robustez da carga mesmo com dados ausentes.
* **Performance:** Criação de **Índices** nas colunas `pais` e `codigo_iso` para otimizar consultas em grandes volumes de dados.

---

## 🛠️ Como Executar
1. Instale as dependências: `pip install requests`
2. Execute o script: `python Main.py`

---
**Estudante:** Ylson Santos Queiroz Filho  
**Professor:** Marco Aurelio Tomaz Mialaret Junior