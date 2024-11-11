---
name: B-CERT VERIFICATION
description: How to verify authenticity of your B-certificate?
---
![cover](assets/cover.webp)

The ₿ Certificate is an internationally recognized exam that evaluates your mastery of Bitcoin and its derived topics. This certificate will enable you to prove your skills and knowledge in the Bitcoin industry, giving you access to the best companies and great job positions.

If you pass the exam a digitally signed and timestamped certificate is issued, to be able to prove your skills.

Find out how to ensure the authenticity and integrity of your certificate in two simple steps:
- Verifying the signature of the certificate's text file
- Verifying the open timestamp of the certificate

We'll provide instructions for both graphical user interface (GUI) and command-line interface (CLI) methods to accommodate different user preferences and technical backgrounds.

## Download your certificate

Log into your personal PBN dashboard, go to Credentials page by clicking on the lefthand-side menu and click on your exam session and locate the certificate you want to verify.
Download the zip file ef he certificate and extract the contents of your zip file and you will find three different files inside:

- Signed text file (e.g., certificate.txt.sig)
- Open timestamp (OTS) file (e.g., certificate.txt.ots)
- PDF certificate (e.g., certificate.pdf)

## Step 1: Verifying the Signature of the Text File


### GUI Method (using Sparrow Wallet)

Download and install the Sparrow Wallet from the official website: https://www.sparrowwallet.com/.
Open the Sparrow Wallet and go to the "Tools" section.
Click on the "Verify Message" option.
In the "Message" field, paste the contents of the signed text file (e.g., certificate.txt.sig).
In the "Address" field, enter the PBN public key: 0x7cb4528aa65f4e6a4375f87d5
Click the "Verify" button to confirm the signature.

### CLI Method (OpenSSL)

1. Open a terminal or command prompt on your computer.
Navigate to the directory containing the downloaded certificate files.

2. Download PBN public key file, which can be found at: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Run the following command to verify the signature:

```
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Step 2: Verifying the Open Timestamp

GUI Method (OpenTimestamps)

Visit the OpenTimestamps website: https://opentimestamps.org/
Click on the "Verify" tab.
Drag and drop the OTS file (e.g., certificate.txt.ots) into the designated area.
The website will automatically verify the open timestamp and display the result.

CLI Method (OpenTimestamps)

Install the OpenTimestamps client from the official repository: https://github.com/opentimestamps/opentimestamps-client
Navigate to the directory containing the downloaded certificate files.
Run the following command to verify the open timestamp:
