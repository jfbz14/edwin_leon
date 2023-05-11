from django.db import models


class UserLeader(models.Model):
    """model userleader"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document_number = models.CharField(max_length=50, unique=True, error_messages={
            "unique": "Documento ya ha sido registrado",
        },)
    date = models.DateField()
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        """return last_name and doucemnt_number"""

        return '{} {}'.format(self.first_name, self.last_name)    

    def save(self, *args, **kwargs ):
        """for uppercase fields"""

        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        self.email = self.email.upper()

        super().save(*args, **kwargs)


class UserProfile(models.Model):
    """model form user"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document_number = models.CharField(max_length=50, unique=True, error_messages={
            "unique": "Documento está registrado",
        },)
    date = models.DateField()
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=10)
    leader = models.ForeignKey(UserLeader, on_delete=models.CASCADE, blank=True, null=True )
    address = models.CharField(max_length=150)
    commune = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=150)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        """return last_name and doucemnt_number"""

        return '{} - {}'.format(self.first_name, self.document_number)
    
    def save(self, *args, **kwargs ):
        """for uppercase fields"""

        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        self.email = self.email.upper()
        self.address = self.address.upper()
        self.commune = self.commune.upper()
        self.neighborhood = self.neighborhood.upper()

        super().save(*args, **kwargs)


class CommuneModel(models.Model):
    """ model commune"""
    name_commune = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=150, unique=True, blank=True, null=True)

    def __str__(self):
        """return name"""

        return '{}'.format(self.name_commune)


class NeighborhoodModel(models.Model):
    """model neighborhood"""

    name_commune = models.ForeignKey(CommuneModel, on_delete=models.CASCADE)
    name_neighborhood = models.CharField(max_length=150, unique=True)

    def __str__(self):
        """return name"""

        return '{}'.format(self.name_neighborhood)
    