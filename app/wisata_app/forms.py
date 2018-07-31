from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    validators,
    TextAreaField,
    FloatField
)


class SearchForm(FlaskForm):
    search = StringField(
        "Cari dengan keyword di sini....!",
        render_kw={
            "class": 'form-control',
            "placeholder": "Cari dengan keyword di sini....!"
        }
    )


class WisataForm(FlaskForm):
    name = StringField(
        "Nama object",
        validators=[validators.DataRequired()],
        render_kw={
            "class": 'form-control',
            "placeholder": "Nama object wisata di sini....!"
        }
    )
    desc = TextAreaField(
        "Dekripsi object",
        render_kw={
            "class": 'form-control',
            "placeholder": "Deskripsi object wisata di sini....!"
        }
    )


class AdministratorForm(FlaskForm):
    admin_name = StringField(
        "Nama Ketua Pengurus",
        render_kw={
            "class": "form-control",
            "placeholder": "Nama pengurus wisata..."
        }
    )
    first_name = StringField(
        "Nama Awal Pengurus",
        render_kw={
            "class": "form-control",
            "placeholder": "Nama awal ketua pengurus wisata..."
        }
    )
    last_name = StringField(
        "Nama akhir pengurus",
        render_kw={
            "class": "form-control",
            "placeholder": "Nama akhir ketua pengurus wisata..."
        }
    )
    address_admin = TextAreaField(
        "Alamat/Sekretariat",
        render_kw={
            "id": "address_admin",
            "class": 'form-control',
            "placeholder": "Alamat/Sekretariat pengurus wisata....!"
        }
    )
    contact = StringField(
        "Hp/Email/WA pengurus",
        render_kw={
            "class": "form-control",
            "placeholder": "Hp/Email/WA pengurus wisata..."
        }
    )


class LocationForm(FlaskForm):
    lat = FloatField(
        "Latitude Lokasi",
        validators=[validators.DataRequired()],
        render_kw={
            "type": 'number',
            'step': 'any',
            "class": 'form-control',
            "placeholder": "Latitude Lokasi wisata....!"
        }
    )
    lng = FloatField(
        "Longitued Lokasi",
        validators=[validators.DataRequired()],
        render_kw={
            "type": 'number',
            'step': 'any',
            "class": 'form-control',
            "placeholder": "Longitued Lokasi wisata....!"
        }
    )
    village = StringField(
        "Desa",
        render_kw={
            "class": "form-control",
            "placeholder": "Desa lokasi wisata..."
        }
    )
    district = StringField(
        "Kecamatan",
        render_kw={
            "class": "form-control",
            "placeholder": "Desa lokasi wisata..."
        }
    )
    address_loc = TextAreaField(
        "Alamat Lengkap",
        render_kw={
            "class": "form-control",
            "placeholder": "Alamat lengkap lokasi wisata..."
        }
    )
