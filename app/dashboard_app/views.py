from flask import (
    render_template,
    views
)

from flask_login import login_required


class DashboardView(views.View):
    def __init__(self, template_name):
        self.template_name = template_name

    @login_required
    def dispatch_request(self):
        return render_template(self.template_name)
