---
name: ₿-CERT VARMENNUS
description: Kuinka varmistaa ₿-sertifikaattisi aitouden?
---

![cover](assets/cover.webp)

₿-sertifikaatti on kansainvälisesti tunnustettu tutkinto, joka arvioi osaamisesi Bitcoinista ja sen johdannaisaiheista. Tämä sertifikaatti mahdollistaa taitojesi ja tietosi todistamisen Bitcoin-teollisuudessa, antaen sinulle pääsyn parhaisiin yrityksiin ja loistaviin työtehtäviin.

Läpäistyäsi kokeen sinulle myönnetään digitaalisesti allekirjoitettu ja aikaleimattu sertifikaatti, jotta voit todistaa taitosi.

Opi, kuinka varmistaa sertifikaattisi aitouden ja eheyden kahdessa yksinkertaisessa vaiheessa:

- Sertifikaatin tekstitiedoston allekirjoituksen varmistaminen
- Sertifikaatin avoimen aikaleiman varmistaminen

Tarjoamme ohjeet sekä graafisen käyttöliittymän (GUI) että komentorivin (CLI) menetelmiin eri käyttäjämieltymysten ja teknisten taustojen mukauttamiseksi.

## Lataa sertifikaattisi

Kirjaudu henkilökohtaiseen PBN-kojelautaasi, siirry Todistukset-sivulle napsauttamalla vasemmanpuoleista valikkoa ja napsauta tenttisessiotasi ja etsi haluamasi sertifikaatti.
Lataa zip-tiedosto ja pura sen sisältö, niin löydät kolme erilaista tiedostoa:

- Allekirjoitettu tekstitiedosto (esim. `certificate.txt.sig`)
- Avoin aikaleimatiedosto (OTS) (esim. `certificate.txt.ots`)
- PDF-sertifikaatti (esim. `certificate.pdf`)

## Vaihe 1: Tekstitiedoston allekirjoituksen varmistaminen

### GUI-menetelmä (käyttäen Sparrow Walletia)

1. Lataa ja asenna Sparrow Wallet viralliselta verkkosivustolta: https://www.sparrowwallet.com/.

2. Avaa Sparrow Wallet ja siirry "Työkalut"-osioon.
   Napsauta "Vahvista viesti"-vaihtoehtoa.

3. "Viesti"-kenttään, liitä allekirjoitetun tekstitiedoston sisältö (esim. `certificate.txt.sig`).

4. "Osoite"-kenttään, syötä PBN:n julkinen avain: `0x7cb4528aa65f4e6a4375f87d5`

5. Napsauta "Vahvista"-painiketta vahvistaaksesi allekirjoituksen.

### CLI-menetelmä (OpenSSL)

1. Avaa terminaali tai komentokehote tietokoneellasi.
   Siirry hakemistoon, joka sisältää zip-tiedostosta puretut sertifikaattitiedostot

2. Lataa PBN:n julkinen avaintiedosto, joka löytyy osoitteesta: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Suorita seuraava komento varmistaaksesi allekirjoituksen:

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Vaihe 2: Avoimen aikaleiman varmistaminen

### GUI-menetelmä (OpenTimestamps)

1. Vieraile OpenTimestamps-verkkosivustolla: https://opentimestamps.org/
2. Napsauta "Vahvista"-välilehteä.
3. Vedä ja pudota OTS-tiedosto (esim. `certificate.txt.ots`) määritettyyn alueeseen.
4. Verkkosivusto vahvistaa automaattisesti avoimen aikaleiman ja näyttää tuloksen.

### CLI-menetelmä (OpenTimestamps)

1. Asenna OpenTimestamps-asiakasohjelma virallisesta repositoriosta: https://github.com/opentimestamps/opentimestamps-client
2. Siirry hakemistoon, joka sisältää puretut sertifikaattitiedostot.
3. Suorita seuraava komento varmistaaksesi avoimen aikaleiman:

```bash
ots verify certificate.txt.ots
```