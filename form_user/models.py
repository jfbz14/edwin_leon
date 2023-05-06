from django.db import models


class UserLeader(models.Model):
    """model userleader"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document_number = models.CharField(max_length=50, unique=True, error_messages={
            "unique": "Documento ya ha sido registrado",
        },)
    date = models.DateField()
    email = models.EmailField()
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
            "unique": "Documento ya ha sido registrado",
        },)
    date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    leader = models.CharField(max_length=4, default="1111")
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
        self.leader = self.leader.upper()
        self.address = self.address.upper()
        self.commune = self.commune.upper()
        self.neighborhood = self.neighborhood.upper()

        super().save(*args, **kwargs)
    