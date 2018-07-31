from .blueprint import dashboard_blueprint
from .views import DashboardView


dashboard_blueprint.add_url_rule(
    '/admin/dashboard',
    view_func = DashboardView.as_view(
        'dashboard_page',
        'dashboard.html'
    )
)
