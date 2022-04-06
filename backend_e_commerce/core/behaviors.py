import uuid
from django.db import models


class ActiveSwitchable(models.Model):
    """
    Behavior que agrega a un modelo las propiedades de estado activo o inactivo
    """
    is_active = models.BooleanField(default=True, verbose_name='Estado')

    def switch_active(self):
        """
        Método para cambiar el estado de una notaría
        """
        self.is_active = not self.is_active
        self.save()

    class Meta:
        abstract = True


class ApplicationModelBase(ActiveSwitchable):
    """
    Behavior que agrega a un modelo las propiedades de fecha de creación, fecha de modificación y autor de la
    modificación
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
