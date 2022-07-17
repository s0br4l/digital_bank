import uuid

from django.core.validators import RegexValidator
from django.db import models


class Contas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True, validators=[RegexValidator(r'^\d{1,11}$')])
    rg = models.CharField(max_length=13, unique=True, validators=[RegexValidator(r'^\d{1,13}$')])
    celular = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,9}$')])
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{1,8}$')])
    email = models.EmailField()
    saldo = models.DecimalField(max_digits=15, decimal_places=2, null=True)

    def __str__(self):
        return self.id


class Historico(models.Model):
    ENVIADO = "-"
    RECEBIDO = "+"
    TIPOS_TRANSF = [(ENVIADO, 'Enviar'), (RECEBIDO, 'Receber')]

    id = models.OneToOneField(Contas, on_delete=models.CASCADE, primary_key=True)
    data_transf = models.DateTimeField()
    valor_transf = models.DecimalField(max_digits=15, decimal_places=2)
    tipo_transf = models.CharField(max_length=1, choices=TIPOS_TRANSF)
