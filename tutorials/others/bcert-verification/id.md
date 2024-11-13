---
name: ₿-CERT VERIFIKASI
description: Bagaimana cara memverifikasi keaslian sertifikat ₿ Anda?
---

![cover](assets/cover.webp)

Sertifikat ₿ adalah ujian yang diakui secara internasional yang mengevaluasi penguasaan Anda terhadap Bitcoin dan topik turunannya. Sertifikat ini akan memungkinkan Anda untuk membuktikan keterampilan dan pengetahuan Anda di industri Bitcoin, memberi Anda akses ke perusahaan-perusahaan terbaik dan posisi pekerjaan yang hebat.

Jika Anda lulus ujian, sertifikat yang ditandatangani secara digital dan diberi cap waktu akan dikeluarkan, untuk dapat membuktikan keterampilan Anda.

Temukan cara untuk memastikan keaslian dan integritas sertifikat Anda dalam dua langkah sederhana:

- Memverifikasi tanda tangan dari file teks sertifikat
- Memverifikasi cap waktu terbuka dari sertifikat

Kami akan menyediakan instruksi untuk metode antarmuka pengguna grafis (GUI) dan antarmuka baris perintah (CLI) untuk mengakomodasi preferensi pengguna dan latar belakang teknis yang berbeda.

## Unduh sertifikat Anda

Masuk ke dashboard PBN pribadi Anda, pergi ke halaman Credentials dengan mengklik menu di sisi kiri dan klik pada sesi ujian Anda dan temukan sertifikat yang ingin Anda verifikasi.
Unduh file zip dan ekstrak isinya dan Anda akan menemukan tiga file berbeda di dalamnya:

- File teks yang ditandatangani (mis., `certificate.txt.sig`)
- File Open Timestamp (OTS) (mis., `certificate.txt.ots`)
- Sertifikat PDF (mis., `certificate.pdf`)

## Langkah 1: Memverifikasi Tanda Tangan dari File Teks

### Metode GUI (menggunakan Sparrow Wallet)

1. Unduh dan instal Sparrow Wallet dari situs web resmi: https://www.sparrowwallet.com/.

2. Buka Sparrow Wallet dan pergi ke bagian "Tools".
   Klik pada opsi "Verify Message".

3. Di bidang "Message", tempelkan isi dari file teks yang ditandatangani (mis., `certificate.txt.sig`).

4. Di bidang "Address", masukkan kunci publik PBN: `0x7cb4528aa65f4e6a4375f87d5`

5. Klik tombol "Verify" untuk mengonfirmasi tanda tangan.

### Metode CLI (OpenSSL)

1. Buka terminal atau command prompt di komputer Anda.
   Navigasi ke direktori yang berisi file sertifikat yang diekstrak dari zip

2. Unduh file kunci publik PBN, yang dapat ditemukan di: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Jalankan perintah berikut untuk memverifikasi tanda tangan:

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Langkah 2: Memverifikasi Open Timestamp

### Metode GUI (OpenTimestamps)

1. Kunjungi situs web OpenTimestamps: https://opentimestamps.org/
2. Klik pada tab "Verify".
3. Seret dan lepaskan file OTS (mis., `certificate.txt.ots`) ke area yang ditentukan.
4. Situs web akan secara otomatis memverifikasi open timestamp dan menampilkan hasilnya.

### Metode CLI (OpenTimestamps)

1. Instal klien OpenTimestamps dari repositori resmi: https://github.com/opentimestamps/opentimestamps-client
2. Navigasi ke direktori yang berisi file sertifikat yang diekstrak.
3. Jalankan perintah berikut untuk memverifikasi open timestamp:

```bash
ots verify certificate.txt.ots
```