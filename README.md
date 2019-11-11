# An Unofficial API integration for Way2SMS.

## Usage

To integrate this API in your project

```bash
from way2sms import Way2Sms

msg = Way2Sms(username, password)
```

To send message

```bash
msg.send_sms(to_mobile_no, msg)
```
