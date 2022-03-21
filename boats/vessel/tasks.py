from os import path

from datetime import datetime
import openpyxl
from dateutil import parser
from celery import shared_task
from django.apps import apps
from django.conf import settings


@shared_task
def load_vessels_movements_file():
    Vessel = apps.get_model(app_label='vessel', model_name='Vessel')
    MovementHistory = apps.get_model(
        app_label='vessel',
        model_name='MovementHistory',
    )
    filename = datetime.today().strftime('%Y%m%d.xlsx')
    wb = openpyxl.load_workbook(path.join(settings.XLSX_DIR_PATH, filename))
    vessels_cache = {}

    for row in wb.active.iter_rows(min_row=2, values_only=True):
        code, rdate, rtime, latitude, longitude, name = row
        vessel = vessels_cache.get(code) or Vessel \
            .objects.filter(code=code).first()
        if not vessel:
            vessel = Vessel(code=code, name=name)
            vessel.save()
        vessels_cache[code] = vessel
        movement_datetime = parser.parse('{} {}'.format(rdate, rtime))
        MovementHistory(
            vessel=vessel,
            latitude=latitude,
            longitude=longitude,
            movement_datetime=movement_datetime,
        ).save()
