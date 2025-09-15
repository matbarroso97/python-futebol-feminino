# Plataforma de Estatísticas do Futebol Feminino
**Sprint 3 - Computational Thinking with Python**

---

## Resumo do Projeto

Sistema desenvolvido em Python para demonstrar conceitos fundamentais de programação através de uma plataforma de estatísticas do futebol feminino. O sistema atende completamente aos requisitos do backlog apresentado.

### Objetivos Alcançados
- ✅ MVP funcional com cadastro de ligas e jogadoras
- ✅ Estatísticas completas de jogadoras
- ✅ Sistema de gestão de dados
- ✅ Interface intuitiva e responsiva

---

## Funcionalidades Implementadas

### 1. Gestão de Usuários
- **Cadastro e Login:** Sistema de autenticação com hash de senhas
- **Tipos de Usuário:** Administrador e usuário comum
- **Painel Administrativo:** Gestão completa de usuários

### 2. Cadastro de Dados
- **Jogadoras:** Cadastro completo com dados pessoais e do clube
- **Clubes:** Informações históricas e geográficas
- **Campeonatos:** Dados de competições e temporadas
- **Partidas:** Registro de jogos com placares
- **Eventos:** Gols, assistências, cartões, finalizações, defesas

### 3. Estatísticas e Rankings
- **Estatísticas Individuais:** Cálculo automático por jogadora
- **Rankings:** Artilheiras e assistências ordenadas
- **Comparação:** Análise lado a lado entre jogadoras
- **Busca:** Localização por nome

### 4. Interface do Usuário
- **Menus Intuitivos:** Navegação clara e organizada
- **Feedback Visual:** Confirmações e mensagens de erro
- **Informações do Sistema:** IDs e dados disponíveis

---

## Conceitos Python Demonstrados

### Entrada, Processamento e Saída
- **Entrada:** `input()` para dados do usuário
- **Processamento:** Cálculos de estatísticas e manipulação de dados
- **Saída:** `print()` formatado para exibição

### Estruturas de Decisão
- **if/elif/else:** Controle de fluxo em menus e validações
- **Condicionais:** Verificação de tipos de usuário

### Estruturas de Repetição
- **for:** Processamento de listas e dicionários
- **while:** Loop principal da aplicação
- **enumerate:** Numeração de rankings

### Listas e Dicionários
- **Listas:** Armazenamento de usuários, jogadoras, clubes
- **Dicionários:** Estruturação de dados com chaves-valores
- **Operações:** append(), busca, filtros, ordenação

### Funções
- **Modularização:** Código organizado em funções específicas
- **Reutilização:** Funções auxiliares para operações comuns

### Boas Práticas
- **Nomenclatura:** Nomes descritivos e consistentes
- **Comentários:** Documentação adequada do código
- **Organização:** Estrutura lógica e legível

---

## Funções Auxiliares e Bibliotecas Utilizadas

### Bibliotecas Padrão do Python

#### hashlib
**Propósito:** Geração de hashes para segurança de senhas e IDs únicos

**Funções utilizadas:**
- `hashlib.sha256()` - Cria hash SHA-256 para senhas
- `hashlib.md5()` - Gera IDs únicos para registros

**Exemplo de uso:**
```python
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def gerar_id():
    timestamp = str(datetime.datetime.now())
    return hashlib.md5(timestamp.encode()).hexdigest()[:8]
```

#### datetime
**Propósito:** Manipulação de datas e timestamps

**Funções utilizadas:**
- `datetime.datetime.now()` - Obtém data/hora atual

**Exemplo de uso:**
```python
timestamp = str(datetime.datetime.now())
```

### Funções Auxiliares Implementadas

#### gerar_id()
**Propósito:** Cria identificadores únicos para registros
**Implementação:** Combina timestamp atual com hash MD5
**Retorno:** String de 8 caracteres (ex: "a1b2c3d4")

#### hash_senha(senha)
**Propósito:** Criptografa senhas para segurança
**Implementação:** Usa SHA-256 para criar hash irreversível
**Retorno:** String hexadecimal de 64 caracteres

#### exibir_cabecalho(titulo)
**Propósito:** Formata cabeçalhos de seções com bordas visuais
**Implementação:** Cria linha de separação com "=" e emoji
**Uso:** Usado no menu principal para melhorar apresentação visual
**Exemplo de saída:**
```
============================================================
🏆 PLATAFORMA DE ESTATÍSTICAS DO FUTEBOL FEMININO
============================================================
```

### Segurança Implementada

#### Hash de Senhas
- **Algoritmo:** SHA-256 (Secure Hash Algorithm)
- **Características:** Irreversível, resistente a ataques
- **Implementação:** Senhas nunca armazenadas em texto plano

#### Geração de IDs
- **Método:** MD5 com timestamp
- **Características:** Único, não sequencial
- **Uso:** Identificação segura de registros

---

## Como Executar

### Comando
```bash
python plataforma_futebol_feminino.py
```

### Credenciais de Teste
- **Admin:** `admin@passaabola.com` / `admin123`
- **Usuário:** `usuario@teste.com` / `user123`

### Dados Disponíveis
- **Jogadoras:** jog_001 (Marta), jog_002 (Debinha), jog_003 (Tamires)
- **Clubes:** clube_001 (São Paulo), clube_002 (Flamengo), clube_003 (Corinthians)
- **Campeonatos:** camp_001 (Brasileirão), camp_002 (Copa do Brasil)

---

## Guia de Teste

### Teste Básico
1. Execute o sistema
2. Faça login como administrador
3. Navegue pelo menu principal
4. Teste visualização de estatísticas
5. Teste rankings e comparações

### Teste Administrativo
1. Acesse painel administrativo (opção 7)
2. Cadastre nova jogadora
3. Cadastre novo clube
4. Adicione evento a partida
5. Verifique estatísticas atualizadas

### Funcionalidades Específicas
- **Estatísticas:** Menu 1 → opção 2 → use ID jog_001
- **Rankings:** Menu 2 → teste artilheiras e assistências
- **Busca:** Menu 5 → digite "Marta" ou "Debinha"
- **Comparação:** Menu 6 → use jog_001 e jog_002
- **Informações:** Menu 8 → veja todos os IDs disponíveis

---

## Estrutura do Código

### Arquivo Principal
- **plataforma_futebol_feminino.py** (941 linhas)
- Classe principal: `SistemaFutebolFeminino`
- Sem dependências externas (apenas Python padrão)

### Componentes
- Sistema de autenticação
- Cálculo de estatísticas
- Interface do usuário
- Painel administrativo
- Funções de busca e comparação


---

## Conclusão

O sistema implementa com sucesso todos os requisitos propostos no backlog, demonstrando de forma prática os conceitos fundamentais de programação Python. A solução é funcional, bem documentada e adequada para fins acadêmicos.
