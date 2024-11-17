# imob_local
Acessando o servidor via PuTTY: (chaves incluidas na pasta config)

https://www.youtube.com/watch?v=cTbYAkyxxqE

Abra o PuTTY

Em Host Name (or Ip address) coloque o endereço do server:

Carregue a imob.ppk em Connection/SSh/Auth/Credentials

Clique Browse em Public-key authentication e escolha a chave imob.ppk

Depois clique: Open

O terminal do PuTTY irá abrir e pedir uma senha:

"You are IN"

Como Rodar

Instale as dependências:
python.exe -m pip install --upgrade pip

pip install -r requirements.txt

Prepare seu ambiente virtual

python -m venv venv

.\venv\Scripts\activate

Inicie o aplicativo (ele fecha por inatividade):
python run.py

Para manter a aplicação rodando utilize o comando:
nohup python run.py &

Para rodar localmente no Visual Studio Code é necessário o ngrok.

OBS: coloque os dados de autenticação no arquivo .env
