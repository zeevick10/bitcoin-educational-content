---
name: ₿-CERT VERIFISERING
description: Hvordan verifisere ektheten av ditt ₿-sertifikat?
---

![cover](assets/cover.webp)

₿-sertifikatet er en internasjonalt anerkjent eksamen som evaluerer din mestring av Bitcoin og relaterte emner. Dette sertifikatet vil gjøre det mulig for deg å bevise dine ferdigheter og kunnskap i Bitcoin-industrien, og gi deg tilgang til de beste selskapene og flotte jobbposisjoner.

Hvis du består eksamenen, utstedes et digitalt signert og tidsstemplet sertifikat, for å kunne bevise dine ferdigheter.

Finn ut hvordan du sikrer ektheten og integriteten til sertifikatet ditt i to enkle trinn:

- Verifisere signaturen til sertifikatets tekstfil
- Verifisere det åpne tidsstempelet til sertifikatet

Vi vil gi instruksjoner for både grafisk brukergrensesnitt (GUI) og kommandolinjegrensesnitt (CLI) metoder for å imøtekomme ulike brukerpreferanser og tekniske bakgrunner.

## Last ned sertifikatet ditt

Logg inn på ditt personlige PBN-dashboard, gå til Credentials-siden ved å klikke på menyen på venstre side og klikk på din eksamensøkt og finn sertifikatet du vil verifisere.
Last ned zip-filen og pakk ut innholdet, og du vil finne tre forskjellige filer inne:

- Signert tekstfil (f.eks., `certificate.txt.sig`)
- Åpent tidsstempel (OTS) fil (f.eks., `certificate.txt.ots`)
- PDF-sertifikat (f.eks., `certificate.pdf`)

## Trinn 1: Verifisere Signaturen til Tekstfilen

### GUI-metode (ved bruk av Sparrow Wallet)

1. Last ned og installer Sparrow Wallet fra den offisielle nettsiden: https://www.sparrowwallet.com/.

2. Åpne Sparrow Wallet og gå til "Verktøy"-seksjonen.
   Klikk på "Verifiser Melding"-alternativet.

3. I "Melding"-feltet, lim inn innholdet av den signerte tekstfilen (f.eks., `certificate.txt.sig`).

4. I "Adresse"-feltet, skriv inn PBN offentlig nøkkel: `0x7cb4528aa65f4e6a4375f87d5`

5. Klikk på "Verifiser"-knappen for å bekrefte signaturen.

### CLI-metode (OpenSSL)

1. Åpne en terminal eller kommandoprompt på datamaskinen din.
   Naviger til mappen som inneholder sertifikatfilene pakket ut fra zip

2. Last ned PBN offentlig nøkkelfil, som kan finnes på: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Kjør følgende kommando for å verifisere signaturen:

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Trinn 2: Verifisere det Åpne Tidsstempelet

### GUI-metode (OpenTimestamps)

1. Besøk OpenTimestamps-nettsiden: https://opentimestamps.org/
2. Klikk på "Verifiser"-fanen.
3. Dra og slipp OTS-filen (f.eks., `certificate.txt.ots`) inn i det angitte området.
4. Nettsiden vil automatisk verifisere det åpne tidsstempelet og vise resultatet.

### CLI-metode (OpenTimestamps)

1. Installer OpenTimestamps-klienten fra det offisielle repositoriet: https://github.com/opentimestamps/opentimestamps-client
2. Naviger til mappen som inneholder de utpakkede sertifikatfilene.
3. Kjør følgende kommando for å verifisere det åpne tidsstempelet:

```bash
ots verify certificate.txt.ots
```