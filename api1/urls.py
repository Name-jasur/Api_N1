from django.urls import path
from .views import AllCar, DetailCar,URLShortenerPage,getPersonInfo
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import GetAllViewset

router = routers.SimpleRouter()
router.register('get', GetAllViewset, basename='all_object')
urlpatterns = router.urls
urlpatterns += [
    path('', AllCar, name = 'allcar'),
    path('update/<int:pk>', DetailCar, name='update'),
    path('service/', URLShortenerPage , name= 'short_url'),
    path('person', getPersonInfo,name='person_info')
]


urlpatterns = format_suffix_patterns(urlpatterns)

