from flask import Flask, request, render_template, redirect
from cgi import escape
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

def has_space(text):
    space = " "
    for char in text:
        if char == space:
            return True
        else:
            return False

def is_out_of_range(text):
    if len(text) < 3 or len(text) > 20:
        return True
    else:
        return False


# @app.route("/", methods=["POST"])
# def sign_up():
#     #We got the info from the form submitted by the user
#     username = request.form['username']
#     password = request.form['password']
#     verify = request.form['verify']
#     email = request.form['email']

#     username = escape(username)
#     password = escape(password)
#     verify = escape(verify)
#     email = escape(email)

#     #Storage for our error messages
#     username_error = ""
#     password_error = ""
#     verify_error = ""
#     email_error = ""

#     if username == "" or " " in username or len(username) < 3 or len(username) > 20:
#         username_error = "Invalid username"
#         username = ""

#     if password == "" or " " in password or len(password) < 3 or len(password) > 20:
#         password_error = "Invalid password"

#     if verify == "" or verify != password:
#         verify_error = "Invalid verification"

#     if email != "":
#         if "@" not in email or "." not in email or " " in email or len(email) < 3 or len(email) > 20:
#                 email_error = "Invalid email"

#     if email_error == "" and username_error == "" and verify_error == "" and password_error == "":
#         return render_template("welcome.html", username = username)
#     else:
#         return render_template("index.html", username_error = username_error
#                                            , password_error = password_error
#                                            , verify_error = verify_error
#                                            , email_error = email_error
#                                            , username = username
#                                            , email = email)
                                     
# @app.route("/")
# def index():
#     return render_template("index.html")

#app.run()

@app.route("/")
def index():
    template = jinja_env.get_template('user-signup_index.html')
    return template.render(error_username='', 
                           error_password='',
                           error_verify='',
                           error_email='',
                           username='',
                           email='')

# return form.format(error_username='', 
#                            error_password='',
#                            error_verify='',
#                            error_email='',
#                            username='',
#                            email=''))

               

@app.route("/errors")
def errors():
    
    username = request.args.get('username')
    password = request.args.get('password')
    verify = request.args.get('verify')
    email = request.args.get('email')

    error_username = ''
    error_password = ''
    error_verify = ''
    error_email = ''

    if has_space(username) or is_out_of_range(username):
        error_username = "That's not a valid username"
        #username = ''
    else:
        if username == '':
            error_username = "That's not a valid username"
        
    if has_space(password) or is_out_of_range(password) or password == '':
        error_password = "That's not a valid password"
        error_verify = "Passwords don't match"
        #password = ''
        #verify = ''
    else:
        if password != verify:
            error_verify = "Passwords don't match"
            #password = ''
            #verify = ''

    if email !='':
        if has_space(email) or is_out_of_range(email):
            error_email = "That's not a valid email"
            #email = ''
        else:
            if '@' not in email or '.' not in email or email.count('@') > 1 or email.count('.') > 1:
                error_email = "That's not a valid email"
                #email = ''

    if not error_username and not error_password and not error_verify and not error_email:
        return redirect('/Welcome?username={0}'.format(username))
    else:
        template = jinja_env.get_template('user-signup_index.html')
        # return form.format(error_username=error_username,
        return template.render(error_username=error_username, 
                           error_password=error_password,
                           error_verify=error_verify,
                           error_email=error_email,
                           username=username,
                           email=email)

@app.route("/Welcome")
def welcome():
    username = request.args.get('username')
    # username = form.format(username=username)
    
    # username = request.args.get('username')
    # password = request.args.get('password')
    # verify = request.args.get('verify')
    # email = request.args.get('email')
        
    # error_username = ''
    # error_password = ''
    # error_verify = ''
    # error_email = ''

    # form.format(
    # #     # error_username=error_username, 
    #                        error_password=error_password,
    #                        error_verify=error_verify,
    #                        error_email=error_email,
    #                        username=username,
    #                        email=email)
    template = jinja_env.get_template('user-signup_Welcome.html')
    return template.render(template_username=username)
                

app.run()