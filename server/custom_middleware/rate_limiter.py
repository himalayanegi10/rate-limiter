import redis
from django.http import HttpResponse


class CustomRateLimiterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rc = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def __call__(self, request):
        too_many_requests = False
        counter = self.rc.get("counter")
        if counter is None:
            self.rc.set("counter", 0, ex=15)
        else:
            counter = self.rc.incr("counter")
            if counter % 10 == 0:
                self.rc.set("counter", 0)
                too_many_requests = True
        if too_many_requests:
            return HttpResponse(status=429, content="<h1>429 Too Many Requests</h1>")
        response = self.get_response(request)
        return response
