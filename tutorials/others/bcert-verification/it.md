---
name: VERIFICA B-CERT
description: Come verificare l'autenticita del tuo Certificato ₿?
---
![cover](assets/cover.webp)

Il ₿ Certificate è un esame riconosciuto a livello internazionale che valuta la tua padronanza di Bitcoin e degli argomenti collegati. Questo certificato ti permetterà di dimostrare le tue competenze e conoscenze nell'industria di Bitcoin, dandoti accesso alle migliori aziende e a posizioni lavorative di prestigio.

Se superi l'esame, ti verrà rilasciato un certificato firmato digitalmente e con data certa, in modo da poter dimostrare le tue abilità.

Scopri come garantire l'autenticità e l'integrità del tuo certificato in due semplici passaggi:

- Verifica della firma del file di testo del certificato
- Verifica del timestamp del certificato

Forniremo istruzioni per entrambi i metodi, sia tramite interfaccia grafica (GUI) sia tramite interfaccia a riga di comando (CLI), per adattarci alle diverse preferenze e livelli tecnici degli utenti.

## Scarica il tuo certificato

Accedi al tuo dashboard personale PBN, vai alla pagina Credenziali cliccando sul menu a sinistra, quindi seleziona la tua sessione d'esame e individua il certificato che desideri verificare.
Scarica il file zip ed estrai i contenuti: troverai tre file diversi al suo interno:

- File di testo firmato (ad es., `certificate.txt.sig`)
- File Open Timestamp (OTS) (ad es., `certificate.txt.ots`)
- Certificato in PDF (ad es., `certificate.pdf`)

## Passo 1: Verifica la firma del file di testo


### Metodo con interfaccia grafica (GUI) usando Sparrow Wallet

1. Scarica e installa Sparrow Wallet dal sito ufficiale: https://www.sparrowwallet.com/.

2. Apri Sparrow Wallet e vai alla sezione "Strumenti". Clicca sull'opzione "Verifica Messaggio".

3. Nel campo "Messaggio", incolla il contenuto del file di testo firmato (ad es., `certificate.txt.sig`).

4. Nel campo "Indirizzo", inserisci la chiave pubblica PBN: `0x7cb4528aa65f4e6a4375f87d5`.

5. Clicca sul pulsante "Verifica" per confermare la firma.

### Metodo da linea di comando (CLI) con OpenSSL

1. Apri un terminale o prompt dei comandi sul tuo computer.
Naviga nella directory contenente i file del certificato estratti dal file zip.

2. Scarica il file della chiave pubblica PBN, disponibile al seguente link: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc.

3. Esegui il seguente comando per verificare la firma:

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Passo 2: Verifica del timestamp 

### Metodo con interfaccia grafica (GUI) OpenTimestamps

1. Visit the OpenTimestamps website: https://opentimestamps.org/
2. Click on the "Verify" tab.
3. Drag and drop the OTS file (e.g., `certificate.txt.ots`) into the designated area.
4. The website will automatically verify the open timestamp and display the result.

### Metodo a linea di comando (CLI) OpenTimestamps

1. Installa il client OpenTimestamps dal repository ufficiale: https://github.com/opentimestamps/opentimestamps-client.

2. Naviga nella directory contenente i file del certificato estratti.

3. Esegui il seguente comando per verificare l'open timestamp:

```bash
ots verify certificate.txt.ots
```
