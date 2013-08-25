from django.core.urlresolvers import reverse
from django.utils import simplejson


class ExampleTestCase(TestCase):

    def test_get_json_200(self):
        response = self.client.get(reverse('get_json'))
        self.assertEqual(response.status_code, 200)
