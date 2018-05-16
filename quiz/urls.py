from django.urls import include, path

from .views import *

urlpatterns = [
    path("", nome_view, name="nome"),
    path("pergunta1/<int:pk>/", pergunta1_view, name="pergunta1"),
    path("pergunta2/<int:pk>/", pergunta2_view, name="pergunta2"),
    path("pergunta3/<int:pk>/", pergunta3_view, name="pergunta3"),
    path("pergunta4/<int:pk>/", pergunta4_view, name="pergunta4"),
    path("pergunta5/<int:pk>/", pergunta5_view, name="pergunta5"),
    path("pergunta6/<int:pk>/", pergunta6_view, name="pergunta6"),
    path("pergunta7/<int:pk>/", pergunta7_view, name="pergunta7"),
    path("pergunta8/<int:pk>/", pergunta8_view, name="pergunta8"),
    path("pergunta9/<int:pk>/", pergunta9_view, name="pergunta9"),
    path("pergunta10/<int:pk>/", pergunta10_view, name="pergunta10"),
    path("resultado", pergunta10_view, name="resultado"),


]