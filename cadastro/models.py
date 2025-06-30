from django.db import models
import uuid
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
=======
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now


<<<<<<< HEAD
class Empresa(models.Model):
    empresa_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=20, unique=True)
    CEP = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(unique=True)
    email = models.EmailField(max_length=150, unique=True)
    telefone = models.CharField(max_length=20, unique=True)

class Usuario(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    cpf = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20, unique=True)
    cargo = models.CharField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    REQUIRED_FIELDS = ['cpf', 'first_name', 'last_name', 'email', 'telefone', 'empresa']

    def __str__(self):
        return self.username
=======
class Usuario(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20, unique=True)

    def __str__   (self):
        return self.nome
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891

class PasswordResetToken(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() < self.created_at + timedelta(minutes=30)

# class Estoque(models.Model):
#     nome = models.CharField(max_length=150, unique=True)
#     categoria = models.CharField(max_length=150, unique=True)
#     quantidade = models.IntegerField(validators=[MinValueValidator(0)])
#     quantidadeMinima = models.IntegerField()
    # preco = models.DecimalField(
    # max_digits=10,
    # decimal_places=2,
    # validators=[MinValueValidator(1)]
    # )
    # descricao = models.CharField(max_length=250)
    # imagem = models.ImageField(upload_to='imagens_user/')
    
#     def clean(self):
#         super().clean()
#         if self.quantidade < self.quantidadeMinima:
#             raise ValidationError({
#                 'quantidade': 'A quantidade atual não pode ser menor que a quantidade mínima.'
#             })

class Categorias_Produtos(models.Model):
    nome = models.CharField(max_length=50, unique=True)
<<<<<<< HEAD
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
=======
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891
    
    class Meta:
        db_table = "Categorias_Produtos"

    def __str__  (self):
        return self.nome
    
class Categorias_Materia_prima(models.Model):
<<<<<<< HEAD
    nome = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
=======
    nome = models.CharField(max_length=50, unique=True)
    
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891
    class Meta:
        db_table = "Categorias_Materia_prima"

    def __str__   (self):
        return self.nome

class Unidade_medida(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    sigla = models.CharField(max_length=150, unique=True)
<<<<<<< HEAD
    tipo = models.CharField(max_length=150)
=======
    tipo = models.CharField(max_length=150, unique=True)
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891

    class Meta:
        db_table = "Unidade_medida"

    def __str__   (self):
        return self.nome
class Unidade_compra(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    sigla = models.CharField(max_length=150, unique=True)
<<<<<<< HEAD
    tipo = models.CharField(max_length=150)
=======
    tipo = models.CharField(max_length=150, unique=True)
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891

    class Meta:
        db_table = "Unidade_compra"

    def __str__   (self):
        return self.nome


class MateriaPrima(models.Model):
    id = models.AutoField(primary_key=True)
    nome_materia_prima = models.CharField(max_length=100, unique=True)
    unidade_medida = models.ForeignKey(
        Unidade_medida,
        db_column='nome',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None,

    )
    unidade_compra = models.ForeignKey(
        Unidade_compra,
        db_column='unidade_compra',
        on_delete=models.PROTECT,
        default=None,

    )
    metragem_por_unidade = models.CharField(max_length=50, default="")
    estoque_atual = models.IntegerField(validators=[MinValueValidator(0)])
    estoque_maximo = models.IntegerField( default=100)
    estoque_minimo = models.IntegerField( default=1 )
    custo_unitario = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(1)]
    )
    # custo_total = models.DecimalField(
    # max_digits=10,
    # decimal_places=2,
    # validators=[MinValueValidator(1)]
    # )
    data_ultima_atualizacao = models.DateField(auto_now=True)
    fornecedor_preferencial = models.CharField(max_length=100)
    img_material = models.ImageField(upload_to='imagens_produtos/imagens_estoque', default="")
    categoria = models.ForeignKey(
        Categorias_Materia_prima,     
        db_column='categoria',
        on_delete=models.PROTECT,
    )
<<<<<<< HEAD
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
=======
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891

    def __str__   (self):
        return self.nome_materia_prima

class Produto(models.Model):
    id = models.AutoField( primary_key=True )
    nome_produto = models.CharField(max_length=255, unique=True)
    descricao = models.TextField()
    codigo_barras = models.CharField(max_length=50, unique=True, null=True, blank=True)
    custo_producao = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(1)],
    default=000
    )
    preco = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(1)]
    )
    estoque_atual = models.IntegerField()
    estoque_maximo = models.IntegerField( default=100)
    estoque_minimo = models.IntegerField( default=1 )
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    img_produto = models.ImageField(upload_to='media/imagens_produtos/imagens_estoque', blank=True, null=True, default=True)
    categoria = models.ForeignKey(
        Categorias_Produtos,
        db_column='categoria',
        on_delete=models.PROTECT,
        default='Sem Categoria',
    )
<<<<<<< HEAD
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
=======
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891

    class Meta:
        db_table = "Produto"

    def __str__   (self):
        return self.nome_produto
    



# class MateriaisUsados(models.Model):
#     id = models.AutoField( primary_key=True)
#     produto = models.ForeignKey(
#         Produto,
#         to_field='id',
#         db_column='produto',
#         on_delete=models.PROTECT,
#     )
#     materia_prima = models.ForeignKey(
#         MateriaPrima,
#         to_field='id',
#         db_column='materia_prima',
#         on_delete=models.PROTECT)
#     quantidade_necessaria = models.IntegerField(validators=[MinValueValidator(1)])

#     class Meta:
#         db_table = "materiais_usados"
#         unique_together = ('produto', 'materia_prima') 

#     def __str__   (self):
#         return f'{self.quantidade_necessaria} de {self.materia_prima} para {self.produto}' 


class Producao(models.Model):
    nome = models.CharField(max_length=255)

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='producoes'
    )

    materiais = models.ForeignKey(
        MateriaPrima,
        db_column='materiais_id',
        on_delete=models.PROTECT
    )

    descricao = models.TextField()
    moldes = models.TextField(blank=True, null=True)

    # categoria = models.ForeignKey(
    #     categorias,
    #     to_field='nome',
    #     on_delete=models.PROTECT
    # )

    observacoes = models.TextField(blank=True, null=True)
    tamanho = models.CharField(max_length=50)
<<<<<<< HEAD
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
=======
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891

    class Meta:
        db_table = 'Producao'

class Clientes(models.Model):
    nome = models.CharField(max_length=255, unique=True)
<<<<<<< HEAD
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    CPF = models.CharField(max_length=14, unique=True)  # Formato típico: 000.000.000-00
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
=======
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    CPF = models.CharField(max_length=14)  # Formato típico: 000.000.000-00
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891

    class Meta:
        db_table = "Clientes"

    def __str__   (self):
        return self.nome

class Vendas(models.Model):
<<<<<<< HEAD
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    cliente = models.ForeignKey(
        Clientes,  
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        db_index=True
    )
    cliente_nao_cadastrado = models.CharField(
        max_length=50,
        null=True, 
        blank=True,
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    data_venda = models.DateTimeField(auto_now_add=True, db_index=True)  # equivale ao DEFAULT CURRENT_TIMESTAMP
=======
    valor = models.FloatField(db_column='Valor')
    comprador = models.ForeignKey(
        Clientes,  # nome do modelo relacionado
        on_delete=models.PROTECT,
        db_column='comprador_id',
        related_name='vendas_por_id'
    )
    comprador_nome = models.ForeignKey(
        Clientes,
        to_field='nome',
        on_delete=models.PROTECT,
        db_column='comprador_nome',
        related_name='vendas_por_nome'
    )
    data = models.DateTimeField(auto_now_add=True)  # equivale ao DEFAULT CURRENT_TIMESTAMP
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891

    class Meta:
        db_table = "Vendas"

    def __str__   (self):
<<<<<<< HEAD
        return f"Venda {self.id} - Comprador: {self.cliente} - Valor: {self.valor_total}"
    
class ProdutoVenda(models.Model):
    venda = models.ForeignKey(Vendas, on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, 
        on_delete=models.SET_NULL,
        null=True
        )
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2)
=======
        return f"Venda {self.id} - Comprador: {self.comprador_nome} - Valor: {self.valor}"
>>>>>>> e4fd9b255f47938380b6d371c8af2c933a7be891
