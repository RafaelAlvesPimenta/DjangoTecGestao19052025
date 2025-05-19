from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario, Item, categorias
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import PasswordResetToken
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm


     


#start cadastro usuários
def cadastrar_usuario(request):
    if request.method == 'POST':
            nome = request.POST.get('nome')
            senha = request.POST.get('senha')
            cpf_cnpj = request.POST.get('cpf_cnpj')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')

            if Usuario.objects.filter(email=email).exists():
                messages.error(request, 'Este e-mail já está cadastrado.')
                return redirect('cadastro')

            if Usuario.objects.filter(cpf_cnpj=cpf_cnpj).exists():
                messages.error(request, 'Este CPF/CNPJ já está cadastrado.')
                return redirect('cadastro')
            
            if Usuario.objects.filter(nome=nome).exists():
                messages.error(request, 'Este Nome já está cadastrado.')
                return redirect('cadastro')
            
            else:
                Usuario.objects.create(
                nome=nome,
                senha=make_password(senha),
                cpf_cnpj=cpf_cnpj,
                email=email,
                telefone=telefone
                )
                messages.success(request, 'Usuário cadastrado com sucesso!')
                return render(request, 'site/home.html')
            
    return render(request, 'cadastro/cadastrar.html')
#end cadastro usuários

#start login
def Login_usuario(request):
    if request.method == "POST":
        if 'form_login' in request.POST:
            nome = request.POST.get('nome')
            senha = request.POST.get('senha')
            cpf_cnpj = request.POST.get('cpf_cnpj')
            
            try:
                usuario = Usuario.objects.get(nome=nome)
                if check_password(senha, usuario.senha):  
                    
                    request.session['usuario_id'] = usuario.id
                    return redirect('home')
                else:
                    messages.error(request, "Senha ou nome incorretos")
                    return redirect('login')

            except Usuario.DoesNotExist:
                
                messages.error(request, "Usuário não encontrado")
        elif 'form_resetpassword' in request.POST:
            email = request.POST.get('email')
            usuario = get_object_or_404(Usuario, email=email)
            token = PasswordResetToken.objects.create(usuario=usuario)
            
            subject = "Redefinição de senha"
            html_content = render_to_string("resetsenha/resetpassword_form.html", {
                'usuario': usuario,
                'reset_link': request.build_absolute_uri(f"/redefinir-senha/{token.token}/")
            })
            text_content = strip_tags(html_content)

            email_msg = EmailMultiAlternatives(subject, text_content, to=[usuario.email])
            email_msg.attach_alternative(html_content, "text/html")
            email_msg.send()

            
    return render(request, 'cadastro/login.html')

#end login

#start reset password

def redefinir_senha(request, token):
    try:
        print("ioihi")
        reset_token = PasswordResetToken.objects.get(token=token)
    except PasswordResetToken.DoesNotExist:
        return render(request, "resetsenha/erro_token.html", {"mensagem": "Token inválido ou expirado."})
    if not reset_token.is_valid():
         return render(request, "resetsenha/erro_token.html", {"mensagem": "Token expirado. Solicite um novo e-mail."})
    if request.method == "POST":
        newsenha1 = request.POST.get('password1')
        newsenha2 = request.POST.get('password2')
        if newsenha1 != newsenha2:
            messages.error(request, "As senhas não coincidem")
            return render(request, 'resetsenha/resetPassword.html', {'token': token})

        usuario = reset_token.usuario
        usuario.senha = make_password(newsenha1)
        usuario.save()
        print('deu certo')
        reset_token.delete()
        return redirect("login")
    return render(request, 'resetsenha/resetPassword.html', {'token': token})
#end reset password

def Home(request):
    if 'usuario_id' not in request.session:
        print('volta')
        return redirect('login')
        
    return render(request, 'site/home.html')
    
def logout_usuario(request):
    request.session.flush()  
    return redirect('login')

def Planilhas(request):
    return render(request, 'site/planilhas.html')
def Produtos(request):
     
    return render(request, 'site/Produtos.html')
def Vendas(request):
    return render(request, 'site/Vendas.html')

def Estoque(request):
    categorias_lista = categorias.objects.all()
    if request.method == "POST":
        
            nome = request.POST.get('nome')
            quantidade = request.POST.get('quantidade')
            quantidade_maxima = request.POST.get('quantidade_maxima')
            quantidade_minima = request.POST.get('quantidade_minima')
            categoria_id = request.POST.get('categoria')
            categoria_obj = categorias.objects.get(id=categoria_id)
            imagem_produto = request.FILES.get('imagem-produto')
            valor = request.POST.get('valor')
            
            if Item.objects.filter(nome = nome).exists():
                messages.error(request, 'Já existe um item com esse nome')

            else:
                Item.objects.create(
                    nome = nome,
                    quantidade = quantidade,
                    quantidade_minima = quantidade_minima,
                    quantidade_maxima = quantidade_maxima,
                    categoria=categoria_obj,
                    img_produto = imagem_produto,
                    preco = valor,
                )
                return redirect('estoque')
    categoria = request.GET.get('categoria', 'all')
    if categoria == 'all':
        produtos = Item.objects.all()
    else:
        produtos = Item.objects.filter(categoria=categoria)

    for produto in produtos:
        try:
            porcentagem = (produto.quantidade / produto.quantidade_maxima) * 100 if produto.quantidade_maxima > 0 else 0
        except ZeroDivisionError:
            porcentagem = 0
        produto.barra = min(porcentagem, 100)
        produto.em_falta = produto.quantidade == 0
    return render(request, 'site/Estoque.html', {'produtos': produtos, 'categorias': categorias_lista })

def newPassword(request):
    return render(request, 'resetsenha/resetPassword.html')