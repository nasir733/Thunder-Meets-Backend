from django.urls import path, include
from.views import Meeting
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'', Meeting)

urlpatterns = [
    # path('', Meeting.as_view(), name='meeting'),
]
urlpatterns += router.urls