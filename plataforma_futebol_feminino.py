"""
Plataforma de Estatísticas do Futebol Feminino
Sprint 3 - Computational Thinking with Python

Sistema desenvolvido para demonstrar conceitos fundamentais de programação:
- Entrada, processamento e saída de dados
- Estruturas de decisão e repetição
- Listas e dicionários
- Funções e modularização
- Interface intuitiva
"""

import hashlib
import datetime

# =============================================================================
# CONSTANTES E CONFIGURAÇÕES
# =============================================================================

# Tipos de usuário
TIPO_ADMIN = "admin"
TIPO_USUARIO = "usuario"

# Tipos de eventos em partidas
EVENTO_GOL = "gol"
EVENTO_ASSISTENCIA = "assistencia"
EVENTO_CARTAO_AMARELO = "cartao_amarelo"
EVENTO_CARTAO_VERMELHO = "cartao_vermelho"
EVENTO_FINALIZACAO = "finalizacao"
EVENTO_DEFESA = "defesa"

# =============================================================================
# FUNÇÕES AUXILIARES
# =============================================================================

def gerar_id():
    """Gera um ID único para registros"""
    timestamp = str(datetime.datetime.now())
    return hashlib.md5(timestamp.encode()).hexdigest()[:8]

def hash_senha(senha):
    """Cria hash da senha para segurança"""
    return hashlib.sha256(senha.encode()).hexdigest()

def exibir_cabecalho(titulo):
    """Exibe cabeçalho formatado"""
    print("\n" + "="*60)
    print(f"🏆 {titulo}")
    print("="*60)

# =============================================================================
# SISTEMA PRINCIPAL
# =============================================================================

class SistemaFutebolFeminino:
    """Sistema principal da plataforma de estatísticas"""
    
    def __init__(self):
        # Listas para armazenar dados (conceito de listas)
        self.usuarios = []
        self.jogadoras = []
        self.clubes = []
        self.campeonatos = []
        self.partidas = []
        self.eventos = []
        self.usuario_logado = None
        
        # Inicializa dados de exemplo
        self.inicializar_dados_exemplo()
    
    def inicializar_dados_exemplo(self):
        """Inicializa dados de exemplo para demonstração"""
        # Usuários de exemplo
        self.usuarios = [
            {
                'id': 'admin_001',
                'email': 'admin@passaabola.com',
                'senha_hash': hash_senha('admin123'),
                'nome': 'Administrador',
                'tipo': TIPO_ADMIN,
                'ativo': True
            },
            {
                'id': 'user_001',
                'email': 'usuario@teste.com',
                'senha_hash': hash_senha('user123'),
                'nome': 'Usuário Teste',
                'tipo': TIPO_USUARIO,
                'ativo': True
            }
        ]
        
        # Clubes de exemplo
        self.clubes = [
            {
                'id': 'clube_001',
                'nome': 'São Paulo FC Feminino',
                'cidade': 'São Paulo',
                'estado': 'SP',
                'pais': 'Brasil',
                'fundacao': 1930,
                'cores': ['vermelho', 'branco', 'preto'],
                'ativo': True
            },
            {
                'id': 'clube_002',
                'nome': 'Flamengo Feminino',
                'cidade': 'Rio de Janeiro',
                'estado': 'RJ',
                'pais': 'Brasil',
                'fundacao': 1895,
                'cores': ['vermelho', 'preto'],
                'ativo': True
            },
            {
                'id': 'clube_003',
                'nome': 'Corinthians Feminino',
                'cidade': 'São Paulo',
                'estado': 'SP',
                'pais': 'Brasil',
                'fundacao': 1910,
                'cores': ['preto', 'branco'],
                'ativo': True
            }
        ]
        
        # Jogadoras de exemplo
        self.jogadoras = [
            {
                'id': 'jog_001',
                'nome': 'Marta Vieira da Silva',
                'posicao': 'Atacante',
                'clube_id': 'clube_001',
                'numero_camisa': 10,
                'idade': 37,
                'nacionalidade': 'Brasileira',
                'altura': 1.63,
                'peso': 58.0,
                'ativa': True
            },
            {
                'id': 'jog_002',
                'nome': 'Debinha',
                'posicao': 'Atacante',
                'clube_id': 'clube_002',
                'numero_camisa': 7,
                'idade': 32,
                'nacionalidade': 'Brasileira',
                'altura': 1.57,
                'peso': 52.0,
                'ativa': True
            },
            {
                'id': 'jog_003',
                'nome': 'Tamires Cássia Dias',
                'posicao': 'Lateral',
                'clube_id': 'clube_003',
                'numero_camisa': 6,
                'idade': 35,
                'nacionalidade': 'Brasileira',
                'altura': 1.60,
                'peso': 55.0,
                'ativa': True
            }
        ]
        
        # Campeonatos de exemplo
        self.campeonatos = [
            {
                'id': 'camp_001',
                'nome': 'Brasileirão Feminino',
                'pais': 'Brasil',
                'temporada': '2024',
                'ativo': True
            },
            {
                'id': 'camp_002',
                'nome': 'Copa do Brasil Feminina',
                'pais': 'Brasil',
                'temporada': '2024',
                'ativo': True
            }
        ]
        
        # Adiciona partidas e eventos de exemplo
        self.adicionar_dados_exemplo()
    
    def adicionar_dados_exemplo(self):
        """Adiciona partidas e eventos de exemplo"""
        # Partidas de exemplo
        self.partidas = [
            {
                'id': 'part_001',
                'clube_casa_id': 'clube_001',
                'clube_fora_id': 'clube_002',
                'campeonato_id': 'camp_001',
                'data': '2024-03-15',
                'placar_casa': 2,
                'placar_fora': 1,
                'finalizada': True
            }
        ]
        
        # Eventos de exemplo
        self.eventos = [
            {'id': 'evt_001', 'partida_id': 'part_001', 'jogadora_id': 'jog_001', 'tipo': EVENTO_GOL, 'minuto': 15, 'observacoes': 'Gol de falta'},
            {'id': 'evt_002', 'partida_id': 'part_001', 'jogadora_id': 'jog_001', 'tipo': EVENTO_ASSISTENCIA, 'minuto': 45, 'observacoes': 'Assistência para gol'},
            {'id': 'evt_003', 'partida_id': 'part_001', 'jogadora_id': 'jog_002', 'tipo': EVENTO_GOL, 'minuto': 67, 'observacoes': 'Gol de cabeça'},
            {'id': 'evt_004', 'partida_id': 'part_001', 'jogadora_id': 'jog_003', 'tipo': EVENTO_CARTAO_AMARELO, 'minuto': 78, 'observacoes': 'Falta tática'}
        ]
    
    # =============================================================================
    # SISTEMA DE AUTENTICAÇÃO
    # =============================================================================
    
    def criar_usuario(self, email, senha, nome, tipo):
        """Cria novo usuário no sistema"""
        # Estrutura de repetição: percorre lista de usuários para verificar email duplicado
        for usuario in self.usuarios:
            if usuario['email'] == email:
                return False
        
        # Dicionário: estrutura chave-valor para organizar dados do usuário
        novo_usuario = {
            'id': gerar_id(),
            'email': email,
            'senha_hash': hash_senha(senha),
            'nome': nome,
            'tipo': tipo,
            'ativo': True
        }
        
        # Lista: adiciona novo elemento ao final da lista de usuários
        self.usuarios.append(novo_usuario)
        return True
    
    def fazer_login(self, email, senha):
        """Realiza login do usuário"""
        senha_hash = hash_senha(senha)
        
        # Estrutura de repetição: busca usuário na lista comparando email e senha
        for usuario in self.usuarios:
            if (usuario['email'] == email and 
                usuario['senha_hash'] == senha_hash and 
                usuario['ativo']):
                self.usuario_logado = usuario
                return True
        return False
    
    def fazer_logout(self):
        """Realiza logout do usuário"""
        self.usuario_logado = None
    
    # =============================================================================
    # SISTEMA DE ESTATÍSTICAS
    # =============================================================================
    
    def calcular_estatisticas_jogadora(self, jogadora_id):
        """Calcula estatísticas de uma jogadora"""
        # Dicionário: estrutura para armazenar contadores de estatísticas
        stats = {
            'gols': 0,
            'assistencias': 0,
            'cartoes_amarelos': 0,
            'cartoes_vermelhos': 0,
            'finalizacoes': 0,
            'defesas': 0,
            'partidas_jogadas': 0
        }
        
        # Conjunto: evita contagem duplicada de partidas (set não permite duplicatas)
        partidas_jogadas = set()
        
        # Estrutura de repetição: percorre todos os eventos para encontrar os da jogadora
        for evento in self.eventos:
            if evento['jogadora_id'] == jogadora_id:
                tipo_evento = evento['tipo']
                partidas_jogadas.add(evento['partida_id'])
                
                # Estrutura de decisão: incrementa contador baseado no tipo de evento
                if tipo_evento == EVENTO_GOL:
                    stats['gols'] += 1
                elif tipo_evento == EVENTO_ASSISTENCIA:
                    stats['assistencias'] += 1
                elif tipo_evento == EVENTO_CARTAO_AMARELO:
                    stats['cartoes_amarelos'] += 1
                elif tipo_evento == EVENTO_CARTAO_VERMELHO:
                    stats['cartoes_vermelhos'] += 1
                elif tipo_evento == EVENTO_FINALIZACAO:
                    stats['finalizacoes'] += 1
                elif tipo_evento == EVENTO_DEFESA:
                    stats['defesas'] += 1
        
        stats['partidas_jogadas'] = len(partidas_jogadas)
        return stats
    
    def obter_ranking_gols(self, limite=10):
        """Obtém ranking de artilheiras"""
        ranking = []
        
        # Estrutura de repetição: processa cada jogadora ativa para calcular estatísticas
        for jogadora in self.jogadoras:
            if jogadora['ativa']:
                stats = self.calcular_estatisticas_jogadora(jogadora['id'])
                # Lista: adiciona dicionário com dados da jogadora ao ranking
                ranking.append({
                    'jogadora': jogadora,
                    'gols': stats['gols'],
                    'partidas': stats['partidas_jogadas']
                })
        
        # Processamento: ordena lista por gols em ordem decrescente
        ranking.sort(key=lambda x: x['gols'], reverse=True)
        return ranking[:limite]
    
    def obter_ranking_assistencias(self, limite=10):
        """Obtém ranking de assistências"""
        ranking = []
        
        # Estrutura de repetição: processa jogadoras ativas para ranking de assistências
        for jogadora in self.jogadoras:
            if jogadora['ativa']:
                stats = self.calcular_estatisticas_jogadora(jogadora['id'])
                ranking.append({
                    'jogadora': jogadora,
                    'assistencias': stats['assistencias'],
                    'partidas': stats['partidas_jogadas']
                })
        
        # Processamento: ordena por assistências em ordem decrescente
        ranking.sort(key=lambda x: x['assistencias'], reverse=True)
        return ranking[:limite]
    
    # =============================================================================
    # FUNÇÕES DE BUSCA
    # =============================================================================
    
    def buscar_jogadora_por_id(self, jogadora_id):
        """Busca jogadora por ID"""
        # Estrutura de repetição: percorre lista até encontrar jogadora com ID correspondente
        for jogadora in self.jogadoras:
            if jogadora['id'] == jogadora_id:
                return jogadora
        return None
    
    def buscar_clube_por_id(self, clube_id):
        """Busca clube por ID"""
        # Estrutura de repetição: busca clube específico na lista de clubes
        for clube in self.clubes:
            if clube['id'] == clube_id:
                return clube
        return None
    
    def buscar_jogadoras_por_nome(self, termo):
        """Busca jogadoras por nome"""
        jogadoras_encontradas = []
        termo_lower = termo.lower()
        
        # Estrutura de repetição: busca parcial no nome (case-insensitive)
        for jogadora in self.jogadoras:
            if termo_lower in jogadora['nome'].lower():
                jogadoras_encontradas.append(jogadora)
        
        return jogadoras_encontradas
    
    # =============================================================================
    # INTERFACE DO USUÁRIO
    # =============================================================================
    
    def exibir_menu_principal(self):
        """Exibe o menu principal da aplicação"""
        # Estrutura de repetição: loop principal que mantém aplicação rodando
        while True:
            exibir_cabecalho("PLATAFORMA DE ESTATÍSTICAS DO FUTEBOL FEMININO")
            
            # Estrutura de decisão: verifica se usuário está logado para mostrar menu apropriado
            if self.usuario_logado:
                print(f"👤 Usuário: {self.usuario_logado['nome']} ({self.usuario_logado['tipo']})")
                print("\n📋 MENU PRINCIPAL:")
                print("1. 📊 Ver Estatísticas de Jogadoras")
                print("2. 🏆 Ver Rankings")
                print("3. ⚽ Ver Clubes")
                print("4. 🏅 Ver Campeonatos")
                print("5. 🔍 Buscar Jogadora")
                print("6. 📈 Comparar Jogadoras")
                
                # Estrutura de decisão: mostra opção admin apenas para administradores
                if self.usuario_logado['tipo'] == TIPO_ADMIN:
                    print("7. ⚙️  Painel Administrativo")
                
                print("8. ℹ️  Informações do Sistema")
                print("0. 🚪 Sair")
                
                opcao = input("\nEscolha uma opção: ").strip()
                
                # Estrutura de decisão: direciona para função correspondente à opção escolhida
                if opcao == "1":
                    self.menu_estatisticas()
                elif opcao == "2":
                    self.menu_rankings()
                elif opcao == "3":
                    self.menu_clubes()
                elif opcao == "4":
                    self.menu_campeonatos()
                elif opcao == "5":
                    self.buscar_jogadora()
                elif opcao == "6":
                    self.comparar_jogadoras()
                elif opcao == "7" and self.usuario_logado['tipo'] == TIPO_ADMIN:
                    self.menu_admin()
                elif opcao == "8":
                    self.mostrar_informacoes_sistema()
                elif opcao == "0":
                    self.fazer_logout()
                    print("\n👋 Obrigado por usar a plataforma!")
                    break
                else:
                    print("❌ Opção inválida!")
            else:
                print("\n🔐 LOGIN:")
                print("1. Entrar")
                print("2. Cadastrar")
                print("0. Sair")
                
                opcao = input("\nEscolha uma opção: ").strip()
                
                # Estrutura de decisão: menu para usuários não logados
                if opcao == "1":
                    self.interface_login()
                elif opcao == "2":
                    self.interface_cadastro()
                elif opcao == "0":
                    print("\n👋 Obrigado por usar a plataforma!")
                    break
                else:
                    print("❌ Opção inválida!")
    
    def interface_login(self):
        """Interface de login"""
        print("\n🔐 LOGIN")
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
        
        if self.fazer_login(email, senha):
            print("✅ Login realizado com sucesso!")
        else:
            print("❌ Email ou senha incorretos!")
    
    def interface_cadastro(self):
        """Interface de cadastro"""
        print("\n📝 CADASTRO")
        nome = input("Nome completo: ").strip()
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
        
        if self.criar_usuario(email, senha, nome, TIPO_USUARIO):
            print("✅ Cadastro realizado com sucesso!")
        else:
            print("❌ Email já cadastrado!")
    
    def menu_estatisticas(self):
        """Menu de estatísticas"""
        print("\n📊 ESTATÍSTICAS DE JOGADORAS")
        print("1. Ver todas as jogadoras")
        print("2. Ver estatísticas detalhadas")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            self.listar_jogadoras()
        elif opcao == "2":
            self.ver_estatisticas_detalhadas()
    
    def listar_jogadoras(self):
        """Lista todas as jogadoras"""
        print("\n👥 JOGADORAS CADASTRADAS:")
        print("-" * 80)
        
        # Estrutura de repetição: percorre lista de jogadoras para exibir informações
        for jogadora in self.jogadoras:
            # Estrutura de decisão: só exibe jogadoras ativas
            if jogadora['ativa']:
                clube = self.buscar_clube_por_id(jogadora['clube_id'])
                clube_nome = clube['nome'] if clube else "Clube não encontrado"
                
                print(f"ID: {jogadora['id']}")
                print(f"Nome: {jogadora['nome']}")
                print(f"Posição: {jogadora['posicao']}")
                print(f"Clube: {clube_nome}")
                print(f"Número: {jogadora['numero_camisa']}")
                print(f"Idade: {jogadora['idade']} anos")
                print("-" * 80)
        
        # Pausa para usuário ver os resultados
        input("\n⏸️  Pressione Enter para continuar...")
    
    def ver_estatisticas_detalhadas(self):
        """Exibe estatísticas detalhadas"""
        # Mostra jogadoras disponíveis para facilitar teste
        print("\n👥 JOGADORAS DISPONÍVEIS:")
        for jogadora in self.jogadoras:
            if jogadora['ativa']:
                print(f"   ID: {jogadora['id']} - {jogadora['nome']}")
        
        jogadora_id = input("\nDigite o ID da jogadora: ").strip()
        
        jogadora = self.buscar_jogadora_por_id(jogadora_id)
        if not jogadora:
            print("❌ Jogadora não encontrada!")
            return
        
        clube = self.buscar_clube_por_id(jogadora['clube_id'])
        clube_nome = clube['nome'] if clube else "Clube não encontrado"
        
        stats = self.calcular_estatisticas_jogadora(jogadora_id)
        
        print(f"\n📊 ESTATÍSTICAS DE {jogadora['nome'].upper()}")
        print("=" * 60)
        print(f"Clube: {clube_nome}")
        print(f"Posição: {jogadora['posicao']}")
        print(f"Número: {jogadora['numero_camisa']}")
        print(f"Idade: {jogadora['idade']} anos")
        print(f"Nacionalidade: {jogadora['nacionalidade']}")
        print("-" * 60)
        print(f"⚽ Gols: {stats['gols']}")
        print(f"🎯 Assistências: {stats['assistencias']}")
        print(f"📊 Partidas jogadas: {stats['partidas_jogadas']}")
        print(f"🟨 Cartões amarelos: {stats['cartoes_amarelos']}")
        print(f"🟥 Cartões vermelhos: {stats['cartoes_vermelhos']}")
        print(f"🎯 Finalizações: {stats['finalizacoes']}")
        print(f"🛡️  Defesas: {stats['defesas']}")
        
        # Pausa para usuário ver os resultados
        input("\n⏸️  Pressione Enter para continuar...")
    
    def menu_rankings(self):
        """Menu de rankings"""
        print("\n🏆 RANKINGS")
        print("1. Ranking de Artilheiras")
        print("2. Ranking de Assistências")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            self.exibir_ranking_gols()
        elif opcao == "2":
            self.exibir_ranking_assistencias()
    
    def exibir_ranking_gols(self):
        """Exibe ranking de artilheiras"""
        ranking = self.obter_ranking_gols(10)
        
        print("\n⚽ RANKING DE ARTILHEIRAS")
        print("=" * 80)
        print(f"{'Pos':<4} {'Nome':<30} {'Clube':<25} {'Gols':<6} {'Partidas':<8}")
        print("-" * 80)
        
        # Estrutura de repetição: exibe cada posição do ranking com enumerate para numerar
        for i, item in enumerate(ranking, 1):
            jogadora = item['jogadora']
            clube = self.buscar_clube_por_id(jogadora['clube_id'])
            clube_nome = clube['nome'] if clube else "N/A"
            
            print(f"{i:<4} {jogadora['nome']:<30} {clube_nome:<25} {item['gols']:<6} {item['partidas']:<8}")
        
        # Pausa para usuário ver os resultados
        input("\n⏸️  Pressione Enter para continuar...")
    
    def exibir_ranking_assistencias(self):
        """Exibe ranking de assistências"""
        ranking = self.obter_ranking_assistencias(10)
        
        print("\n🎯 RANKING DE ASSISTÊNCIAS")
        print("=" * 80)
        print(f"{'Pos':<4} {'Nome':<30} {'Clube':<25} {'Assist':<6} {'Partidas':<8}")
        print("-" * 80)
        
        for i, item in enumerate(ranking, 1):
            jogadora = item['jogadora']
            clube = self.buscar_clube_por_id(jogadora['clube_id'])
            clube_nome = clube['nome'] if clube else "N/A"
            
            print(f"{i:<4} {jogadora['nome']:<30} {clube_nome:<25} {item['assistencias']:<6} {item['partidas']:<8}")
        
        # Pausa para usuário ver os resultados
        input("\n⏸️  Pressione Enter para continuar...")
    
    def menu_clubes(self):
        """Menu de clubes"""
        print("\n⚽ CLUBES CADASTRADOS")
        print("-" * 60)
        
        # Estrutura de repetição: percorre lista de clubes para exibir informações
        for clube in self.clubes:
            # Estrutura de decisão: só exibe clubes ativos
            if clube['ativo']:
                print(f"ID: {clube['id']}")
                print(f"Nome: {clube['nome']}")
                print(f"Cidade: {clube['cidade']}, {clube['estado']}")
                print(f"País: {clube['pais']}")
                print(f"Fundação: {clube['fundacao']}")
                print(f"Cores: {', '.join(clube['cores'])}")
                print("-" * 60)
        
        # Pausa para usuário ver os resultados
        input("\n⏸️  Pressione Enter para continuar...")
    
    def menu_campeonatos(self):
        """Menu de campeonatos"""
        print("\n🏅 CAMPEONATOS CADASTRADOS")
        print("-" * 60)
        
        for campeonato in self.campeonatos:
            if campeonato['ativo']:
                print(f"ID: {campeonato['id']}")
                print(f"Nome: {campeonato['nome']}")
                print(f"País: {campeonato['pais']}")
                print(f"Temporada: {campeonato['temporada']}")
                print("-" * 60)
        
        # Pausa para usuário ver os resultados
        input("\n⏸️  Pressione Enter para continuar...")
    
    def buscar_jogadora(self):
        """Busca jogadora por nome"""
        termo = input("Digite o nome da jogadora: ").strip()
        
        jogadoras_encontradas = self.buscar_jogadoras_por_nome(termo)
        
        if jogadoras_encontradas:
            print(f"\n🔍 JOGADORAS ENCONTRADAS ({len(jogadoras_encontradas)}):")
            print("-" * 60)
            
            for jogadora in jogadoras_encontradas:
                clube = self.buscar_clube_por_id(jogadora['clube_id'])
                clube_nome = clube['nome'] if clube else "N/A"
                
                print(f"ID: {jogadora['id']}")
                print(f"Nome: {jogadora['nome']}")
                print(f"Clube: {clube_nome}")
                print("-" * 60)
        else:
            print("❌ Nenhuma jogadora encontrada!")
        
        # Pausa para usuário ver os resultados
        input("\n⏸️  Pressione Enter para continuar...")
    
    def comparar_jogadoras(self):
        """Compara duas jogadoras"""
        print("\n📈 COMPARAÇÃO DE JOGADORAS")
        
        # Mostra jogadoras disponíveis para facilitar teste
        print("\n👥 JOGADORAS DISPONÍVEIS:")
        for jogadora in self.jogadoras:
            if jogadora['ativa']:
                print(f"   ID: {jogadora['id']} - {jogadora['nome']}")
        
        id1 = input("\nDigite o ID da primeira jogadora: ").strip()
        id2 = input("Digite o ID da segunda jogadora: ").strip()
        
        jogadora1 = self.buscar_jogadora_por_id(id1)
        jogadora2 = self.buscar_jogadora_por_id(id2)
        
        if not jogadora1 or not jogadora2:
            print("❌ Uma ou ambas as jogadoras não foram encontradas!")
            return
        
        stats1 = self.calcular_estatisticas_jogadora(id1)
        stats2 = self.calcular_estatisticas_jogadora(id2)
        
        print(f"\n📊 COMPARAÇÃO: {jogadora1['nome']} vs {jogadora2['nome']}")
        print("=" * 80)
        print(f"{'Estatística':<20} {'Jogadora 1':<15} {'Jogadora 2':<15}")
        print("-" * 80)
        print(f"{'Gols':<20} {stats1['gols']:<15} {stats2['gols']:<15}")
        print(f"{'Assistências':<20} {stats1['assistencias']:<15} {stats2['assistencias']:<15}")
        print(f"{'Partidas':<20} {stats1['partidas_jogadas']:<15} {stats2['partidas_jogadas']:<15}")
        print(f"{'Cartões Amarelos':<20} {stats1['cartoes_amarelos']:<15} {stats2['cartoes_amarelos']:<15}")
        print(f"{'Cartões Vermelhos':<20} {stats1['cartoes_vermelhos']:<15} {stats2['cartoes_vermelhos']:<15}")
        print(f"{'Finalizações':<20} {stats1['finalizacoes']:<15} {stats2['finalizacoes']:<15}")
        print(f"{'Defesas':<20} {stats1['defesas']:<15} {stats2['defesas']:<15}")
        
        # Pausa para usuário ver os resultados
        input("\n⏸️  Pressione Enter para continuar...")
    
    def mostrar_informacoes_sistema(self):
        """Mostra informações úteis do sistema"""
        print("\nℹ️  INFORMAÇÕES DO SISTEMA")
        print("=" * 60)
        print(f"📊 Dados cadastrados:")
        print(f"   • {len(self.usuarios)} usuários")
        print(f"   • {len(self.jogadoras)} jogadoras")
        print(f"   • {len(self.clubes)} clubes")
        print(f"   • {len(self.campeonatos)} campeonatos")
        print(f"   • {len(self.partidas)} partidas")
        print(f"   • {len(self.eventos)} eventos")
        
        print(f"\n👥 JOGADORAS DISPONÍVEIS:")
        for jogadora in self.jogadoras:
            if jogadora['ativa']:
                clube = self.buscar_clube_por_id(jogadora['clube_id'])
                clube_nome = clube['nome'] if clube else "N/A"
                print(f"   • ID: {jogadora['id']} - {jogadora['nome']} ({clube_nome})")
        
        print(f"\n⚽ CLUBES DISPONÍVEIS:")
        for clube in self.clubes:
            if clube['ativo']:
                print(f"   • ID: {clube['id']} - {clube['nome']}")
        
        print(f"\n🏅 CAMPEONATOS DISPONÍVEIS:")
        for campeonato in self.campeonatos:
            if campeonato['ativo']:
                print(f"   • ID: {campeonato['id']} - {campeonato['nome']}")
        
        print(f"\n💡 DICAS:")
        print("   • Use os IDs mostrados acima para testar as funcionalidades")
        print("   • Exemplo: Para ver estatísticas da Marta, use ID 'jog_001'")
        print("   • Para comparar jogadoras, use IDs diferentes (ex: jog_001 e jog_002)")
        
        # Pausa para usuário ver os resultados
        input("\n⏸️  Pressione Enter para continuar...")
    
    def menu_admin(self):
        """Menu administrativo"""
        print("\n⚙️  PAINEL ADMINISTRATIVO")
        print("1. Cadastrar Jogadora")
        print("2. Cadastrar Clube")
        print("3. Cadastrar Campeonato")
        print("4. Cadastrar Partida")
        print("5. Adicionar Evento à Partida")
        print("6. Gerenciar Usuários")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            self.cadastrar_jogadora()
        elif opcao == "2":
            self.cadastrar_clube()
        elif opcao == "3":
            self.cadastrar_campeonato()
        elif opcao == "4":
            self.cadastrar_partida()
        elif opcao == "5":
            self.adicionar_evento()
        elif opcao == "6":
            self.gerenciar_usuarios()
    
    def cadastrar_jogadora(self):
        """Cadastra nova jogadora"""
        print("\n👥 CADASTRAR JOGADORA")
        
        nome = input("Nome completo: ").strip()
        posicao = input("Posição: ").strip()
        clube_id = input("ID do clube: ").strip()
        numero = int(input("Número da camisa: "))
        idade = int(input("Idade: "))
        nacionalidade = input("Nacionalidade: ").strip()
        altura = float(input("Altura (m): "))
        peso = float(input("Peso (kg): "))
        
        nova_jogadora = {
            'id': gerar_id(),
            'nome': nome,
            'posicao': posicao,
            'clube_id': clube_id,
            'numero_camisa': numero,
            'idade': idade,
            'nacionalidade': nacionalidade,
            'altura': altura,
            'peso': peso,
            'ativa': True
        }
        
        self.jogadoras.append(nova_jogadora)
        print("✅ Jogadora cadastrada com sucesso!")
        
        # Pausa para usuário ver o resultado
        input("\n⏸️  Pressione Enter para continuar...")
    
    def cadastrar_clube(self):
        """Cadastra novo clube"""
        print("\n⚽ CADASTRAR CLUBE")
        
        nome = input("Nome do clube: ").strip()
        cidade = input("Cidade: ").strip()
        estado = input("Estado: ").strip()
        pais = input("País: ").strip()
        fundacao = int(input("Ano de fundação: "))
        cores_input = input("Cores (separadas por vírgula): ").strip()
        cores = [cor.strip() for cor in cores_input.split(',')]
        
        novo_clube = {
            'id': gerar_id(),
            'nome': nome,
            'cidade': cidade,
            'estado': estado,
            'pais': pais,
            'fundacao': fundacao,
            'cores': cores,
            'ativo': True
        }
        
        self.clubes.append(novo_clube)
        print("✅ Clube cadastrado com sucesso!")
        
        # Pausa para usuário ver o resultado
        input("\n⏸️  Pressione Enter para continuar...")
    
    def cadastrar_campeonato(self):
        """Cadastra novo campeonato"""
        print("\n🏅 CADASTRAR CAMPEONATO")
        
        nome = input("Nome do campeonato: ").strip()
        pais = input("País: ").strip()
        temporada = input("Temporada: ").strip()
        
        novo_campeonato = {
            'id': gerar_id(),
            'nome': nome,
            'pais': pais,
            'temporada': temporada,
            'ativo': True
        }
        
        self.campeonatos.append(novo_campeonato)
        print("✅ Campeonato cadastrado com sucesso!")
        
        # Pausa para usuário ver o resultado
        input("\n⏸️  Pressione Enter para continuar...")
    
    def cadastrar_partida(self):
        """Cadastra nova partida"""
        print("\n⚽ CADASTRAR PARTIDA")
        
        clube_casa = input("ID do clube da casa: ").strip()
        clube_fora = input("ID do clube visitante: ").strip()
        campeonato_id = input("ID do campeonato: ").strip()
        data = input("Data (YYYY-MM-DD): ").strip()
        
        nova_partida = {
            'id': gerar_id(),
            'clube_casa_id': clube_casa,
            'clube_fora_id': clube_fora,
            'campeonato_id': campeonato_id,
            'data': data,
            'placar_casa': 0,
            'placar_fora': 0,
            'finalizada': False
        }
        
        self.partidas.append(nova_partida)
        print("✅ Partida cadastrada com sucesso!")
        
        # Pausa para usuário ver o resultado
        input("\n⏸️  Pressione Enter para continuar...")
    
    def adicionar_evento(self):
        """Adiciona evento a uma partida"""
        print("\n📝 ADICIONAR EVENTO À PARTIDA")
        
        partida_id = input("ID da partida: ").strip()
        jogadora_id = input("ID da jogadora: ").strip()
        
        print("Tipos de evento:")
        print("1. Gol")
        print("2. Assistência")
        print("3. Cartão Amarelo")
        print("4. Cartão Vermelho")
        print("5. Finalização")
        print("6. Defesa")
        
        tipo_opcao = input("Escolha o tipo (1-6): ").strip()
        tipos = {
            '1': EVENTO_GOL,
            '2': EVENTO_ASSISTENCIA,
            '3': EVENTO_CARTAO_AMARELO,
            '4': EVENTO_CARTAO_VERMELHO,
            '5': EVENTO_FINALIZACAO,
            '6': EVENTO_DEFESA
        }
        
        tipo_evento = tipos.get(tipo_opcao)
        if not tipo_evento:
            print("❌ Tipo inválido!")
            return
        
        minuto = int(input("Minuto do evento: "))
        observacoes = input("Observações (opcional): ").strip()
        
        novo_evento = {
            'id': gerar_id(),
            'partida_id': partida_id,
            'jogadora_id': jogadora_id,
            'tipo': tipo_evento,
            'minuto': minuto,
            'observacoes': observacoes
        }
        
        self.eventos.append(novo_evento)
        print("✅ Evento adicionado com sucesso!")
        
        # Pausa para usuário ver o resultado
        input("\n⏸️  Pressione Enter para continuar...")
    
    def gerenciar_usuarios(self):
        """Gerencia usuários do sistema"""
        print("\n👥 GERENCIAR USUÁRIOS")
        print("-" * 60)
        
        for usuario in self.usuarios:
            status = "✅ Ativo" if usuario['ativo'] else "❌ Inativo"
            print(f"ID: {usuario['id']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Email: {usuario['email']}")
            print(f"Tipo: {usuario['tipo']}")
            print(f"Status: {status}")
            print("-" * 60)
        
        # Pausa para usuário ver os resultados
        input("\n⏸️  Pressione Enter para continuar...")

# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

def main():
    """Função principal do programa"""
    print("🚀 Iniciando Plataforma de Estatísticas do Futebol Feminino...")
    print("📚 Trabalho Acadêmico - Demonstração de Conceitos Python")
    
    try:
        sistema = SistemaFutebolFeminino()
        sistema.exibir_menu_principal()
    except KeyboardInterrupt:
        print("\n\n👋 Obrigado por usar a plataforma!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()