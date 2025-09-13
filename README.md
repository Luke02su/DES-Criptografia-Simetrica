# Criptografia Simétrica - DES Simplificado

Este projeto didático implementa uma versão **simplificada do DES (Data Encryption Standard)** totalmente do zero, sem utilizar bibliotecas externas de criptografia oriundas do **Python**.
O objetivo é demonstrar didaticamente como funciona a **cifragem e decifragem de mensagens** utilizando uma chave definida pelo usuário.
Enquanto estiver sendo executado, conforme é visto o passo-a-passo logo abaixo, as **mensagens cifradas permaneceram guardadas** até que o **terminal** que executa este **prompt** seja fechado por completo, ou seja, quando não estiver mais residente na **memória temporária** do computador.

---

## 🔐 O que é Criptografia Simétrica?

Na criptografia simétrica, a **mesma chave** é usada tanto para cifrar quanto para decifrar uma mensagem.  

- **Cifragem:** transforma o texto original (mensagem em claro) em dados ilegíveis chamados de **cifra**.  
- **Decifragem:** reverte o processo, recuperando a mensagem original a partir da cifra e da mesma chave utilizada.  

---

## ⚙️ Como Funciona

1. O usuário escolhe se deseja **cifrar** ou **decifrar**.  
2. Uma **chave** de até 8 caracteres deve ser fornecida.  
3. Durante a cifragem:  
   - A mensagem é dividida em blocos.  
   - É aplicado **padding** (preenchimento) quando necessário.  
   - Cada bloco é processado junto da chave usando operações lógicas (XOR).  
   - O resultado final é apresentado em **hexadecimal**.  
4. Durante a decifragem:  
   - O usuário informa a chave e o texto cifrado em hexadecimal.  
   - O algoritmo reverte o processo.  
   - A mensagem original é restaurada.  

---

## ▶️ Como Executar

1. Tenha o **Python 3.x** instalado.  
2. Baixe o código, ou copie-o e salve-o como **DES-criptografia-simetrica.py**. 
3. No terminal (CMD ou PowerShell), dentro da pasta na qual o arquivo **.py** está inserido, execute:

```bash
py DES-criptografia-simetrica.py
