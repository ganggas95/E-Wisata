from flask import Blueprint


wisata_blueprint = Blueprint(
    'wisata_blueprint',
    __name__,
    template_folder='templates'
)
