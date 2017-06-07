from django.core.urlresolvers import reverse
def get_absolute_url(self):
    path = reverse('detail', kwargs={'id': self})
    print("http:127.0.0.1:8000%s" % path)
get_absolute_url(1)
