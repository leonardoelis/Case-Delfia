# Case Delfia

<p>Repositório com o case de Python da Delfia. Trata-se da criação de dois scripts Python, um para manipular arquivos CSV e outro para consumir uma API Rest. Abaixo encontram-se as instruções para rodar o projeto.</p>

### Como rodar o projeto? (Windows)
<ul>
    <li>Clone o repositório</li>
    <li>Crie um virtualenv</li>
    <li>Ative o virtualenv</li>
</ul>

```
git clone https://github.com/leonardoelis/Case-Delfia.git
python -m venv venv
cd venv/Scripts
activate
```
Dentro da pasta Case-Delfia:
<ul>
    <li>Instale as dependências</li>
</ul>

```
pip install -r requirements.txt
```

Para rodar o primeiro script, abra um terminal dentro da pasta etapa1 e execute o seguinte comando:
```
python etapa1.py
```

Para rodar o segundo script, é necessário gerar uma chave de API do OpenWeatherMap. Para isso, crie uma conta em https://openweathermap.org/ e depois, com a conta criada, vá até a aba "API keys" e gere uma chave de API (a chave de API pode demorar alguns minutos para ficar disponível para uso).
Depois de gerar a chave, crie um arquivo .env dentro da pasta etapa2. O arquivo .env deve ter a seguinte estrutura:
```
API_KEY=SUA_CHAVE_DE_API
```
Substitua SUA_CHAVE_DE_API pela chave gerada no site do OpenWeatherMap. Após isso, você já pode rodar o seguinte comando dentro da pasta etapa2:
```
python etapa2.py
```