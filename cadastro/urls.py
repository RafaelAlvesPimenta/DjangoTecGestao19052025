from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastro/', views.cadastrar_empresa, name='cadastro_empresa'),
    path('cadastrouser', views.cadastrar_usuario, name='cadastro'),
    path('login/', views.Login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logou'),

     path('home/', views.Home, name='home'),
     path('planilhas/', views.Planilhas, name='planilhas'),
     path('produtos/', views.Produtos, name='produtos'),
     path('clientes/', views.Clientes, name='clientes'),
     path('vendas/', views.Vendas, name='vendas'),
     path('estoque/', views.Estoque, name='estoque'),

     path('redefinir-senha/<uuid:token>/', views.redefinir_senha, name='resetpassword_form'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)