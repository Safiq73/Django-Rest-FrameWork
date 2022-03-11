from rest_framework.throttling import UserRateThrottle

class Throttle1(UserRateThrottle):
    scope='throttle1'