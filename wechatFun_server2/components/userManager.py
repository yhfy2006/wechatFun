import leancloud
from leancloud.errors import LeanCloudError


class UserManager(object):

    @classmethod
    def createNewUser(cls,userName,email,password):
        user = leancloud.User()
        user.set_username(userName)
        user.set_password(password)
        user.set_email(email)
        try:
            user.sign_up()
            return "注册成功"
        except LeanCloudError as err:
            return err.error


    @classmethod
    def userLogin(cls,userName,password):
        user = leancloud.User()
        try:
            user.login(userName, password)
            return user.session_token
        except LeanCloudError as err:
            return err.error




