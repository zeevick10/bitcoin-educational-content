---
name: ₿-CERT VERIFITSEERIMINE
description: Kuidas kontrollida oma ₿-sertifikaadi autentsust?
---

![kaas](assets/cover.webp)

₿ Sertifikaat on rahvusvaheliselt tunnustatud eksam, mis hindab teie oskusi Bitcoin'i ja sellega seotud teemadel. See sertifikaat võimaldab teil tõestada oma oskusi ja teadmisi Bitcoin'i tööstuses, andes teile juurdepääsu parimatele ettevõtetele ja suurepärastele töökohtadele.

Kui läbite eksami, väljastatakse digitaalselt allkirjastatud ja ajatempliga sertifikaat, et saaksite tõestada oma oskusi.

Uurige, kuidas tagada oma sertifikaadi autentsus ja terviklikkus kahe lihtsa sammu abil:

- Sertifikaadi tekstifaili allkirja kontrollimine
- Sertifikaadi avatud ajatempli kontrollimine

Pakume juhiseid nii graafilise kasutajaliidese (GUI) kui ka käsurea liidese (CLI) meetodite jaoks, et mahutada erinevaid kasutajaeelistusi ja tehnilisi taustu.

## Laadige alla oma sertifikaat

Logige sisse oma isiklikule PBN-i armatuurlauale, minge volituste lehele, klõpsates vasakpoolse menüü peal ja klõpsake oma eksamiseansil ning leidke sertifikaat, mida soovite kontrollida.
Laadige alla zip-fail ja ekstraheerige sisu ning leiate seest kolm erinevat faili:

- Allkirjastatud tekstifail (nt `certificate.txt.sig`)
- Avatud ajatempli (OTS) fail (nt `certificate.txt.ots`)
- PDF-sertifikaat (nt `certificate.pdf`)

## 1. samm: Tekstifaili allkirja kontrollimine

### GUI meetod (kasutades Sparrow Wallet'i)

1. Laadige alla ja installige Sparrow Wallet ametlikult veebilehelt: https://www.sparrowwallet.com/.

2. Avage Sparrow Wallet ja minge jaotisse "Tools".
   Klõpsake valikul "Verify Message".

3. "Message" väljale kleepige allkirjastatud tekstifaili sisu (nt `certificate.txt.sig`).

4. "Address" väljale sisestage PBN avalik võti: `0x7cb4528aa65f4e6a4375f87d5`

5. Klõpsake nupul "Verify", et kinnitada allkiri.

### CLI meetod (OpenSSL)

1. Avage oma arvutis terminal või käsurida.
   Liikuge kataloogi, kus on zip-failist ekstraheeritud sertifikaadifailid

2. Laadige alla PBN avalik võtmefail, mida saab leida aadressilt: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Käivitage järgmine käsk allkirja kontrollimiseks:

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## 2. samm: Avatud ajatempli kontrollimine

### GUI meetod (OpenTimestamps)

1. Külastage OpenTimestamps veebilehte: https://opentimestamps.org/
2. Klõpsake vahekaardil "Verify".
3. Lohistage OTS-fail (nt `certificate.txt.ots`) määratud alasse.
4. Veebileht kontrollib automaatselt avatud ajatemplit ja kuvab tulemuse.

### CLI meetod (OpenTimestamps)

1. Installige OpenTimestamps klient ametlikust repositooriumist: https://github.com/opentimestamps/opentimestamps-client
2. Liikuge kataloogi, kus on ekstraheeritud sertifikaadifailid.
3. Käivitage järgmine käsk avatud ajatemplit kontrollimiseks:

```bash
ots verify certificate.txt.ots
```