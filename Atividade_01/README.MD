# Atividade 01: Extração e Persistência de Dados (API Hipolabs)

Este projeto realiza o consumo de uma API REST de universidades e armazena os dados de forma estruturada em um banco de dados relacional.

### 1. Modelagem Proposta

A tabela `universidades` contém os campos: `id` (PK), `nome` (Unique), `pais`, `codigo_iso`, `estado_provincia` e `site_web`. 

**Decisão Técnica:** Para garantir a normalização (3NF) em escala real, domínios e sites seriam movidos para tabelas separadas (1:N), evitando campos multivalorados e redundância de strings.

### 2. Estratégia para Escala (Múltiplos Países)

Para lidar com dados de vários países mantendo a consistência e performance:
* **Idempotência:** Uso de `INSERT OR REPLACE` para evitar duplicidade em re-execuções do pipeline.
* **Tratamento de Nulos:** Uso do método `.get()` para o campo `state-province`, garantindo a robustez da carga mesmo com dados ausentes.
* **Performance:** Sugestão de criação de **Índices** nas colunas `pais` e `codigo_iso` para otimizar filtros em grandes volumes de dados.

---

## 🛠️ Como Executar no Windows

Siga estes passos no terminal (PowerShell) dentro desta pasta:

1. **Configurar o Ambiente Virtual:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```