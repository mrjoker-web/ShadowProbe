<p align="center">
  <h1>ShadowProbe</h1>
  <p>⚡ Fast HTTP/HTTPS Probe Tool for Reconnaissance</p>
</p>

---

---

# 💣 Extra

```markdown id="q2k3df"
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-active-success)
![Version](https://img.shields.io/badge/version-1.0-orange)
![License](https://img.shields.io/badge/license-MIT-green)


## 🔍 Sobre o Projeto

**ShadowProbe** é uma ferramenta rápida e eficiente para identificar **hosts ativos** durante a fase de *reconnaissance* em pentesting.

Criada por **Mr Joker**, esta tool permite testar múltiplos alvos simultaneamente, detectando serviços HTTP/HTTPS, status codes e títulos das páginas.

---

## ⚡ Funcionalidades

- 🌐 Suporte a HTTP e HTTPS  
- ⚡ Multi-threading (scan rápido)  
- 📊 Barra de progresso em tempo real  
- 🧠 Extração de título da página  
- 📁 Exportação de resultados (.txt e .json)  
- 🎨 Interface CLI com cores  

---

## 🎯 Objetivo

Ajudar na identificação de **hosts ativos** após a descoberta de subdomínios.

Ideal para:
- Pentesters  
- Estudantes de cybersecurity  
- Entusiastas de ethical hacking  

---

## 🔗 Integração (Pipeline)

```text
ShadowSub → encontra subdomínios
↓
ShadowProbe → verifica quais estão ativos
↓
ShadowScan → analisa portas e serviços

⚙️ Instalação

git clone https://github.com/mrjoker-web/ShadowProbe.git
cd ShadowProbe
pip install requests

▶️ Como usar

python shadowprobe.py -l subdomains.txt

Com threads personalizadas:

python shadowprobe.py -l subdomains.txt --threads 100

📄 Input
Ficheiro de entrada (subdomains.txt):

admin.example.com
api.example.com
dev.example.com

📸 Exemplo de Output

[200] https://admin.example.com | Admin Panel
[403] http://dev.example.com | Forbidden
[200] https://api.example.com | API Gateway

[##############################] 100.0%

[+] Output guardado em live_hosts.txt e live_hosts.json

📁 Output
live_hosts.txt → lista simples
live_hosts.json → formato estruturado (ideal para automação)

⚠️ Disclaimer
Esta ferramenta foi desenvolvida apenas para fins educacionais e testes autorizados.
O uso indevido desta ferramenta é da inteira responsabilidade do utilizador.


👨‍💻 Autor
Mr Joker
🔗 https://github.com/mrjoker-web⁠�


📌 Roadmap
[ ] Detecção de tecnologias web
[ ] Exportação em CSV
[ ] Integração direta com ShadowSub
[ ] Suporte a proxies
[ ] Melhor parsing de títulos


⭐ Apoio
Se gostares do projeto, deixa uma ⭐ no repositório.


