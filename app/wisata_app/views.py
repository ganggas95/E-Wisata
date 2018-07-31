from flask import (
    render_template,
    views,
    redirect,
    url_for,
    request
)
from flask_login import login_required
from .models import (
    Wisata,
    Location,
    Administrator
)
from .forms import (
    SearchForm,
    WisataForm,
    LocationForm,
    AdministratorForm
)


class ListWisataView(views.View):
    def __init__(self, template_name):
        self.template_name = template_name

    @login_required
    def dispatch_request(self):
        search = request.args.get(
            'search', 
            default='', 
            type=str
        )
        form_search = SearchForm(request.form)
        form_search.search.data = search
        data_wisata = Wisata.get_all_data(
            form_search.search.data,
            request.args.get('page', default=1, type=int),
            15
        )
        next_page = data_wisata.next_num if data_wisata.has_next else None
        prev_page = data_wisata.prev_num if data_wisata.has_prev else None
        pages = data_wisata.iter_pages(
            left_edge=3, 
            right_edge=3, 
            left_current=3, 
            right_current=3
        )
        return render_template(
            self.template_name,
            next_page=next_page,
            prev_page=prev_page,
            data_wisata=data_wisata.items,
            pages=pages,
            form_search = form_search
        )


class AddDataView(views.View):
    def __init__(self, template_name):
        self.template_name = template_name

    @login_required
    def dispatch_request(self):
        form_wisata = WisataForm(request.form)
        form_location = LocationForm(request.form)
        form_admin = AdministratorForm(request.form)
        if request.method == 'GET':
            return render_template(
                self.template_name,
                form_wisata=form_wisata,
                form_location=form_location,
                form_admin=form_admin
            )
        if form_location.validate() and form_wisata.validate():
            wisata = Wisata()
            wisata.wisata_form(form_wisata)
            location = Location()
            location.location_form(form_location)
            wisata.location = location
            admin = Administrator()
            admin.admin_form(form_admin)
            wisata.admin = admin
            wisata.save()
            return redirect(
                url_for('wisata_blueprint.list_wisata')
            )


class EditDataView(views.View):
    def __init__(self, template_name):
        self.template_name = template_name

    @login_required
    def dispatch_request(self, wisata_id):
        wisata = Wisata.get_by_id(wisata_id)
        form_wisata = WisataForm(request.form)
        form_location = LocationForm(request.form)
        form_admin = AdministratorForm(request.form)
        if request.method == 'GET':
            return render_template(
                self.template_name,
                form_wisata=form_wisata,
                form_location=form_location,
                form_admin=form_admin
            )
        if form_location.validate() and form_wisata.validate():
            
            wisata.wisata_form(form_wisata)
            location = wisata.location
            location.location_form(form_location)
            wisata.location = location
            admin = wisata.admin
            admin.admin_form(form_admin)
            wisata.admin = admin
            wisata.save()
            return redirect(
                url_for('wisata_blueprint.list_wisata')
            )
