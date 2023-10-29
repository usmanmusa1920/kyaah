# -*- coding: utf-8 -*-
"""
Kyaah.server
~~~~~~~~~~~~

It simplify mail servers stuffs for ease!
"""

server = {
    'gmail': {
        'server': [
            'smtp.gmail.com',
            'pop.googlemail.com',
            'imap.gmail.com'
        ],
        'port': [
            465, # smtp server (for SSL) it listen on port 25 if not SSL
            587, # smtp server (for TLS)
            995, # pop server, (it listen on port 110, but use 995 for SSL)
            993, # imap server, (it listen on port 143, but use 993 for SSL)
        ]
    },
    
    'local': {
        'server': ['localhost'],
        'port': [
            1025, # smtp server
        ]
    },
    
    'yahoo': {
        'server': [
            'smtp.mail.yahoo.com',
            'pop.mail.yahoo.com',
            'imap.mail.yahoo.com'
        ],
        'port': [
            465, # smtp server it listen on port 25 if not SSL
            587, # smtp server
            995, # pop server, (it listen on port 110, but use 995 for SSL)
            993, # imap server, (it listen on port 143, but use 993 for SSL)
        ]
    },
    
    'icloud': {
        'server': [
            'smtp.mail.me.com',
            # 'pop.mail.yahoo.com',
            'imap.mail.me.com'
        ],
        'port': [
            465, # SSL. If you see an error message when using SSL, try using TLS or STARTTLS instead.
            587, # smtp server
            # 995, # pop server, (it listen on port 110, but use 995 for SSL)
            # iCloud does not support POP configurations
            993, # imap server, (it listen on port 143, but use 993 for SSL)
        ]
    },
}


class Serve:
    """
    This class handle SMTP server suffs
    """

    def mail(mail):
        """It return server related credentials"""
        return server[mail]
