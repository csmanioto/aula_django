# app/context_processors.py
import os

def environment_variables(request):
    return {
        'HEADER_TITLE': os.getenv('HEADER_TITLE', 'Default Title'),
    }
