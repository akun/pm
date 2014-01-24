
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.http import require_GET

@require_GET
def get_json(request):

    return HttpResponse(simplejson.dumps({
        'name': u'大卷的耶稣', 'age': 13
    }), mimetype='application/json')
