from django.urls import path, include
from rest_framework import routers
from .views import ChatRoomViewSet, ChatMessageViewSet

router = routers.DefaultRouter()
router.register('chatrooms/', ChatRoomViewSet)
router.register('chatmessages/', ChatMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
