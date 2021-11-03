patologias = {
                "sensacao": ["Hiperestesia", "Hipoestesia", "Anestesia", "Analgesia"],
                
                "percepcao": {
                            "Agnosias": ["agnosia Visual", "Agnosia Tátil","Agnosia Primária ou Perseptiva", "Agnosia Semântica", "Agnosia Auditiva", ],
                            "Ilusão": None
                          },
                
                "representacao": {
                                "Alucinação": ["Alucinação Auditiva", "Alucinação Visual", "Alucinação Autoscópia", "Alucinação Extracampinas",
                                "Alucinação Alfativas e Gustativa", "Alucinação Tátil", "Aluinação Cenestésicas",
                                "Alucinação do Sentido de Equilíbrio", "Alucinação Psíquica"],
                                "Alucinose": ["Alucinose Penduncular","Pseudo-Alucinação","Visões Fantástias"] 
                               },

                "conceitos": ["Esquizofrenia", "Deficiência Mental", "Estados Demenciais", "Psicoses Sintomáticas"],

                "juizo": {
                          "Delirios": ["Percepção Delirante", "Ocorrência Delirante", "Reação Deliróide"] ,
                          "Delirio de perseguição": None,
                          "Delirio de Relação": None,
                          "Delirio de Influência":None,
                          "Delirio de Ciúme": None,
                          "Delirio de Grandeza": ["Delirio Ambicioso", "Delirio de Invenção", "Delirio de Reforma", "Delirio erótico"] 
                      },   

              "raciocinio": ["Inibição do pensamento", "Fuga das ideias", "Perseveração", "Prolixidade", "Incoerência", "Interceptação do Pensamento", "Complusãp a Pensar",
              "pensamento Obsessivo", "Psicose Maníaco - Depressiva", "Epilepsia", "Esquizofrenia", "Deficiência Mental", "Psicoses Orgânicas", "Psicodes Sintomáticas"],

              "memoria": {
                          "Hipermneisa": None, 
                          "Amnesia": ["Amnesia Anterógrada", "Amnesia Retrógrada", "Amnesia retroanterógrada ou Total", "Amnesia transitória"]
                        }
            }


#print(percepcao)
#print(sensacao)
#print(representacao)
#print(conceitos)
#print(juizo)
#print(raciocinio)

#print(percepcao["Agnosias"][0]) #dicionário
#print(percepcao[1][0])
#sensacao = patologias["sensacao"]
#print(f"Sensação: {sensacao}")

for tag in patologias:
#  print(tag)
  for subtag in patologias[tag]:
    print(type(subtag))
    print(subtag)
    if isinstance(subtag, list):
    if isinstance(subtag.value, list):
        for pat in patologias[tag][subtag]:
        print(f"{tag}- {subtag}: {pat}")
    print(f"{tag}: {subtag}")