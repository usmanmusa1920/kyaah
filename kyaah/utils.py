# -*- coding: utf-8 -*-
import json
import math
import random
import geocoder
import requests
# from itsdangerous import Serializer #(itsdangerous==2.1.2)
# from itsdangerous.serializer import Serializer #(itsdangerous==2.1.2)
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer #(itsdangerous==0.24)


SECRET_KEY = '5068b4fec3aadefef830137fcee44af81751d6c6a09b6f7eef' # use your secrets key


class Tokens:
    """The base class for OTP mail"""
    
    def mail_otp(self, _range=6):
        """send otp code"""
        digits = '0123456789'
        OTP = ''
        for _ in range(_range):
            OTP += digits[math.floor(random.random()*10)]
        return OTP
    

class Faker:
    """
    Class that give you random email address
    """
    
    _source = ['https://www.guerrillamail.com/ajax.php?f=get_email_address&ip=', '&agent=Mozilla_foo_bar']
    
    def __init__(self, url=_source, ip='me'):
        """Faker init"""
        self.url = url
        self.ip = ip

    def what_ip(self):
        """Find ip address of the requester"""
        g = geocoder.ip(self.ip).raw
        ip = g.get('ip')
        return ip
    
    @property
    def make_request(self):
        """
        This method make a request along side with an ip address from `what_ip` method of this class
        """
        url_first = self.url[0]
        url_mid = self.url[1]
        url_end = self.what_ip()
        
        com_url = url_first + url_end + url_mid
        r = requests.get(com_url).text
        return r
    
    def faker(self) -> dict:
        """Give the actual maill address generated from guerrillamail"""
        gue_raw = json.loads(self.make_request)
        _fake = gue_raw['email_addr']
        return {'fake_email': _fake}
    

class IzitDanger:
    """
    IzitDanger class for generating salting 🤔
    
    A reqular expression that matches any character that
    should never appear in base 64 encodings would be:
    [^A-Za-z0-9+/=]

    we follow the base64 pattern of [^A-Za-z0-9+/=] that should never appear in base64, (in regex)

    NOTE: usage:
        >>> pass_cls = IzitDanger()
        >>> pass_salt = pass_cls._salt
        >>> print(pass_salt)
    """

    token_sm_alpha = 'abcdefghijklmnopqrstuvwxyz'
    token_cap_alpha = token_sm_alpha.upper()
    token_num = '0123456789'
    # token_char = '/+='
    token_sum = token_sm_alpha + token_cap_alpha + token_num

    # We times the above variable (token_sum) by 2 (total length is 124),
    # so that we will randomly select from it without any restriction,
    # since we make the minimum length of the salt to be 32 and the maximum to be 64,
    # and also it will randomly select from that range of (32 - 64)

    token_times = token_sum * 2
    token_list = list(token_times)
    random.shuffle(token_list) # shuffling the above list
    token_generate = ''.join(token_list)
    
    def __init__(self, token_generate = token_generate):
        self.token_generate = ''.join(token_generate)
        
    @property
    def _salt(self):
        """
        Salting with this class method

        By using the random sample method, where we make:
            population = self.token_generate
            k = random.randint(32, 64)
        """
        salt = ''.join(random.sample(self.token_generate, random.randint(32, 64)))
        return salt # return type is string
    
    @staticmethod
    def get_token(expires_sec=1):
        """Get token"""
        s = Serializer(SECRET_KEY, expires_sec * 60)
        # s = Serializer(SECRET_KEY) #(itsdangerous==2.1.2)
        mysecret = IzitDanger()._salt
        # return s.dumps([1,2,3,4])
        # return s.dumps('mysecret')
        return s.dumps(mysecret)
    
    @staticmethod
    def verify_token(token):
        """Verify token (sign)"""
        s = Serializer(SECRET_KEY)
        try:
            load_token = s.loads(token)
        except:
            return None
        return load_token
    
    def __str__(self):
        """Dunder str"""
        return f'IzitDanger class'
    
    
class Box: ...

# from itsdangerous import TimestampSigner as ts
# s = ts('secretkey')
# string = s.sign('foo')
# s.unsign(string, max_age=5)
