import sys
sys.path.append("../")
from flask import Blueprint,request
from components.userManager import UserManager

user=Blueprint('user',__name__)


@user.route("/user")
def music():
    return '这里是一首音乐~'


@user.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@user.route('/user/register')
def register_new_user():
    email = request.args.get('email')
    username = email
    password = request.args.get('password')
    return UserManager.createNewUser(username,email,password)


@user.route('/user/login')
def loginUser():
    email = request.args.get('email')
    userName = email
    password = request.args.get('password')
    return UserManager.userLogin(userName,password)



