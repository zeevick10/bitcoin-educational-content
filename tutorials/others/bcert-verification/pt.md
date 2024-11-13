---
name: ₿-CERT VERIFICAÇÃO
description: Como verificar a autenticidade do seu ₿-certificado?
---

![cover](assets/cover.webp)

O ₿ Certificado é um exame reconhecido internacionalmente que avalia sua maestria sobre o Bitcoin e seus tópicos derivados. Este certificado permitirá que você comprove suas habilidades e conhecimento na indústria do Bitcoin, dando-lhe acesso às melhores empresas e ótimas posições de trabalho.

Se você passar no exame, um certificado digitalmente assinado e com timestamp é emitido, para poder comprovar suas habilidades.

Descubra como garantir a autenticidade e integridade do seu certificado em dois passos simples:

- Verificando a assinatura do arquivo de texto do certificado
- Verificando o timestamp aberto do certificado

Forneceremos instruções para ambos os métodos de interface gráfica do usuário (GUI) e interface de linha de comando (CLI) para acomodar diferentes preferências de usuários e antecedentes técnicos.

## Baixe seu certificado

Faça login no seu painel PBN pessoal, vá para a página de Credenciais clicando no menu do lado esquerdo e clique na sua sessão de exame e localize o certificado que você deseja verificar.
Baixe o arquivo zip e extraia o conteúdo e você encontrará três arquivos diferentes dentro:

- Arquivo de texto assinado (por exemplo, `certificate.txt.sig`)
- Arquivo de timestamp aberto (OTS) (por exemplo, `certificate.txt.ots`)
- Certificado em PDF (por exemplo, `certificate.pdf`)

## Passo 1: Verificando a Assinatura do Arquivo de Texto

### Método GUI (usando Sparrow Wallet)

1. Baixe e instale o Sparrow Wallet do site oficial: https://www.sparrowwallet.com/.

2. Abra o Sparrow Wallet e vá para a seção "Ferramentas".
   Clique na opção "Verificar Mensagem".

3. No campo "Mensagem", cole o conteúdo do arquivo de texto assinado (por exemplo, `certificate.txt.sig`).

4. No campo "Endereço", insira a chave pública PBN: `0x7cb4528aa65f4e6a4375f87d5`

5. Clique no botão "Verificar" para confirmar a assinatura.

### Método CLI (OpenSSL)

1. Abra um terminal ou prompt de comando no seu computador.
   Navegue até o diretório contendo os arquivos do certificado extraídos do zip

2. Baixe o arquivo de chave pública PBN, que pode ser encontrado em: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Execute o seguinte comando para verificar a assinatura:

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Passo 2: Verificando o Timestamp Aberto

### Método GUI (OpenTimestamps)

1. Visite o site do OpenTimestamps: https://opentimestamps.org/
2. Clique na aba "Verificar".
3. Arraste e solte o arquivo OTS (por exemplo, `certificate.txt.ots`) na área designada.
4. O site verificará automaticamente o timestamp aberto e exibirá o resultado.

### Método CLI (OpenTimestamps)

1. Instale o cliente OpenTimestamps do repositório oficial: https://github.com/opentimestamps/opentimestamps-client
2. Navegue até o diretório contendo os arquivos do certificado extraídos.
3. Execute o seguinte comando para verificar o timestamp aberto:

```bash
ots verify certificate.txt.ots
```