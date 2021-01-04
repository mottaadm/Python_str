from extratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://www.youtube.com/watch?v=fn3KWM1kuAw"
url2 = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=700"
meu_nome = "Marcos"

substring = meu_nome[5]
print(substring)
substring = meu_nome[0:3]
print(substring)

index = url.find("=")
print(index)
substring = url[index + 1:]
print(substring)

lista_argumentos = url.split("/")
print((lista_argumentos))
lista_argumentos = url.split("=")
print((lista_argumentos))

argumentos = ExtratorArgumentosUrl(url)
print(argumentos)
print(ExtratorArgumentosUrl.urlValida(url))

argumentos_2 = ExtratorArgumentosUrl(url2)
print(argumentos_2)
print(ExtratorArgumentosUrl.urlValida(url2))

moedaOrigem, moedaDestino = argumentos_2.extrairArgumentos()
valor = argumentos_2.extrairValor()
print(f"{moedaOrigem}, {moedaDestino}, {valor}")


print(f"Sua URL tem {argumentos_2.__len__()} caracteres")