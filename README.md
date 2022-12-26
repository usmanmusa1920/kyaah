
Kyaah abstract away SMTP mail operations

Simplify your email message with `kyaah`


    #    #   #   #    ##      ##    #    #
    #   #     # #    #  #    #  #   #    #
    ####       #    #    #  #    #  ######
    #  #       #    ######  ######  #    #
    #   #      #    #    #  #    #  #    #
    #    #     #    #    #  #    #  #    #
# How to use the library
First we recommend creating a virtual environment `python3 -m venv venv` and then activate it `source venv/bin/activate`

Once that finish now install the library using `pip install dipense` and wait for the installation basically the library was uploaded using `sdist` (Source Distribution)

After that create a new file let call it `test.py` in the file put the below code

```python
import kyaah
            
sender = "my_email@gmail.com"
receiver = ["receiver_1@gmail.com", "receiver_2@gmail.com"]
passwd = "*********"

server = "gmail"
subj = f"Hellow world!"
body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt."

kyaah.sendMail(
        from_usr=sender, to_usr=receiver, svr=server, subject=subj, body=body, mail_passwd=passwd)
```

save the file and navigate to where the file is located in terminal and your are ready to go

To find information about a domain name run the file like:

`python3 test.py`


## Github and docker repository:

- https://github.com/usmanmusa1920/kyaah


Pull requests are welcome

![DiPense at a glance](https://raw.githubusercontent.com/usmanmusa1920/dipense/master/screen-shot.png)
