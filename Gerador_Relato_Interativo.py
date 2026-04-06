def obter_dados_vendas():
    dados_vendas = []
    while True:
        produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
        if produto.lower() == 'sair':
            break
        categoria = input("Digite a categoria do produto: ")
        quantidade = int(input("Digite a quantidade vendida: "))
        preco_unitario = float(input("Digite o preço unitário: "))
        
        dados_vendas.append({
            "produto": produto,
            "categoria": categoria,
            "quantidade": quantidade,
            "preco_unitario": preco_unitario
        })
    return dados_vendas

def gerar_relatorio(vendas, filtro_fn=None, transformacao_fn=None): 
    vendas_filtradas = list(filter(filtro_fn, vendas)) if filtro_fn else vendas 
    vendas_transformadas = list(map(transformacao_fn, vendas_filtradas)) if transformacao_fn else vendas_filtradas 
    return vendas_transformadas 

def imprimir_relatorio(titulo, relatorio): 
    print(f"\n--- {titulo} ---") 
    for item in relatorio: 
        print(item)

def main():
    dados_vendas = obter_dados_vendas()

    while True:
        print("\nEscolha o tipo de relatório:")
        print("1. Relatório Completo")
        print("2. Relatório de Eletrônicos (Total de Vendas)")
        print("3. Relatório de Acessórios (Nome e Quantidade)")
        print("4. Sair")
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '1':
            relatorio_completo = gerar_relatorio(dados_vendas) 
            imprimir_relatorio("Relatório Completo", relatorio_completo)
        elif escolha == '2':
            filtro_eletronicos = lambda item: item["categoria"] == "Eletrônicos" 
            transformacao_total_vendas = lambda item: { 
                "produto": item["produto"], 
                "total_venda": item["quantidade"] * item["preco_unitario"] 
            } 
            relatorio_eletronicos = gerar_relatorio(dados_vendas, filtro_fn=filtro_eletronicos, transformacao_fn=transformacao_total_vendas) 
            imprimir_relatorio("Relatório de Eletrônicos (Total de Vendas)", relatorio_eletronicos)
        elif escolha == '3':
            filtro_acessorios = lambda item: item["categoria"] == "Acessórios" 
            transformacao_nome_quantidade = lambda item: {"produto": item["produto"], "quantidade": item["quantidade"]} 
            relatorio_acessorios = gerar_relatorio(dados_vendas, filtro_fn=filtro_acessorios, transformacao_fn=transformacao_nome_quantidade) 
            imprimir_relatorio("Relatório de Acessórios (Nome e Quantidade)", relatorio_acessorios)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()