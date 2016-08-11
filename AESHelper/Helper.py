# -*-coding:utf-8 -*-
"""AES/CBC/PKCS5Padding加解密的工具

关于AES:
私钥aes_key的长度, 必须是16、24、或32个字节长度的一种;
初始向量aes_iv, ecb、cfb模式下不需要该参数, cbc模式下, 是一堆长度为AES.block_size的十六进制的0;
aes同时要求被加密的文本长度必须为16的倍数, 不足则补位填充。具体的填充方法由填充模式决定。

加解密顺序:
加密: 明文密码 --> 补位填充 --> (CBC)加密 --> base64编码 --> 加密字符串
解密: 加密字符串 --> base64解码 --> (CBC)解密 --> 去除填充 --> 明文密码

注意事项:
要注意的是, 加密/解密不能使用同一个AES对象, 即使他们的初始向量相同, 所以不能再初始化中生成aes对象。这个地方折腾了很久。。
Refer to: https://reality0ne.com/a-tip-of-pycrypto/
"""

import base64
from Crypto.Cipher import AES
from Crypto.Hash import MD5

__author__ = "lqs"


class AesHelper:
    def __init__(self, aes_key, aes_iv, mode=AES.MODE_CBC):
        """
        :param aes_key: 私钥
        :param aes_iv: 初始向量
        :param mode: aes加密模式, 默认cbc
        """
        self.aes_key = aes_key
        self.aes_iv = aes_iv
        self.aes_mode = mode

    @classmethod
    def _md5(cls, content):
        """生成初始向量"""
        m = MD5.new()
        try:
            m.update(content)
        except TypeError:
            m.update(content.encode())
        finally:
            return m.digest()

    @classmethod
    def padding(cls, data):
        """采用pkcs5/7的补位方式"""
        bs = AES.block_size
        pad = bs - len(data) % bs
        return data + pad * chr(pad)

    @classmethod
    def unpadding(cls, data):
        return data[0:-data[-1]]

    def _gen(self):
        """强制转换aes_key, aes_iv

        aes算法对密钥的长度有要求: 16、24、或32字节中的一种。我们使用的是32个字节长度。
        """
        if self.aes_key is None or len(self.aes_key) != 32:
            raise RuntimeError("invalid key")
        if self.aes_iv is None:
            self.aes_iv = self._md5(self.aes_key)

        return AES.new(self.aes_key, self.aes_mode, self.aes_iv)

    def encrypt(self, plaintext):
        cipher = self._gen()
        text = self.padding(plaintext)
        return cipher.encrypt(text)

    def decrypt(self, encrypted):
        cipher = self._gen()
        text = cipher.decrypt(encrypted)
        return self.unpadding(text)
