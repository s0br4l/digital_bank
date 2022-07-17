import uuid
from django.core.validators import RegexValidator
from django.db import models


class Contas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True, validators=[RegexValidator(
        regex=r'^\d{1,11}$', message='CPF: inserir apenas numeros')])
    rg = models.CharField(max_length=13, unique=True, validators=[RegexValidator(
        regex=r'^\d{1,13}$', message='RG: inserir apenas numeros')])
    celular = models.CharField(max_length=11, validators=[RegexValidator(
        regex=r'^\d{1,11}$', message='Celular: inserir apenas numeros')])
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=8, validators=[RegexValidator(
        regex=r'^\d{1,8}$', message='CEP: inserir apenas numeros')])
    email = models.EmailField()
    saldo = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0.00)

    def __str__(self):
        return str(self.cpf)


class Historico(models.Model):
    ENVIADO = "-"
    RECEBIDO = "+"
    TIPOS_TRANSF = [(ENVIADO, 'Enviar'), (RECEBIDO, 'Receber')]

    id = models.OneToOneField(Contas, on_delete=models.CASCADE, primary_key=True)
    data_transf = models.DateTimeField()
    valor_transf = models.DecimalField(max_digits=15, decimal_places=2)
    tipo_transf = models.CharField(max_length=1, choices=TIPOS_TRANSF)
