from flask import (
    render_template,
    redirect,
    url_for,
    request,
    flash
)
from flask.views import View
from flask_login import (
    login_required,
    login_user
)
from app.user_app.models import (
    User
)
from .models import LoginForm


class LoginView(View):
    def __init__(self, template_name):
        self.template_name = template_name
    
    def dispatch_request(self):
        form = LoginForm(request.form)
        if request.method == 'GET':
            return render_template(
                self.template_name,
                form=form
            )
        
        if form.validate_on_submit():
            print("AHA")
            user = User.get_by_username(form.username.data)
            print(user)
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Login Successfully!', category='success')
                return redirect(
                    url_for('dashboard_blueprint.dashboard_page')
                )
            flash('Username and password invalid!', category='error')
            return redirect(
                url_for('auth_blueprint.login_page')
            )
                