from .views import GamesViewset
from rest_framework import routers


routers = routers.SimpleRouter()

routers.register('games',GamesViewset)
