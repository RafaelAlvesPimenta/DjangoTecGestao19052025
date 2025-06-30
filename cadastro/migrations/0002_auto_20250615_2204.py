from django.db import migrations

def inserir_unidades_medida(apps, schema_editor):
    UnidadeMedida = apps.get_model('cadastro', 'Unidade_medida')
    unidades = [
        {"nome": "Metro", "sigla": "m", "tipo": "Comprimento"},
        {"nome": "Centímetro", "sigla": "cm", "tipo": "Comprimento"},
        {"nome": "Milímetro", "sigla": "mm", "tipo": "Comprimento"},
        {"nome": "Polegada", "sigla": "in", "tipo": "Comprimento"},
        {"nome": "Unidade", "sigla": "un", "tipo": "Contagem"},
        {"nome": "Dezena", "sigla": "dz", "tipo": "Contagem"},
        {"nome": "Centena", "sigla": "ct", "tipo": "Contagem"},
        {"nome": "Quilograma", "sigla": "kg", "tipo": "Peso"},
        {"nome": "Grama", "sigla": "g", "tipo": "Peso"},
        {"nome": "Litro", "sigla": "l", "tipo": "Volume"},
        {"nome": "Mililitro", "sigla": "ml", "tipo": "Volume"},
        {"nome": "Rolo", "sigla": "rl", "tipo": "Pacote"},
        {"nome": "Pacote", "sigla": "pct", "tipo": "Pacote"},
    ]
    for unidade in unidades:
        UnidadeMedida.objects.get_or_create(**unidade)

class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),  # ou a última migração real
    ]

    operations = [
        migrations.RunPython(inserir_unidades_medida),
    ]
