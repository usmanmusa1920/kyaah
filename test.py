from kyaah import Vault
from kyaah import BaseMail


subj = f"Hellow world! from kyaah"
body = "Lorem ipsum dolor sit amet consectetur adipisicing elit, rerum voluptate ipsum volupt."

base = BaseMail(
      from_usr = "my_email@gmail.com",
      mail_passwd = "<your_password_or_app_password>",
      to_usr = ["userOne@mail.com", "userTwo@mail.com"],
      subject = subj,
      body = body,
      server = "smtp.gmail.com",
      )
base.send_mail(port=465)
