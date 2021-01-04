class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.urlValida(url):
            self.url = url.lower()
        else:
            raise LookupError("URL inválida!!!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem, moedaDestino = self.extrairArgumentos()
        representacaoString = f"Valor: {self.extrairValor()} \nMoeda Origem: {moedaOrigem} \nMoeda Destino: {moedaDestino} \n"
        return representacaoString

    def __eq__(self, outraValor):
        return self.url == outraValor.url

    @staticmethod
    def urlValida(url):
        if url and url.startswith("https://www.bytebank.com.br") or url.startswith("https://www.youtube.com"):
            return True
        else:
            return False

    # Extraindo argumentos da string passada
    def extrairArgumentos(self):

        buscaMoedaOrigem = "moedaorigem".lower()
        buscaMOedaDestino = "moedadestino".lower()

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem: indiceFinalMoedaOrigem]

        if moedaOrigem == buscaMOedaDestino:
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem: indiceFinalMoedaOrigem]

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMOedaDestino)
        indiceFinalMoedaDestino = self.url.find("&", indiceFinalMoedaOrigem + 1)

        moedaDestino = self.url[indiceInicialMoedaDestino: indiceFinalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, valor):
        return self.url.find(valor) + len(valor)+1

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extrairValor(self):
        buscaValor = "valor"
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor