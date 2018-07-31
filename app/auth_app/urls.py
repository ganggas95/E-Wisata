from .blueprint import auth_blueprint
from .views import LoginView

auth_blueprint.add_url_rule(
    '/authenticate',
    view_func=LoginView.as_view(
        'login_page',
        'login_page.html'
    ),
    methods=['GET', 'POST']
)