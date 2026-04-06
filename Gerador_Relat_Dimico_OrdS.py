dados_vendas = [ 
    {"produto": "Laptop", "categoria": "Eletrônicos", "quantidade": 10, "preco_unitario": 1200}, 
    {"produto": "Teclado", "categoria": "Acessórios", "quantidade": 50, "preco_unitario": 50}, 
    {"produto": "Mouse", "categoria": "Acessórios", "quantidade": 75, "preco_unitario": 25}, 
    {"produto": "Monitor", "categoria": "Eletrônicos", "quantidade": 15, "preco_unitario": 300}, 
    {"produto": "Webcam", "categoria": "Acessórios", "quantidade": 30, "preco_unitario": 70}, 
] 

def gerar_relatorio(vendas, filtro_fn=None, transformacao_fn=None): 
    # Aplicar filtro, se houver 
    vendas_filtradas = list(filter(filtro_fn, vendas)) if filtro_fn else vendas 
    # Aplicar transformação, se houver 
    vendas_transformadas = list(map(transformacao_fn, vendas_filtradas)) if transformacao_fn else vendas_filtradas 
    return vendas_transformadas 

def imprimir_relatorio(titulo, relatorio): 
    print(f"\n--- {titulo} ---") 
    for item in relatorio: 
        print(item)

# Filtro para eletrônicos 
filtro_eletronicos = lambda item: item["categoria"] == "Eletrônicos" 

# Transformação para calcular o total de vendas por item 
transformacao_total_vendas = lambda item: { 
    "produto": item["produto"], 
    "total_venda": item["quantidade"] * item["preco_unitario"] 
} 

# Relatório de todos os itens 
relatorio_completo = gerar_relatorio(dados_vendas) 
imprimir_relatorio("Relatório Completo", relatorio_completo)

# Relatório de eletrônicos com total de vendas 
relatorio_eletronicos = gerar_relatorio(dados_vendas, filtro_fn=filtro_eletronicos, transformacao_fn=transformacao_total_vendas) 
imprimir_relatorio("Relatório de Eletrônicos (Total de Vendas)", relatorio_eletronicos)

# Relatório de acessórios com apenas nome e quantidade 
filtro_acessorios = lambda item: item["categoria"] == "Acessórios" 
transformacao_nome_quantidade = lambda item: {"produto": item["produto"], "quantidade": item["quantidade"]} 
relatorio_acessorios = gerar_relatorio(dados_vendas, filtro_fn=filtro_acessorios, transformacao_fn=transformacao_nome_quantidade) 
imprimir_relatorio("Relatório de Acessórios (Nome e Quantidade)", relatorio_acessorios)