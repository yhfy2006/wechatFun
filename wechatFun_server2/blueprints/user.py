from flask import Blueprint


user=Blueprint('user',__name__)


@user.route("/user")
def music():
    return '这里是一首音乐~'



@user.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username