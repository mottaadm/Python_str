import re

# Expressões Regulares: métodos re.search, re.findall e group()
padrao = "[0-9]{4,5}-?[0-9]{4}"
# Vamos testar esse padrão.
texto =  "Meu número para contato é 2633-5723. Fale comigo pelo número 97857-6776, esse é meu celular."
retorno = re.search(padrao, texto)
retorno_2 = re.findall(padrao, texto)
print(retorno.group())
print(retorno_2)