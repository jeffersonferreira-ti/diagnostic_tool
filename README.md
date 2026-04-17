<div align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Focus-IT%20Support%20%26%20Infrastructure-1976D2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-MVP%20Complete-00C853?style=for-the-badge"/>

<br/><br/>

# System Diagnostic Tool

**Ferramenta de diagnóstico de sistema e rede para suporte técnico e infraestrutura**

*Diagnose. Analyze. Act.*

</div>

---

## 🧠 O Problema

No dia a dia de suporte técnico, problemas comuns incluem:

| Problema | Impacto |
|---|---|
| Máquina lenta | Queda de produtividade |
| Falha de conexão | Interrupção de serviços |
| Serviços inacessíveis | Usuários bloqueados |
| Falta de diagnóstico claro | Tempo alto de resolução |

Muitas vezes, o diagnóstico inicial é manual, repetitivo e sujeito a erro.

---

## 🚀 A Solução

O **System Diagnostic Tool** automatiza a triagem inicial de problemas, coletando e analisando:

- estado do sistema
- conectividade de rede
- disponibilidade de serviços (portas)
- resumo de problemas detectados

Tudo com saída clara e acionável.

---

## ⚙️ Como Funciona


Sistema → Coleta de dados → Análise → Classificação → Relatório → CLI


Pipeline simples e focada em troubleshooting.

---

## 🔍 Funcionalidades

### 🖥️ System Diagnostics
- CPU usage
- Memory usage
- Disk usage
- Sistema operacional
- Arquitetura e processador

### 🌐 Network Diagnostics
- IP local
- Teste de DNS
- Teste de conectividade externa

### 🔌 Service Checks
- HTTP (80)
- HTTPS (443)
- RDP (3389)
- SSH (22)

### 📊 Análise
- Classificação por severidade:
  - OK
  - WARNING
  - CRITICAL
  - FAILED

### 🧾 Output
- Diagnóstico no terminal
- Resumo com principais problemas
- Relatório estruturado em JSON

---

## 📈 Exemplo de Execução

```bash
python main.py
Output
System Diagnostic Tool v0.1.0

Hostname: DESKTOP-01

## System Information

CPU Usage: 14% [OK]
Memory: 92% [CRITICAL]
Disk: 85% [WARNING]

## Network Diagnostics

DNS Resolution: OK [OK]
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
- High memory usage
- High disk usage
- RDP port unavailable
- SSH port unavailable
🧾 JSON Report

O sistema gera automaticamente:

data/output/diagnostic_report.json

Exemplo:

{
  "hostname": "DESKTOP-01",
  "overall_status": "WARNING",
  "key_findings": [
    "High disk usage",
    "RDP port unavailable"
  ]
}
🖥️ Uso via CLI
Execução padrão
python main.py
Apenas resumo
python main.py --summary-only
Sem gerar relatório
python main.py --no-report
Definir caminho do relatório
python main.py --output ./reports/host01.json
🧠 Diagnóstico Inteligente

A ferramenta interpreta dados e gera insights:

uso elevado de memória → possível lentidão
disco cheio → risco de falhas
DNS falhando → problema de resolução
portas fechadas → serviço indisponível
🏗️ Arquitetura
diagnostic_tool/
├── app/
│   ├── system/
│   ├── network/
│   ├── ports/
│   ├── reporting/
│   └── models/
├── data/
│   └── output/
├── main.py
├── config.py
└── requirements.txt
⚠️ Limitações
Não substitui ferramentas corporativas
Não analisa logs ou processos avançados
Não realiza varredura completa de portas
Focado em triagem inicial
🗺️ Roadmap
Versão	Foco	Status
v1.0	Diagnóstico completo (system + network + ports)	✅ Concluído
v1.1	Refinamentos e melhorias de saída	✅ Concluído
v1.2	Relatório JSON e CLI	✅ Concluído
v2.0	Integração com logs	📋 Planejado
v2.1	Suporte a monitoramento contínuo	💡 Futuro
🎯 Objetivo do Projeto

Projeto desenvolvido para demonstrar:

troubleshooting em ambientes reais
diagnóstico de sistema e rede
automação de tarefas de suporte
boas práticas de arquitetura


👨‍💻 Sobre o Desenvolvedor

Desenvolvido por Jefferson Ferreira




<div align="center"> <sub>System Diagnostic Tool · 2026</sub> </div>