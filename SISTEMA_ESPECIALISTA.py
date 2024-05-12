def calcular_ocorrencias(dados, C1, grausC1, C2, grausC2, C3, grausC3):
    
    #Função para calcular as ocorrências com base nas características e graus informados.
    
    for i in dados:
        i["OCORRENCIAS"] = 0
        i["PERCENTUAL"] = 0
    
    for pos, i in enumerate(dados):
        caracteristica = i["CARACTERISTICAS"]
        if C1 in caracteristica: 
            i["OCORRENCIAS"] += caracteristica[C1] * (float(grausC1) / 10)
        if C2 in caracteristica: 
            i["OCORRENCIAS"] += caracteristica[C2] * (float(grausC2) / 10)
        if C3 in caracteristica: 
            i["OCORRENCIAS"] += caracteristica[C3] * (float(grausC3) / 10)

    for pos, i in enumerate(dados):
        caracteristica = i["CARACTERISTICAS"]
        total = sum(caracteristica[k] for k in caracteristica)
        dados[pos]["PERCENTUAL"] = float(i["OCORRENCIAS"]) / total * 100

def validar_numero(n):
    
    #Função para validar se a entrada é um número inteiro no intervalo de 0 a 10.
    
    try:
        numero = int(n)
        if 0 <= numero <= 10:
            return True
        else:
            return False
    except ValueError:
        return False


def main():
    dados = [
        {"REFEICAO":"Smoothie energetico com WHEY, leite, aveia e manteiga de amendoim",
         "CARACTERISTICAS": {"CALORICO":7,"PROTEICO":9,"CARBOIDRATADA":7,"GORDUROSO":6,"VITAMINICO":2},
         "OCORRENCIAS": 0,"PERCENTUAL":0,"DESCRICAO":"Fonte alta de proteinas e consideravelmente alta em calorias e carboidratos."},
        {"REFEICAO":"Peito de frango grelhado com quinoa e legumes assados",
         "CARACTERISTICAS": {"CALORICO":4,"PROTEICO":8,"CARBOIDRATADA":3,"GORDUROSO":4,"VITAMINICO":6},
         "OCORRENCIAS": 0,"PERCENTUAL":0,"DESCRICAO":"Fonte alta em proteinas e consideravelmente vitaminico."},
        {"REFEICAO":"Macarrão integral com molho de tomate e almondegas",
         "CARACTERISTICAS": {"CALORICO":6,"PROTEICO":4,"CARBOIDRATADA":9,"GORDUROSO":6,"VITAMINICO":3},
         "OCORRENCIAS": 0,"PERCENTUAL":0,"DESCRICAO":"Fonte alta em carboidratos e consideralvemente calorico e gorduroso."},
        {"REFEICAO":"Batata-doce assada com salmão grelhado",
         "CARACTERISTICAS": {"CALORICO":8,"PROTEICO":5,"CARBOIDRATADA":7,"GORDUROSO":5,"VITAMINICO":3},
         "OCORRENCIAS": 0,"PERCENTUAL":0,"DESCRICAO":"Fonte alta em calorias, consideravelmente alta em carboidratos e razoavelmente proteico e gorduroso."},
        {"REFEICAO":"Wrap de Frango com Abacate, Cenoura e Alface",
         "CARACTERISTICAS": {"CALORICO":5,"PROTEICO":6,"CARBOIDRATADA":5,"GORDUROSO":7,"VITAMINICO":8},
         "OCORRENCIAS": 0,"PERCENTUAL":0,"DESCRICAO":"Fonte alta em vitaminas consideravelmente proteico e alto em gordura boa."},
        {"REFEICAO":"Omelete de queijo com tomate e espinafre",
         "CARACTERISTICAS": {"CALORICO":5,"PROTEICO":7,"CARBOIDRATADA":3,"GORDUROSO":4,"VITAMINICO":5},
         "OCORRENCIAS": 0,"PERCENTUAL":0,"DESCRICAO":"Fonte moderada em calorias, proteínas e vitaminas."},
        {"REFEICAO":"Sopa de legumes com frango desfiado",
         "CARACTERISTICAS": {"CALORICO":3,"PROTEICO":6,"CARBOIDRATADA":4,"GORDUROSO":2,"VITAMINICO":7},
         "OCORRENCIAS": 0,"PERCENTUAL":0,"DESCRICAO":"Fonte moderada em calorias, rica em proteínas e vitaminas."},
        {"REFEICAO":"Salada de quinoa com abacate e tomate",
         "CARACTERISTICAS": {"CALORICO":4,"PROTEICO":5,"CARBOIDRATADA":6,"GORDUROSO":3,"VITAMINICO":6},
         "OCORRENCIAS": 0,"PERCENTUAL":0,"DESCRICAO":"Fonte moderada em calorias, carboidratos e gorduras saudáveis."},
        {"REFEICAO":"Hambúrguer vegetariano com batata doce assada",
         "CARACTERISTICAS": {"CALORICO":6,"PROTEICO":5,"CARBOIDRATADA":7,"GORDUROSO":4,"VITAMINICO":5},
         "OCORRENCIAS": 0,"PERCENTUAL":0,"DESCRICAO":"Fonte moderada em calorias, rica em carboidratos e proteínas."},
        {"REFEICAO":"Tigela de açaí com granola e frutas",
         "CARACTERISTICAS": {"CALORICO":8,"PROTEICO":3,"CARBOIDRATADA":9,"GORDUROSO":5,"VITAMINICO":8},
         "OCORRENCIAS": 0,"PERCENTUAL":0,"DESCRICAO":"Fonte alta em calorias e carboidratos, com antioxidantes e vitaminas."}
    ]

    print("Sistema Especialista sobre recomendacoes de pratos para suas refeicoes, baseando-se no grau das caracteristicas destacadas.\n")
    print("*************************************\n")
    print("Características dos pratos:\n  CALORICO\n  PROTEICO\n  CARBOIDRATADA\n  GORDUROSO\n  VITAMINICO\n")
    print("*************************************\n")

    C1 = input("INDIQUE A PRIMEIRA CARACTERISTICA: ").upper()
    while True:
        grausC1 = input("   INDIQUE O GRAU DA CARACTERISTICA (0 a 10): ")
        if validar_numero(grausC1):
            break
        else:
            print("Por favor, digite apenas números entre 0 e 10 para o grau da característica.")
            
    C2 = input("INDIQUE A SEGUNDA CARACTERISTICA: ").upper()
    while True:
        grausC2 = input("   INDIQUE O GRAU DA CARACTERISTICA (0 a 10): ")
        if validar_numero(grausC2):
            break
        else:
            print("Por favor, digite apenas números entre 0 e 10 para o grau da característica.")
            
    C3 = input("INDIQUE A TERCEIRA CARACTERISTICA: ").upper()
    while True:
        grausC3 = input("   INDIQUE O GRAU DA CARACTERISTICA (0 a 10): ")
        if validar_numero(grausC3):
            break
        else:
            print("Por favor, digite apenas números entre 0 e 10 para o grau da característica.")

    calcular_ocorrencias(dados, C1, grausC1, C2, grausC2, C3, grausC3)

    print("\n*************************************")
    print("RESULTADOS PARA AS CARACTERISTICAS: ")
    print("    ",C1," EM GRAU ", grausC1)
    print("    ",C2," EM GRAU ", grausC2)
    print("    ",C3," EM GRAU ", grausC3)
    print("\n*************************************")

    aux = [[v["PERCENTUAL"], v["REFEICAO"]] for v in dados]
    ordenado = sorted(aux, reverse=True)
    print("\nPROBABILIDADE DE MATCHING ORDENADA CONSIDERANDO O TOTAL DE CARACTERISTICAS:")
    for i in ordenado:
        percentual = format(i[0], "5.2f")
        print("A REFEICAO:", i[1], "TEM", percentual, "% DE PROBABILIDADE DE ATENDER AS CARACTERISTICAS ESPECIFICADAS")

    # RECOMENDAÇÃO DOS PRATOS
    print("\nMELHORES OPCOES DE PRATOS PARA ESTA REFEICAO:")
    for prato in ordenado[:2]:
        nome_prato = prato[1]  # Obtém o nome do prato
        j = [i["REFEICAO"] for i in dados].index(nome_prato)  # Encontra o índice do prato no dicionário de dados
        descricao_prato = dados[j]["DESCRICAO"]  # Obtém a descrição do prato
        print(nome_prato)
        print("    ",descricao_prato)

if __name__ == "__main__":
    main()
