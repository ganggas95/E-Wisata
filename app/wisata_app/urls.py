from .blueprint import wisata_blueprint
from .views import (
    ListWisataView,
    AddDataView,
    EditDataView
)


wisata_blueprint.add_url_rule(
    '/admin/wisata/object/list',
    view_func=ListWisataView.as_view(
        'list_wisata',
        'wisata_page/list_wisata.html'
    )
)

wisata_blueprint.add_url_rule(
    '/admin/wisata/object/add',
    view_func=AddDataView.as_view(
        'add_wisata',
        'wisata_page/add_wisata.html'
    ),
    methods=['POST', 'GET']
)

wisata_blueprint.add_url_rule(
    '/admin/wisata/object/<int:wisata_id>/edit',
    view_func=EditDataView.as_view(
        'edit_wisata',
        'wisata_page/edit_wisata.html'
    ),
    methods=['POST', 'GET']
)
