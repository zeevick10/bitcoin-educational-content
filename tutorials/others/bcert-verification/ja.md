---
name: ₿-CERT認証の検証
description: ₿-証明書の真正性をどのように確認しますか？
---

![cover](assets/cover.webp)

₿ 証明書は、Bitcoin及びその派生トピックの習熟度を評価する国際的に認識された試験です。この証明書により、Bitcoin業界におけるあなたのスキルと知識を証明し、最高の企業へのアクセスと素晴らしい職位を得ることができます。

試験に合格すると、スキルを証明できるようにデジタル署名されタイムスタンプが付けられた証明書が発行されます。

証明書の真正性と完全性を確保するための2つの簡単なステップを以下に示します：

- 証明書のテキストファイルの署名を検証する
- 証明書のオープンタイムスタンプを検証する

異なるユーザーの好みと技術的背景に対応するために、グラフィカルユーザーインターフェース（GUI）とコマンドラインインターフェース（CLI）の両方の方法について指示を提供します。

## 証明書のダウンロード

個人のPBNダッシュボードにログインし、左側のメニューをクリックしてCredentialsページに移動し、試験セッションをクリックして検証したい証明書を見つけます。
zipファイルをダウンロードして内容を抽出すると、以下の3つの異なるファイルが見つかります：

- 署名されたテキストファイル（例：`certificate.txt.sig`）
- オープンタイムスタンプ（OTS）ファイル（例：`certificate.txt.ots`）
- PDF証明書（例：`certificate.pdf`）

## ステップ1：テキストファイルの署名を検証する

### GUI方法（Sparrow Walletを使用）

1. 公式ウェブサイトからSparrow Walletをダウンロードしてインストールします：https://www.sparrowwallet.com/。

2. Sparrow Walletを開き、「Tools」セクションに移動します。
   「Verify Message」オプションをクリックします。

3. 「Message」フィールドに、署名されたテキストファイルの内容（例：`certificate.txt.sig`）を貼り付けます。

4. 「Address」フィールドに、PBN公開キー：`0x7cb4528aa65f4e6a4375f87d5`を入力します。

5. 「Verify」ボタンをクリックして署名を確認します。

### CLI方法（OpenSSL）

1. コンピューターで端末またはコマンドプロンプトを開きます。
   zipから抽出した証明書ファイルが含まれるディレクトリに移動します

2. PBN公開キーファイルをダウンロードします。これは以下で見つかります：https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. 署名を検証するために、以下のコマンドを実行します：

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## ステップ2：オープンタイムスタンプを検証する

### GUI方法（OpenTimestamps）

1. OpenTimestampsのウェブサイトを訪れます：https://opentimestamps.org/
2. 「Verify」タブをクリックします。
3. 指定されたエリアにOTSファイル（例：`certificate.txt.ots`）をドラッグアンドドロップします。
4. ウェブサイトは自動的にオープンタイムスタンプを検証し、結果を表示します。

### CLI方法（OpenTimestamps）

1. 公式リポジトリからOpenTimestampsクライアントをインストールします：https://github.com/opentimestamps/opentimestamps-client
2. 抽出した証明書ファイルが含まれるディレクトリに移動します。
3. オープンタイムスタンプを検証するために、以下のコマンドを実行します：

```bash
ots verify certificate.txt.ots
```