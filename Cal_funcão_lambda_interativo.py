from functools import reduce

def calcular_expressao(operacoes):
    """
    Calcula o resultado de uma lista de operações sequenciais.
    operacoes: lista de tuplas [(operador, valor), ...]
    """
    def aplicar_operacao(acumulador, operacao_item):
        operador, valor = operacao_item
        if operador == "+":
            return acumulador + valor
        elif operador == "-":
            return acumulador - valor
        elif operador == "*":
            return acumulador * valor
        elif operador == "/":
            if valor == 0:
                raise ValueError("Divisão por zero!")
            return acumulador / valor
        else:
            raise ValueError(f"Operador desconhecido: {operador}")

    if not operacoes:
        return 0

    # Se a primeira operação for '=', define o valor inicial.
    # Caso contrário, começa do zero.
    if operacoes[0][0] == "=":
        valor_inicial = operacoes[0][1]
        return reduce(aplicar_operacao, operacoes[1:], valor_inicial)
    else:
        return reduce(aplicar_operacao, operacoes, 0)

def obter_input_usuario():
    """
    Interface interativa para coletar operações do utilizador.
    """
    print("\n--- Calculadora de Expressões Interativa ---")
    print("Instruções:")
    print("1. Insira o valor inicial usando '=' (ex: = 10)")
    print("2. Insira as operações seguintes (ex: + 5, * 2, - 3)")
    print("3. Digite 'fim' para calcular o resultado.")
    print("4. Digite 'sair' para fechar o programa.")

    operacoes = []
    
    while True:
        entrada = input("\nOperação (ex: + 5) ou comando: ").strip().lower()
        
        if entrada == 'sair':
            return None
        if entrada == 'fim':
            break
        
        try:
            partes = entrada.split()
            if len(partes) != 2:
                print("Erro: Formato inválido. Use 'operador valor' (ex: + 5).")
                continue
            
            operador = partes[0]
            valor = float(partes[1])
            
            if operador not in ["=", "+", "-", "*", "/"]:
                print(f"Erro: Operador '{operador}' não reconhecido.")
                continue
                
            operacoes.append((operador, valor))
            print(f"Lista atual: {operacoes}")
            
        except ValueError:
            print("Erro: O valor inserido deve ser um número.")

    return operacoes

def main():
    while True:
        lista_operacoes = obter_input_usuario()
        
        if lista_operacoes is None:
            print("Encerrando a calculadora. Até logo!")
            break
            
        if not lista_operacoes:
            print("Nenhuma operação inserida.")
            continue
            
        try:
            resultado = calcular_expressao(lista_operacoes)
            print(f"\n>>> RESULTADO FINAL: {resultado}")
        except ValueError as e:
            print(f"\n>>> ERRO NO CÁLCULO: {e}")
        
        continuar = input("\nDeseja realizar outro cálculo? (s/n): ").strip().lower()
        if continuar != 's':
            print("Encerrando a calculadora. Até logo!")
            break

if __name__ == "__main__":
    main()
