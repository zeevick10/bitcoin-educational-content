---
name: ₿-CERT VERIFIKATION
description: Wie man die Echtheit Ihres ₿-Zertifikats überprüft?
---

![cover](assets/cover.webp)

Das ₿-Zertifikat ist eine international anerkannte Prüfung, die Ihre Beherrschung von Bitcoin und den daraus abgeleiteten Themen bewertet. Dieses Zertifikat ermöglicht es Ihnen, Ihre Fähigkeiten und Kenntnisse in der Bitcoin-Branche nachzuweisen, was Ihnen Zugang zu den besten Unternehmen und großartigen Jobpositionen bietet.

Wenn Sie die Prüfung bestehen, wird ein digital signiertes und zeitgestempeltes Zertifikat ausgestellt, um Ihre Fähigkeiten nachweisen zu können.

Erfahren Sie, wie Sie in zwei einfachen Schritten die Echtheit und Integrität Ihres Zertifikats sicherstellen können:

- Überprüfung der Signatur der Textdatei des Zertifikats
- Überprüfung des offenen Zeitstempels des Zertifikats

Wir bieten Anleitungen sowohl für Methoden der grafischen Benutzeroberfläche (GUI) als auch der Befehlszeilenschnittstelle (CLI), um unterschiedlichen Benutzerpräferenzen und technischen Hintergründen gerecht zu werden.

## Laden Sie Ihr Zertifikat herunter

Loggen Sie sich in Ihr persönliches PBN-Dashboard ein, gehen Sie zur Seite "Credentials" (Zugangsdaten), indem Sie im Menü auf der linken Seite klicken, und klicken Sie auf Ihre Prüfungssitzung und lokalisieren Sie das Zertifikat, das Sie überprüfen möchten.
Laden Sie die Zip-Datei herunter und extrahieren Sie den Inhalt, und Sie werden drei verschiedene Dateien darin finden:

- Signierte Textdatei (z.B. `certificate.txt.sig`)
- Open Timestamp (OTS) Datei (z.B. `certificate.txt.ots`)
- PDF-Zertifikat (z.B. `certificate.pdf`)

## Schritt 1: Überprüfung der Signatur der Textdatei

### GUI-Methode (mit Sparrow Wallet)

1. Laden Sie das Sparrow Wallet von der offiziellen Website herunter und installieren Sie es: https://www.sparrowwallet.com/.

2. Öffnen Sie das Sparrow Wallet und gehen Sie zum Abschnitt "Tools".
   Klicken Sie auf die Option "Verify Message" (Nachricht überprüfen).

3. Fügen Sie im Feld "Message" (Nachricht) den Inhalt der signierten Textdatei ein (z.B. `certificate.txt.sig`).

4. Geben Sie im Feld "Address" (Adresse) den öffentlichen Schlüssel von PBN ein: `0x7cb4528aa65f4e6a4375f87d5`

5. Klicken Sie auf die Schaltfläche "Verify" (Überprüfen), um die Signatur zu bestätigen.

### CLI-Methode (OpenSSL)

1. Öffnen Sie ein Terminal oder eine Eingabeaufforderung auf Ihrem Computer.
   Navigieren Sie zum Verzeichnis, das die aus der Zip-Datei extrahierten Zertifikatsdateien enthält.

2. Laden Sie die PBN-öffentlichen Schlüsseldatei herunter, die Sie unter folgendem Link finden: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Führen Sie den folgenden Befehl aus, um die Signatur zu überprüfen:

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Schritt 2: Überprüfung des offenen Zeitstempels

### GUI-Methode (OpenTimestamps)

1. Besuchen Sie die OpenTimestamps-Website: https://opentimestamps.org/
2. Klicken Sie auf den Tab "Verify" (Überprüfen).
3. Ziehen Sie die OTS-Datei (z.B. `certificate.txt.ots`) in den dafür vorgesehenen Bereich.
4. Die Website wird automatisch den offenen Zeitstempel überprüfen und das Ergebnis anzeigen.

### CLI-Methode (OpenTimestamps)

1. Installieren Sie den OpenTimestamps-Client aus dem offiziellen Repository: https://github.com/opentimestamps/opentimestamps-client
2. Navigieren Sie zum Verzeichnis, das die extrahierten Zertifikatsdateien enthält.
3. Führen Sie den folgenden Befehl aus, um den offenen Zeitstempel zu überprüfen:

```bash
ots verify certificate.txt.ots
```