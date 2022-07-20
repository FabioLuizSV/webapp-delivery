from django.db import models

class Cardapio(models.Model):
    """Definição de modelo para Cardapio."""

    nomeCardapio = models.CharField(max_length=60, name='Cardápio')
    bloqueado = models.BooleanField()

    class Meta:
        """Definição de Meta para Cardapio."""

        verbose_name = 'Cardapio'
        verbose_name_plural = 'Cardapios'

    def __str__(self):
        return self.nomeCardapio