---
name: ₿-证书验证
description: 如何验证您的₿-证书的真实性？
---

![封面](assets/cover.webp)

₿ 证书是一个国际认可的考试，用于评估您对比特币及其衍生话题的掌握程度。这个证书将使您能够证明您在比特币行业的技能和知识，让您获得进入最佳公司和优秀职位的机会。

如果您通过了考试，将会发给您一份数字签名和时间戳的证书，以证明您的技能。

了解如何通过两个简单的步骤确保您的证书的真实性和完整性：

- 验证证书文本文件的签名
- 验证证书的开放时间戳

我们将为图形用户界面（GUI）和命令行界面（CLI）方法提供说明，以适应不同用户偏好和技术背景。

## 下载您的证书

登录到您的个人PBN仪表板，通过点击左侧菜单进入凭证页面，点击您的考试会话并找到您想要验证的证书。
下载zip文件并提取内容，您将在里面找到三个不同的文件：

- 签名的文本文件（例如，`certificate.txt.sig`）
- 开放时间戳（OTS）文件（例如，`certificate.txt.ots`）
- PDF证书（例如，`certificate.pdf`）

## 第1步：验证文本文件的签名

### GUI方法（使用Sparrow Wallet）

1. 从官方网站下载并安装Sparrow Wallet：https://www.sparrowwallet.com/。

2. 打开Sparrow Wallet并进入“工具”部分。
   点击“验证消息”选项。

3. 在“消息”字段中，粘贴签名文本文件的内容（例如，`certificate.txt.sig`）。

4. 在“地址”字段中，输入PBN公钥：`0x7cb4528aa65f4e6a4375f87d5`

5. 点击“验证”按钮以确认签名。

### CLI方法（OpenSSL）

1. 在您的计算机上打开终端或命令提示符。
   导航到从zip中提取的证书文件所在的目录

2. 下载PBN公钥文件，可以在此处找到：https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. 运行以下命令以验证签名：

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## 第2步：验证开放时间戳

### GUI方法（OpenTimestamps）

1. 访问OpenTimestamps网站：https://opentimestamps.org/
2. 点击“验证”标签页。
3. 将OTS文件（例如，`certificate.txt.ots`）拖放到指定区域。
4. 网站将自动验证开放时间戳并显示结果。

### CLI方法（OpenTimestamps）

1. 从官方仓库安装OpenTimestamps客户端：https://github.com/opentimestamps/opentimestamps-client
2. 导航到包含提取的证书文件的目录。
3. 运行以下命令以验证开放时间戳：

```bash
ots verify certificate.txt.ots
```