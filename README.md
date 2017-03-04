##AESHelper
AESHelper是一个使用Python 3.4编写的对明文密码进行加解密的小工具。加解密时使用AES/CBC/PKCS5Padding加密填充模式。

###Installation
``pip install git+https://github.com/liqinshan/AESHelper.git``

###Example

```python
import base64
from AESHelper import Helper

class Parser:
    def __init__(self, key, iv):
        self.aes = Helper.AesHelper(base64.b64decode(key), iv)
    
    def encrypt(self, text):
        data = self.aes.encrypt(text)
        return base64.b64encode(data)
    
    def decrypt(self, secret):
        data = base64.b64decode(secret)
        return self.aes.decrypt(data)

if __name__ == '__main__':
    key = "eqHSs48SCL2VoGsW1lWvDWKQ8Vu71UZJyS7Dbf/e4zo="
    parser = Parser(key=key, iv=None)

    plain = "server=192.168.1.100;uid=sa;pwd=123;database=mdb"
    print(parser.encrypt(plain))

    secret = b'qBclQuVaxf8qBmpEiKOfbTbnsb9Yfct0DPDqFoVRIPd1hvg5KgVmp9pfKevjvlrhZR7ovuDlIX03zZnTe5w9oA=='
    print(parser.decrypt(secret))    
```

