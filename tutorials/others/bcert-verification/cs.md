---
name: ₿-CERT VERIFIKACE
description: Jak ověřit pravost vašeho ₿-certifikátu?
---

![cover](assets/cover.webp)

₿ Certifikát je mezinárodně uznávaná zkouška, která hodnotí vaši odbornost v oblasti Bitcoinu a odvozených témat. Tento certifikát vám umožní prokázat vaše dovednosti a znalosti v průmyslu Bitcoinu, což vám otevře dveře k nejlepším společnostem a skvělým pracovním pozicím.

Pokud zkoušku úspěšně složíte, obdržíte digitálně podepsaný a časově označený certifikát, abyste mohli prokázat své dovednosti.

Zjistěte, jak zajistit pravost a integritu vašeho certifikátu ve dvou jednoduchých krocích:

- Ověření podpisu textového souboru certifikátu
- Ověření otevřeného časového razítka certifikátu

Poskytneme návody pro obě metody grafického uživatelského rozhraní (GUI) a rozhraní příkazové řádky (CLI), aby byly vyhověny různým uživatelským preferencím a technickým zázemím.

## Stáhněte si svůj certifikát

Přihlaste se do svého osobního PBN dashboardu, přejděte na stránku Credentials kliknutím na menu na levé straně a klikněte na vaši zkouškovou session a najděte certifikát, který chcete ověřit.
Stáhněte zip soubor, extrahujte obsah a uvnitř najdete tři různé soubory:

- Podepsaný textový soubor (např. `certificate.txt.sig`)
- Soubor s otevřeným časovým razítkem (OTS) (např. `certificate.txt.ots`)
- PDF certifikát (např. `certificate.pdf`)

## Krok 1: Ověření podpisu textového souboru

### Metoda GUI (použitím Sparrow Wallet)

1. Stáhněte a nainstalujte Sparrow Wallet z oficiálního webu: https://www.sparrowwallet.com/.

2. Otevřete Sparrow Wallet a přejděte do sekce "Tools".
   Klikněte na možnost "Verify Message".

3. Do pole "Message" vložte obsah podepsaného textového souboru (např. `certificate.txt.sig`).

4. Do pole "Address" zadejte veřejný klíč PBN: `0x7cb4528aa65f4e6a4375f87d5`

5. Klikněte na tlačítko "Verify" pro potvrzení podpisu.

### Metoda CLI (OpenSSL)

1. Otevřete terminál nebo příkazový řádek na vašem počítači.
   Navigujte do adresáře obsahujícího extrahované soubory certifikátu

2. Stáhněte soubor s veřejným klíčem PBN, který lze najít na: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Spusťte následující příkaz pro ověření podpisu:

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Krok 2: Ověření otevřeného časového razítka

### Metoda GUI (OpenTimestamps)

1. Navštivte webovou stránku OpenTimestamps: https://opentimestamps.org/
2. Klikněte na záložku "Verify".
3. Přetáhněte soubor OTS (např. `certificate.txt.ots`) do určené oblasti.
4. Webová stránka automaticky ověří otevřené časové razítko a zobrazí výsledek.

### Metoda CLI (OpenTimestamps)

1. Nainstalujte klienta OpenTimestamps z oficiálního repozitáře: https://github.com/opentimestamps/opentimestamps-client
2. Navigujte do adresáře obsahujícího extrahované soubory certifikátu.
3. Spusťte následující příkaz pro ověření otevřeného časového razítka:

```bash
ots verify certificate.txt.ots
```