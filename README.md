# BluePen Bot

## <b>Um bot de música para o discord que aceita Youtube e Soundcloud.</b>

### Todos os comandos:

![alt text for screen readers](/_git/_help.png).

<br></br>

## Rodando o Código

1. Clone o repositorio atual (git clone git@github.com:fer-moreira/BluePenBot.git) ou baixe o zip e extraia em qualquer lugar
2. Abra um terminal na raiz do bot, onde se encontra o main.py
3. Instale os pacotes do ffmpeg, [Instalar no windows](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/), para instalar no Linux (WSL) use os comandos abaixo
 
```bash
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install ffmpeg
```

4. Crie uma nova virtualenv com o python, pra isso siga os comandos abaixo
``` bash
python -m pip install virtualenv
python -m virtualenv venv
```

5. Ative a Virtualenv 
```bash
source venv/bin/activate
```

6. Instale os pacotes do python
```bash
python -m pip install -r requirements.txt
```

7. Agora você está pronto para configurar o bot para o seu discord, siga os proximos passos 🍷🗿


<br></br>

## Como configurar para o seu Bot

1. Crie uma aplicação no [Discord Development Portal](https://discord.com/developers/applications), gera um novo token de Bot para essa APP no botão (Reset Token)
2.  Copie o token e coloque em uma variavel de ambiente chamada ```DISCORD_TOKEN```, no wsl é export DISCORD_TOKEN="token" no Windows pesquise por variavel de ambiente, abre as configurações e adicione lá como DISCORD_TOKEN
3. Agora está tudo pronto, só rodar o código com:
```bash
python main.py
``` 
<br></br>

# TODO
- melhorar readme
- refatorar código do player