

# @app.route('/login.html', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = User.query.filter_by(email=email).first()
#         if user and user.check_password(password):
#             if user.role == 'Admin':
#                 login_user(user)
#                 flash('Wellcome Admin.', 'success')
#                 return render_template('admin.html')
#             elif user.role == 'Student':
#                 login_user(user)
#                 flash('Wellcome {user.first_name} {user.surname}.', 'success')
#                 return render_template("student.html")
#             else:
#                 login_user(user)
#                 flash('Wellcome Donor.', 'success')
#                 return render_template("donor.html")
#         else:
#             flash('Invalid username or password', 'danger')
#     return render_template('login.html')




#---------------------------------- Register -------------------------------------------

        # If email doesn't exist, continue with registration
        #password = request.form['password']
        #first_name = request.form['firstName']
        #surname = request.form['surname']
        #role = request.form['role']

        # Create a new user instance
        #new_user = User(email=email, password=password, first_name=first_name, surname=surname, role=role)