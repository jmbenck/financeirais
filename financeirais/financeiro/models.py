from django.db import models

class Categoria(models.Model):

    nome_categoria = models.CharField(max_length=100)


    def __str__(self):
        return str(self.nome_categoria)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Movimentacao(models.Model):
    Tipos = ((1, 'Entrada'), (2, 'Saida'))
    data_hora = models.DateTimeField()
    tipo = models.IntegerField(choices=Tipos)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    anexo = models.FileField(upload_to='anexos/%Y/%m/', null=True, blank=True)
    descricao = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return str(self.data_hora)

    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'