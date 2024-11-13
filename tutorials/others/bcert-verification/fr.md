---
name: ₿-CERT VERIFICATION
description: Comment vérifier l'authenticité de votre ₿-certificat ?
---

![cover](assets/cover.webp)

Le ₿ Certificat est un examen reconnu internationalement qui évalue votre maîtrise de Bitcoin et des sujets qui en découlent. Ce certificat vous permettra de prouver vos compétences et vos connaissances dans l'industrie du Bitcoin, vous donnant accès aux meilleures entreprises et à d'excellentes positions professionnelles.

Si vous réussissez l'examen, un certificat signé numériquement et horodaté est émis, pour pouvoir prouver vos compétences.

Découvrez comment assurer l'authenticité et l'intégrité de votre certificat en deux étapes simples :

- Vérifier la signature du fichier texte du certificat
- Vérifier le timestamp ouvert du certificat

Nous fournirons des instructions pour les méthodes d'interface graphique (GUI) et d'interface en ligne de commande (CLI) afin de répondre aux différentes préférences des utilisateurs et aux antécédents techniques.

## Téléchargez votre certificat

Connectez-vous à votre tableau de bord PBN personnel, allez à la page Credentials en cliquant sur le menu latéral gauche et cliquez sur votre session d'examen puis localisez le certificat que vous souhaitez vérifier.
Téléchargez le fichier zip et extrayez le contenu et vous trouverez trois fichiers différents à l'intérieur :

- Fichier texte signé (par exemple, `certificate.txt.sig`)
- Fichier de timestamp ouvert (OTS) (par exemple, `certificate.txt.ots`)
- Certificat PDF (par exemple, `certificate.pdf`)

## Étape 1 : Vérification de la Signature du Fichier Texte

### Méthode GUI (en utilisant Sparrow Wallet)

1. Téléchargez et installez Sparrow Wallet depuis le site officiel : https://www.sparrowwallet.com/.

2. Ouvrez Sparrow Wallet et allez à la section "Outils".
   Cliquez sur l'option "Vérifier le message".

3. Dans le champ "Message", collez le contenu du fichier texte signé (par exemple, `certificate.txt.sig`).

4. Dans le champ "Adresse", entrez la clé publique PBN : `0x7cb4528aa65f4e6a4375f87d5`

5. Cliquez sur le bouton "Vérifier" pour confirmer la signature.

### Méthode CLI (OpenSSL)

1. Ouvrez un terminal ou une invite de commande sur votre ordinateur.
   Naviguez jusqu'au répertoire contenant les fichiers du certificat extraits du zip

2. Téléchargez le fichier de clé publique PBN, qui peut être trouvé à : https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Exécutez la commande suivante pour vérifier la signature :

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Étape 2 : Vérification du Timestamp Ouvert

### Méthode GUI (OpenTimestamps)

1. Visitez le site web OpenTimestamps : https://opentimestamps.org/
2. Cliquez sur l'onglet "Vérifier".
3. Glissez et déposez le fichier OTS (par exemple, `certificate.txt.ots`) dans la zone désignée.
4. Le site web vérifiera automatiquement le timestamp ouvert et affichera le résultat.

### Méthode CLI (OpenTimestamps)

1. Installez le client OpenTimestamps depuis le dépôt officiel : https://github.com/opentimestamps/opentimestamps-client
2. Naviguez jusqu'au répertoire contenant les fichiers du certificat extraits.
3. Exécutez la commande suivante pour vérifier le timestamp ouvert :

```bash
ots verify certificate.txt.ots
```