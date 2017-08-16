
from django.conf.urls import url
from . import views

app_name = 'items'

urlpatterns = [
    url(r'^$', views.ItemView_template.as_view(), name = 'index'),
    # url(r'^items/', include('items.urls'))
]
