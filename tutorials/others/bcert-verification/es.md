---
name: ₿-CERT VERIFICATION
description: Cómo verificar la autenticidad de tu ₿-certificado?
---

![cover](assets/cover.webp)

El ₿ Certificado es un examen reconocido internacionalmente que evalúa tu dominio sobre Bitcoin y sus temas derivados. Este certificado te permitirá demostrar tus habilidades y conocimientos en la industria de Bitcoin, dándote acceso a las mejores empresas y excelentes posiciones laborales.

Si apruebas el examen, se emite un certificado firmado digitalmente y con marca de tiempo, para poder demostrar tus habilidades.

Descubre cómo asegurar la autenticidad e integridad de tu certificado en dos simples pasos:

- Verificando la firma del archivo de texto del certificado
- Verificando la marca de tiempo abierta del certificado

Proporcionaremos instrucciones para ambos métodos de interfaz gráfica de usuario (GUI) e interfaz de línea de comandos (CLI) para acomodar diferentes preferencias de usuarios y antecedentes técnicos.

## Descarga tu certificado

Inicia sesión en tu panel de control PBN personal, ve a la página de Credenciales haciendo clic en el menú del lado izquierdo y haz clic en tu sesión de examen y localiza el certificado que quieres verificar.
Descarga el archivo zip y extrae los contenidos y encontrarás tres archivos diferentes dentro:

- Archivo de texto firmado (por ejemplo, `certificate.txt.sig`)
- Archivo de marca de tiempo abierta (OTS) (por ejemplo, `certificate.txt.ots`)
- Certificado en PDF (por ejemplo, `certificate.pdf`)

## Paso 1: Verificando la Firma del Archivo de Texto

### Método GUI (usando Sparrow Wallet)

1. Descarga e instala Sparrow Wallet desde el sitio web oficial: https://www.sparrowwallet.com/.

2. Abre Sparrow Wallet y ve a la sección "Herramientas".
   Haz clic en la opción "Verificar Mensaje".

3. En el campo "Mensaje", pega el contenido del archivo de texto firmado (por ejemplo, `certificate.txt.sig`).

4. En el campo "Dirección", introduce la clave pública PBN: `0x7cb4528aa65f4e6a4375f87d5`

5. Haz clic en el botón "Verificar" para confirmar la firma.

### Método CLI (OpenSSL)

1. Abre un terminal o símbolo del sistema en tu computadora.
   Navega al directorio que contiene los archivos del certificado extraídos del zip

2. Descarga el archivo de clave pública PBN, que se puede encontrar en: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Ejecuta el siguiente comando para verificar la firma:

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Paso 2: Verificando la Marca de Tiempo Abierta

### Método GUI (OpenTimestamps)

1. Visita el sitio web de OpenTimestamps: https://opentimestamps.org/
2. Haz clic en la pestaña "Verificar".
3. Arrastra y suelta el archivo OTS (por ejemplo, `certificate.txt.ots`) en el área designada.
4. El sitio web verificará automáticamente la marca de tiempo abierta y mostrará el resultado.

### Método CLI (OpenTimestamps)

1. Instala el cliente OpenTimestamps desde el repositorio oficial: https://github.com/opentimestamps/opentimestamps-client
2. Navega al directorio que contiene los archivos del certificado extraídos.
3. Ejecuta el siguiente comando para verificar la marca de tiempo abierta:

```bash
ots verify certificate.txt.ots
```