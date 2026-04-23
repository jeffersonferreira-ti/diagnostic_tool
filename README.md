<div align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Focus-IT%20Support%20%26%20Infrastructure-1976D2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-MVP%20Complete-00C853?style=for-the-badge"/>

<br/><br/>

# System Diagnostic Tool

**Ferramenta de diagnostico de sistema e rede para suporte tecnico e infraestrutura**

*Diagnose. Analyze. Act.*

</div>

---

🧠 O Problema

No dia a dia de suporte tecnico, problemas comuns incluem:

| Problema | Impacto |
|---|---|
| Maquina lenta | Queda de produtividade |
| Falha de conexao | Interrupcao de servicos |
| Servicos inacessiveis | Usuarios bloqueados |
| Falta de diagnostico claro | Tempo alto de resolucao |

Muitas vezes, o diagnostico inicial e manual, repetitivo e sujeito a erro.

---

🚀 A Solucao

O **System Diagnostic Tool** automatiza a triagem inicial de problemas, coletando e analisando:

- estado do sistema
- conectividade de rede
- disponibilidade de servicos e portas
- resumo de problemas detectados

Tudo com saida clara e acionavel.

---

⚙️ Como Funciona

```text
Sistema -> Coleta de dados -> Analise -> Classificacao -> Relatorio -> CLI
```

Pipeline simples e focada em troubleshooting.

---

🔍 Funcionalidades

🖥️ System Diagnostics
- CPU usage
- Memory usage
- Disk usage
- Sistema operacional
- Arquitetura e processador

🌐 Network Diagnostics
- Hostname
- IP local
- Teste de DNS
- Teste de conectividade externa

🔌 Service Checks
- HTTP (80)
- HTTPS (443)
- RDP (3389)
- SSH (22)

📊 Analise
- Classificacao por severidade: `OK`, `WARNING`, `CRITICAL`, `FAILED`
- Destaque automatico de achados relevantes
- Status geral consolidado

🧾 Output
- Diagnostico no terminal
- Resumo com principais problemas
- Relatorio estruturado em JSON

---

📈 Exemplo de Execucao

```bash
python main.py
```

Exemplo de saida:

```text
System Diagnostic Tool v0.1.0

Hostname: DESKTOP-01

## System Information

OS: Windows 11
Architecture: AMD64
Processor: Intel64 Family

CPU Usage: 14% [OK]
Memory: 14.72GB / 16.00GB (92%) [CRITICAL]
Disk: 120.00GB free / 800.00GB (85%) [WARNING]

## Network Diagnostics

Local IP: 192.168.0.10
DNS Resolution: OK (google.com -> 142.250.79.14) [OK]
Connectivity: 8.8.8.8:53 -> OK [OK]
Connectivity: google.com:443 -> OK [OK]

## External Service Checks

google.com:80 -> OK [OK]
google.com:443 -> OK [OK]

## Local Service Checks

localhost:3389 -> FAILED [FAILED]
localhost:22 -> FAILED [FAILED]

## Summary

Overall Status: CRITICAL

Key Findings:

* High memory usage
* High disk usage
* RDP port unavailable
* SSH port unavailable

Report path: data/output/diagnostic_report.json
```

---

🧾 JSON Report

O sistema gera automaticamente um arquivo JSON em:

```text
data/output/diagnostic_report.json
```

Exemplo:

```json
{
  "hostname": "DESKTOP-01",
  "summary": {
    "overall_status": "WARNING",
    "key_findings": [
      "High disk usage",
      "RDP port unavailable"
    ]
  }
}
```

---

🖥️ Uso via CLI

Execucao padrao:

```bash
python main.py
```

Apenas resumo:

```bash
python main.py --summary-only
```

Sem gerar relatorio:

```bash
python main.py --no-report
```

Definir caminho do relatorio:

```bash
python main.py --output ./reports/host01.json
```

---

🧠 Diagnostico Inteligente

A ferramenta interpreta os dados coletados e gera insights objetivos:

- uso elevado de memoria -> possivel lentidao
- disco com alta ocupacao -> risco de falhas e indisponibilidade
- DNS falhando -> problema de resolucao
- portas fechadas -> servico indisponivel

---

🏗️ Arquitetura

```text
diagnostic_tool/
|-- app/
|   |-- models/
|   |-- network/
|   |-- ports/
|   |-- reporting/
|   `-- system/
|-- data/
|   `-- output/
|-- reports/
|-- main.py
|-- config.py
`-- requirements.txt
```

---

## Como Executar

**Pre-requisitos:** Python `3.10+`

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

⚠️ Limitacoes

- Nao substitui ferramentas corporativas de observabilidade
- Nao analisa logs ou processos avancados
- Nao realiza varredura completa de portas
- Focado em triagem inicial

---

🗺️ Roadmap

| Versao | Foco | Status |
|---|---|---|
| v1.0 | Diagnostico completo (system + network + ports) | ✅ Concluido |
| v1.1 | Refinamentos e melhorias de saida | ✅ Concluido |
| v1.2 | Relatorio JSON e CLI | ✅ Concluido |
| v2.0 | Integracao com logs | 📋 Planejado |
| v2.1 | Suporte a monitoramento continuo | 💡 Futuro |

---

## Objetivo do Projeto

Projeto desenvolvido para demonstrar:

- troubleshooting em ambientes reais
- diagnostico de sistema e rede
- automacao de tarefas de suporte
- boas praticas de arquitetura em Python

---


## 👨‍💻Desenvolvido por **Jefferson Ferreira**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/jefferson-ferreira-ti/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/jeffersonferreira-ti)

---

<div align="center">
<sub>System Diagnostic Tool - 2026</sub>
</div>
