<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Version-1.0-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-HTTP%20Probe-red?style=for-the-badge"/>
</p>

<h1 align="center">⚡ ShadowProbe</h1>
<p align="center"><b>Fast HTTP/HTTPS Probe Tool for Reconnaissance</b></p>

---

## 📖 Sobre

**ShadowProbe** é uma ferramenta rápida e eficiente para identificar **hosts ativos** durante a fase de *reconnaissance* em pentesting.

Criada por **Mr Joker**, permite testar múltiplos alvos simultaneamente, detetando serviços HTTP/HTTPS, status codes e títulos das páginas.

---

## ⚡ Funcionalidades

- 🌐 Suporte a HTTP e HTTPS
- ⚡ Multi-threading (scan paralelo e rápido)
- 📊 Barra de progresso em tempo real
- 🧠 Extração automática do título da página
- 📁 Exportação de resultados em `.txt` e `.json`
- 🎨 Interface CLI com cores

---

## 🔗 Pipeline de Integração

ShadowProbe faz parte de um conjunto de tools criadas pelo Mr Joker:

```
ShadowSub   →  encontra subdomínios
     ↓
ShadowProbe →  verifica quais estão ativos
     ↓
ShadowScan  →  analisa portas e serviços
```

---

## ⚙️ Instalação

```bash
git clone https://github.com/mrjoker-web/ShadowProbe.git
cd ShadowProbe
pip install requests
```

---

## ▶️ Como usar

Uso básico com ficheiro de subdomínios:

```bash
python shadowprobe.py -l subdomains.txt
```

Com threads personalizadas (mais rápido):

```bash
python shadowprobe.py -l subdomains.txt --threads 100
```

---

## 📄 Input

Ficheiro de entrada `subdomains.txt` (um host por linha):

```
admin.example.com
api.example.com
dev.example.com
```

---

## 📸 Exemplo de Output

```
===========================================
       ShadowProbe - HTTP Probe Tool
       Author: Mr Joker
===========================================

[200] https://admin.example.com  | Admin Panel
[403] http://dev.example.com     | Forbidden
[200] https://api.example.com    | API Gateway

[##############################] 100.0%

[+] 2 hosts ativos encontrados
[+] Output guardado em live_hosts.txt e live_hosts.json
===========================================
```

---

## 📁 Ficheiros de Output

| Ficheiro | Formato | Uso |
|---|---|---|
| `live_hosts.txt` | Texto simples | Leitura rápida |
| `live_hosts.json` | JSON estruturado | Automação e scripts |

---

## 📌 Roadmap

- [ ] Detecção de tecnologias web
- [ ] Exportação em CSV
- [ ] Integração direta com ShadowSub

---

## ⚠️ Disclaimer

> Esta ferramenta foi desenvolvida **apenas para fins educacionais e testes em sistemas autorizados**.  
> O uso indevido é da **inteira responsabilidade do utilizador**.  
> Nunca uses esta ferramenta em sistemas sem autorização explícita.

---

## 👨‍💻 Autor

**Mr Joker**  
🔗 [github.com/mrjoker-web](https://github.com/mrjoker-web)  
🔒 Cybersecurity Enthusiast | Pentesting Tools Developer
