# Generated by Django 5.2 on 2025-06-29 16:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_categorias_materia_prima_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendas',
            name='comprador',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='comprador_nome',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='data',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='valor',
        ),
        migrations.AddField(
            model_name='vendas',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro.clientes'),
        ),
        migrations.AddField(
            model_name='vendas',
            name='cliente_nao_cadastrado',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vendas',
            name='data_venda',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendas',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=(0, 0), max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientes',
            name='CPF',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='ProdutoVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.vendas')),
            ],
        ),
    ]
