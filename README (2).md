# TP2 – Simulação e Detecção de SQL Injection 🔒

Trabalho prático da disciplina **Tópicos Avançados em Segurança Computacional – 2025/1**, Universidade de Brasília (UnB). O objetivo é criar um ambiente vulnerável, simular ataques de SQL Injection e implementar ferramentas de monitoramento e mitigação.

---

## 📌 Objetivos

- Implantar um ambiente web vulnerável usando Docker
- Executar ataques de SQL Injection (manuais e automatizados)
- Detectar e mitigar ataques com ferramentas como firewall e Snort
- Coletar e analisar logs
- Documentar o processo em relatório técnico

---

## 🛠️ Tecnologias e Ferramentas

| Componente      | Ferramenta usada                  |
|----------------|-----------------------------------|
| Ambiente Web   | SQLi-Labs (via Docker)            |
| Ataque         | sqlmap, ataques manuais           |
| IDS            | Snort                             |
| Firewall       | UFW                               |
| Monitoramento  | Script Python + análise de logs   |
| Versionamento  | Git + GitHub                      |

---

## 🧱 Estrutura do Projeto

```
tp2-sql-injection/
├── README.md                # Este arquivo
├── relatorio/               # Relatório final e evidências
│   ├── relatorio.pdf
│   ├── topologia.png
│   └── capturas/
├── scripts/                 # Scripts de monitoramento e automação
│   ├── monitor_snort_log.py
├── logs/                    # Logs coletados
│   ├── sqlmap_output.txt
│   └── snort_alerts.log
├── docker/                  # Comandos e observações de setup
│   └── comandos_utilizados.txt
└── .gitignore
```

---

## ⚙️ Como executar o ambiente

```bash
# Clonar este repositório
git clone https://github.com/SEU_USUARIO/tp2-sql-injection.git
cd tp2-sql-injection

# Rodar o SQLi-Labs
docker run -d -p 8080:80 --name sqli-labs acgpiano/sqli-labs:latest

# Acessar no navegador
http://localhost:8080
```

---

## 💥 Como simular um ataque

```bash
# Listar bancos de dados
sqlmap -u "http://localhost:8080/Less-1/?id=1" --dbs

# Dump de dados
sqlmap -u "http://localhost:8080/Less-1/?id=1" -D security -T users --dump
```

---

## 🕵️‍♀️ Como detectar e mitigar

### Rodar Snort:
```bash
sudo snort -A console -i lo -c /etc/snort/snort.conf
```

### Rodar script de monitoramento:
```bash
python3 scripts/monitor_snort_log.py
```

### Mitigar ataque (exemplo com UFW):
```bash
sudo ufw deny from <IP do atacante>
```

---

## 🧾 Relatório

O relatório final em PDF está disponível em `relatorio/relatorio.pdf` com:

- Topologia
- Etapas do ataque
- Logs e capturas
- Análise e resposta ao incidente

---

## 👩‍💻 Autores

- [Seu Nome] – DRE xxxxxxxxx
- [Parceiro, se tiver]

---

## 📄 Licença

Este projeto é acadêmico e de uso educacional. Não utilize nenhuma técnica aqui descrita em sistemas reais sem autorização explícita.
