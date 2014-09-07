from django.contrib.auth.models import User

class Middleware(object):
    def process_request(self, request):
        request.user = User(id=1, is_superuser=True,
                            is_active=True, is_staff=True, username='user')
