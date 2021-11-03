sensacao = ["Hiperestesia", "Hipoestesia", "Anestesia", "Analgesia"]
percepcao = ["Agnosias",["agnosia Visual", "Agnosia Tátil","Agnosia Primária ou Perseptiva", "Agnosia Semântica", "Agnosia Auditiva", ], "Ilusão"]
representacao = ["Alucinação",["Alucinação Auditiva", "Alucinação Visual", "Alucinação Autoscópia", "Alucinação Extracampinas",
 "Alucinação Alfativas e Gustativa", "Alucinação Tátil", "Aluinação Cenestésicas",
  "Alucinação do Sentido de Equilíbrio", "Alucinação Psíquica"],"Alucinose","Alucinose Penduncular","Pseudo-Alucinação","Visões Fantástias"]
conceitos = ["Esquizofrenia", "Deficiência Mental", "Estados Demenciais", "Psicoses Sintomáticas"]
juizo = ["Delirios", ["Percepção Delirante", "Ocorrência Delirante", "Reação Deliróide"] ,"Delirio de perseguição",
 "Delirio de Relação", "Delirio de Influência", "Delirio de Ciúme", "Delirio de Grandeza",["Delirio Ambicioso", "Delirio de Invenção", "Delirio de Reforma", "Delirio erótico"] ]
raciocinio = ["Inibição do pensamento", "Fuga das ideias", "Perseveração", "Prolixidade", "Incoerência", "Interceptação do Pensamento", "Complusãp a Pensar",
"pensamento Obsessivo", "Psicose Maníaco - Depressiva", "Epilepsia", "Esquizofrenia", "Deficiência Mental", "Psicoses Orgânicas", "Psicodes Sintomáticas"]
memoria = ["Hipermneisa", "Amnesia", ["Amnesia Anterógrada", "Amnesia Retrógrada", "Amnesia retroanterógrada ou Total", "Amnesia transitória"]]

print("Categoria de Patoligias:\n 1- Sensação,\n 2-Percepção,\n 3- Representação,\n 4- Conceitos,\n 5-Raciocínio, \n 6- Memória. ")

escolha = int(input("Escolha uma categoria: "))

if escolha == 1:
  for tag in sensacao:
    print(f"Psicopatologia da Sensação - {tag}")

elif escolha == 2:
  for tag in percepcao:
   print(f"Psicopatologia da Percepção - {tag}")

elif escolha == 3:
  for tag in representacao:
   print(f"Psicopatologia de Representação - {tag}")

elif escolha == 4:
  for tag in conceitos:
   print(f"Psicopatologia de Conceito - {tag}")

elif escolha == 5:
  for tag in juizo:
    print(f"Psicopatologia de Juízo - {tag}")

elif escolha == 6:
  for tag in memoria:
    print(f"Psicopatologia da Memória - {tag}")
 

