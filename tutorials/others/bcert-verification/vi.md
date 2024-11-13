---
name: ₿-CERT VERIFICATION
description: Cách xác minh tính xác thực của chứng chỉ ₿ của bạn?
---

![cover](assets/cover.webp)

Chứng chỉ ₿ là một kỳ thi được công nhận trên toàn thế giới, đánh giá sự thành thạo của bạn về Bitcoin và các chủ đề liên quan. Chứng chỉ này sẽ giúp bạn chứng minh kỹ năng và kiến thức của mình trong ngành công nghiệp Bitcoin, mang lại cho bạn cơ hội tiếp cận với các công ty hàng đầu và vị trí công việc tuyệt vời.

Nếu bạn vượt qua kỳ thi, một chứng chỉ được ký số và dán thời gian sẽ được cấp, để bạn có thể chứng minh kỹ năng của mình.

Tìm hiểu cách đảm bảo tính xác thực và toàn vẹn của chứng chỉ của bạn qua hai bước đơn giản:

- Xác minh chữ ký của tệp văn bản chứng chỉ
- Xác minh thời gian mở của chứng chỉ

Chúng tôi sẽ cung cấp hướng dẫn cho cả phương pháp giao diện người dùng đồ họa (GUI) và giao diện dòng lệnh (CLI) để phù hợp với sở thích và nền tảng kỹ thuật khác nhau của người dùng.

## Tải xuống chứng chỉ của bạn

Đăng nhập vào bảng điều khiển PBN cá nhân của bạn, đi đến trang Credentials bằng cách nhấp vào menu bên trái và nhấp vào phiên thi của bạn và tìm chứng chỉ bạn muốn xác minh.
Tải xuống tệp zip và giải nén nội dung, bạn sẽ tìm thấy ba tệp khác nhau bên trong:

- Tệp văn bản đã ký (ví dụ: `certificate.txt.sig`)
- Tệp thời gian mở (OTS) (ví dụ: `certificate.txt.ots`)
- Chứng chỉ PDF (ví dụ: `certificate.pdf`)

## Bước 1: Xác minh Chữ ký của Tệp Văn bản

### Phương pháp GUI (sử dụng Sparrow Wallet)

1. Tải xuống và cài đặt Sparrow Wallet từ trang web chính thức: https://www.sparrowwallet.com/.

2. Mở Sparrow Wallet và đi đến mục "Tools".
   Nhấp vào tùy chọn "Verify Message".

3. Trong trường "Message", dán nội dung của tệp văn bản đã ký (ví dụ: `certificate.txt.sig`).

4. Trong trường "Address", nhập khóa công khai PBN: `0x7cb4528aa65f4e6a4375f87d5`

5. Nhấp vào nút "Verify" để xác nhận chữ ký.

### Phương pháp CLI (OpenSSL)

1. Mở một cửa sổ terminal hoặc command prompt trên máy tính của bạn.
   Di chuyển đến thư mục chứa các tệp chứng chỉ được giải nén từ tệp zip

2. Tải xuống tệp khóa công khai PBN, có thể tìm thấy tại: https://github.com/Asi0Flammeus/pgp-public-keys/blob/master/planb-network-pk.asc

3. Chạy lệnh sau để xác minh chữ ký:

```bash
openssl dgst -verify planb-network-pk.asc -signature certificate.txt.sig certificate.txt
```

## Bước 2: Xác minh Thời gian Mở

### Phương pháp GUI (OpenTimestamps)

1. Truy cập trang web OpenTimestamps: https://opentimestamps.org/
2. Nhấp vào tab "Verify".
3. Kéo và thả tệp OTS (ví dụ: `certificate.txt.ots`) vào khu vực được chỉ định.
4. Trang web sẽ tự động xác minh thời gian mở và hiển thị kết quả.

### Phương pháp CLI (OpenTimestamps)

1. Cài đặt client OpenTimestamps từ kho chính thức: https://github.com/opentimestamps/opentimestamps-client
2. Di chuyển đến thư mục chứa các tệp chứng chỉ đã giải nén.
3. Chạy lệnh sau để xác minh thời gian mở:

```bash
ots verify certificate.txt.ots
```