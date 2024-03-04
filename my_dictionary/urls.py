from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.indexpage, name="index"),
    path("home", views.indexpage, name="index"),
    path("home/", views.indexpage, name="index"),
    path("add_word", views.addwordpage, name="add_word"),
    path("add_word/", views.addwordpage, name="add_word"),
    path("words_list", views.wordslistpage, name="words_list"),
    path("words_list/", views.wordslistpage, name="words_list")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)