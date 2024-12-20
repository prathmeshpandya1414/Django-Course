from django.utils.text import slugify

'''
This function generates a unique slug for a given title and reuturn str
'''

import uuid
def generate_slug(title:str) -> str:
    from .models import Receipe
    title = slugify(title)

    while Receipe.objects.filter(slug=title).exists():
        title = f'{slugify(title)}-{str(uuid.uuid4())[:4]}'
    return title