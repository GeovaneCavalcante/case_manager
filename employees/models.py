import boto3
import json
from django.db import models


class Employee(models.Model):
    full_name = models.CharField(verbose_name='Nome Completo', max_length=255)
    register_number = models.CharField(verbose_name='Matrícula', max_length=10)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    is_active = models.BooleanField(verbose_name='Ativo', default=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.full_name


class EmployeeFileImport(models.Model):
    file = models.FileField(
        verbose_name='Arquivo de Importação')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Arquivo de Importação'
        verbose_name_plural = 'Arquivos de Importação'

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        sqs = boto3.client(
            'sqs',
            region_name='us-east-1',
            endpoint_url="http://localhost:4566"
        )

        message_body = {
            "file_name": self.file.name,
            "data": {"teste": True}
        }

        queue_url = "http://localhost:4566/000000000000/employees-process"

        msg = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message_body)
        )

        print(msg)
