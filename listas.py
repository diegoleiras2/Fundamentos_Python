#lista são arrays/vetores
listaUnidimensional = ["Alê", 2, 0.1, True]
print(listaUnidimensional)

#índices são contados a partir do 0
print(listaUnidimensional[0])

for valor in listaUnidimensional:
    #f representa a função format - que formata uma string
    #print(f"{}")
    print(f"Valor da lista: {valor}")
    """print("Valor da lista: {}".format(valor))"""

    #str(variavel) converte para string
    #int(), float(), bool()
    """print("Valor da lista: " + str(valor)) #concatenação"""
    
cidades = ["Rio de janeiro", "São Paulo", "Maricá", "Belo Horizonte"]
for cidade in cidades:
    print(f"Cidade: {cidade}")
