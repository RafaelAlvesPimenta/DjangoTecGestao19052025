from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario, Categorias_Produtos, Unidade_medida, Unidade_compra, Categorias_Materia_prima, MateriaPrima, Produto
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


def Estoque(request):
    categorias_lista = Categorias_Materia_prima.objects.all()

    if request.method == "POST":

        if "atualizar_estoque" in request.POST:
            produtos = Produto.objects.all()
            for produto in produtos:
                campo_estoque = f'estoque_{produto.id}'
                nova_quantidade = request.POST.get(campo_estoque)
                if nova_quantidade is not None and nova_quantidade.isdigit():
                    produto.estoque_atual = int(nova_quantidade)
                    produto.save()
            messages.success(request, "Estoque atualizado com sucesso.")
            return redirect('estoque')
        
        if "button_register_category" in request.POST:
            new_category = request.POST.get('new_category')
            if Categorias_Materia_prima.objects.filter(nome = new_category).exists():
                messages.error(request, "Essa categoria já existe")
            else:
                Categorias_Materia_prima.objects.create(nome = new_category)
                


        if 'form_newItem' in request.POST:
            nome_materia_prima = request.POST.get('nome_materia_prima')
            estoque_atual = request.POST.get('estoque_atual')
            quantidade_minima = request.POST.get('quantidade-min')
            quantidade_maxima = request.POST.get('quantidade-max')
            unidade_medida_id  = request.POST.get('unidade_medida')
            unidade_compra_id  = request.POST.get('unidade_compra')
            custo_unitario = request.POST.get('custo_unitario')
            categoria_id = request.POST.get('categoria')
            fornecedor_preferencial = request.POST.get('FornecedorPreferencial')
            imagem_material = request.FILES.get('imagem_material')

            print("categoria_id recebido:", categoria_id)
            try:
                categoria_obj = Categorias_Materia_prima.objects.get(id=categoria_id)
            except Categorias_Materia_prima.DoesNotExist:
                messages.error(request, "Categoria selecionada é inválida.")
                print("Categoria selecionada é inválida.")
                return redirect('estoque')
            try:
                unidade_medida_obj = Unidade_medida.objects.get(id=unidade_medida_id)
            except Unidade_medida.DoesNotExist:
                messages.error(request, "Unidade de medida inválida.")
                return redirect('estoque')
            try:
                custo_unitario_obj = Unidade_compra.objects.get(id=unidade_compra_id)
            except Unidade_compra.DoesNotExist:
                messages.error(request, "Unidade de medida inválida.")
                return redirect('estoque')

                
            if MateriaPrima.objects.filter(nome_materia_prima = nome_materia_prima).exists():
                messages.error(request, 'Já existe um item com esse nome')
            else:
                MateriaPrima.objects.create(
                    nome_materia_prima = nome_materia_prima,
                    unidade_medida = unidade_medida_obj,
                    unidade_compra = custo_unitario_obj,
                    custo_unitario = custo_unitario,
                    estoque_atual = estoque_atual,
                    estoque_maximo = quantidade_maxima,
                    estoque_minimo = quantidade_minima,
                    categoria=categoria_obj,
                    fornecedor_preferencial = fornecedor_preferencial,
                    img_material = imagem_material,
                    
                )
                return redirect('estoque')
            
        if "edit_material" in request.POST:
            material_id = request.POST.get('material_id')
            try:
                material = Produto.objects.get(id=material_id)
                material.nome_materia_prima = request.POST.get('nome_produto')
                unidade_medida_obj = Unidade_medida.objects.get(id=unidade_medida_id)
                material.unidade_medida = unidade_medida_obj
                material.estoque_atual = request.POST.get('quantidade')
                try:
                    material.estoque_minimo = int(request.POST.get('quantidade-min', 0))
                    material.estoque_maximo = int(request.POST.get('quantidade-max', 0))
                    material.custo_unitario = float(request.POST.get('custo_unitario', 0))
                except ValueError:
                    messages.error(request, "Valores numéricos inválidos")
                    return redirect('estoque')
                material.descricao = request.POST.get('descricao')
                
                categoria_id = request.POST.get('Categorias_Materia_prima')
                if categoria_id:
                    material.categoria = Categorias_Materia_prima.objects.get(id=categoria_id)
                
                if 'imagem-produto' in request.FILES:
                    material.img_produto = request.FILES['imagem-produto']
                
                material.save()
                messages.success(request, "Produto atualizado com sucesso!")
                print("Produto atualizado com sucesso!")
                return redirect('estoque')
                
            except Exception as e:
                messages.error(request, f"Erro ao atualizar produto: {str(e)}")
            return redirect('estoque')

    categoria_id = request.GET.get('categoria', 'all')

    materiais = MateriaPrima.objects.all()

    for material in materiais:
        estoque_atual = material.estoque_atual or 0
        estoque_maximo = material.estoque_maximo or 1  
        estoque_minimo = material.estoque_minimo or 1  
        material.tem_imagem = material.img_material and hasattr(material.img_material, 'url')
        
        if estoque_maximo == 0:
            porcentagem = 0
        else:
            porcentagem = (estoque_atual / estoque_maximo) * 100 if estoque_atual > 0 else 0
        
        material.barra = min(porcentagem, 100)
        material.em_falta = estoque_atual <= estoque_minimo    
        
    unidades_medidas = Unidade_medida.objects.all()
    unidades_compra = Unidade_compra.objects.all()
    return render(request, 'site/estoque.html', {'categorias': categorias_lista, 'unidadesmedidas': unidades_medidas, 'unidadescompra': unidades_compra,'materiais': materiais })







def Produtos(request): 
    categorias_lista = Categorias_Produtos.objects.all()
    if request.method == "POST":

        if "atualizar_estoque" in request.POST:
            produtos = Produto.objects.all()
            for produto in produtos:
                campo_estoque = f'estoque_{produto.id}'
                nova_quantidade = request.POST.get(campo_estoque)
                if nova_quantidade is not None and nova_quantidade.isdigit():
                    produto.estoque_atual = int(nova_quantidade)
                    produto.save()
            messages.success(request, "Estoque atualizado com sucesso.")
            return redirect('produtos')
        
        if "button_register_category" in request.POST:
            new_category = request.POST.get('new_category')
            if Categorias_Produtos.objects.filter(nome = new_category).exists():
                messages.error(request, "Essa categoria já existe")
            else:
                Categorias_Produtos.objects.create(nome = new_category)
                messages.success(request, "Categoria criada com sucesso!")
            

        if 'form_newItem' in request.POST:
            nome_produto = request.POST.get('nome_produto')
            quantidade = request.POST.get('quantidade')
            quantidade_minima = request.POST.get('quantidade-min')
            quantidade_maxima = request.POST.get('quantidade-max')
            categoria_id = request.POST.get('categoria')
            print("categoria_id recebido:", categoria_id)
            try:
                categoria_obj = Categorias_Produtos.objects.get(id=categoria_id)
            except Categorias_Produtos.DoesNotExist:
                messages.error(request, "Categoria selecionada é inválida.")
                print("Categoria selecionada é inválida.")
                return redirect('produtos')

            categoria_obj = Categorias_Produtos.objects.get(id=categoria_id)
            descricao = request.POST.get('descricao')
            imagem_produto = request.FILES.get('imagem-produto')
            valor = request.POST.get('valor')
            codigo_barras = request.POST.get('codigo_barras')
            custo_producao = request.POST.get('custo_producao')

                
            if Produto.objects.filter(nome_produto = nome_produto).exists():
                messages.error(request, 'Já existe um item com esse nome')
            else:
                Produto.objects.create(
                    nome_produto = nome_produto,
                    descricao = descricao,
                    codigo_barras = codigo_barras,
                    custo_producao = custo_producao,
                    preco = valor,
                    estoque_atual = quantidade,
                    estoque_maximo = quantidade_maxima,
                    estoque_minimo = quantidade_minima,
                    categoria=categoria_obj,
                    img_produto = imagem_produto,
                        
                )
                return redirect('produtos')
            
        if "form_editar_produto" in request.POST:
            produto_id = request.POST.get('produto_id')
            try:
                produto = Produto.objects.get(id=produto_id)
                produto.nome_produto = request.POST.get('nome_produto')
                produto.estoque_atual = request.POST.get('quantidade')
                produto.estoque_minimo = request.POST.get('quantidade-min')
                produto.estoque_maximo = request.POST.get('quantidade-max')
                produto.descricao = request.POST.get('descricao')
                produto.custo_producao = request.POST.get('custo_producao')
                produto.preco = request.POST.get('valor')
                
                categoria_id = request.POST.get('categoria')
                if categoria_id:
                    produto.categoria = Categorias_Produtos.objects.get(id=categoria_id)
                
                if 'imagem-produto' in request.FILES:
                    produto.img_produto = request.FILES['imagem-produto']
                
                produto.save()
                messages.success(request, "Produto atualizado com sucesso!")
                print("Produto atualizado com sucesso!")
                return redirect('produtos')
                
            except Exception as e:
                messages.error(request, f"Erro ao atualizar produto: {str(e)}")
                return redirect('produtos')
            
    categoria_id = request.GET.get('categoria', 'all')
    print("categoria_id enviado:", categoria_id)
    if categoria_id == 'all':
        produtos = Produto.objects.all()        
    else:
        try:
            categoria_obj = Categorias_Produtos.objects.get(id=categoria_id)
            produtos = Produto.objects.filter(categoria=categoria_obj)
        except Categorias_Produtos.DoesNotExist:
            produtos = Produto.objects.none()
            messages.error(request, "Categoria não encontrada.")

    for produto in produtos:
        estoque_atual = produto.estoque_atual or 0
        estoque_maximo = produto.estoque_maximo or 1  
        estoque_minimo = produto.estoque_minimo or 1  
        
        if estoque_maximo == 0:
            porcentagem = 0
        else:
            porcentagem = (estoque_atual / estoque_maximo) * 100 if estoque_atual > 0 else 0
        
        produto.barra = min(porcentagem, 100)
        produto.em_falta = estoque_atual <= estoque_minimo
    return render(request, 'site/produtos.html', {'produtos': produtos, 'categorias': categorias_lista })

def Vendas(request):
    return render(request, 'site/Vendas.html')