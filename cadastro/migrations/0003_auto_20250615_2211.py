from django.db import migrations

def inserir_unidades_compra(apps, schema_editor):
    UnidadeCompra = apps.get_model('cadastro', 'Unidade_compra')
    unidades = [
        {"nome": "Caixa", "sigla": "cx", "tipo": "Embalagem"},
        {"nome": "Rolo", "sigla": "rl", "tipo": "Pacote"},
        {"nome": "Fardo", "sigla": "fd", "tipo": "Volume"},
        {"nome": "Pacote", "sigla": "pct", "tipo": "Pacote"},
        {"nome": "Tonel", "sigla": "tn", "tipo": "Volume"},
        {"nome": "Saco", "sigla": "sc", "tipo": "Volume"},
        {"nome": "Lote", "sigla": "lt", "tipo": "Agrupamento"},
        {"nome": "Bobina", "sigla": "bb", "tipo": "Rolo"},
        {"nome": "Galão", "sigla": "gl", "tipo": "Volume"},
        {"nome": "Embalagem", "sigla": "emb", "tipo": "Geral"},
    ]
    for unidade in unidades:
        UnidadeCompra.objects.get_or_create(**unidade)

class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20250615_2204'),
    ]

    operations = [
        migrations.RunPython(inserir_unidades_compra),
    ]