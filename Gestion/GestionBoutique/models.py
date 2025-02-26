from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)  # Image de la catégorie
    default_image = models.ImageField(upload_to='default_images/', blank=True, null=True)  # Image par défaut

    def get_image_url(self):
        if self.image:
            return self.image.url
        if self.default_image:
            return self.default_image.url
        return '/media/default_images/default_image.png'  # Image par défaut générique si aucune image n'est spécifiée

    
    @staticmethod
    def get_default_Categorie():
        return Categorie.objects.first()

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, default=Categorie.get_default_Categorie, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()

    def __str__(self):
        return self.nom

class Vente(models.Model):
    produit = models.ForeignKey(Produit, default=Produit.objects.first, on_delete=models.CASCADE)
    quantite_vendue = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(editable=True)

    def __str__(self):
        return f"Vente {self.id} - Total: {self.total}"
class Transaction(models.Model):
    service = models.CharField(max_length=20, choices=[('TMoney', 'TMoney'), ('Flooz', 'Flooz')])
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    type_transaction = models.CharField(max_length=20, choices=[('Depot', 'Depot'), ('Retrait', 'Retrait')])
    date_transaction = models.DateField(editable=True)

    def __str__(self):
        return f"{self.service} - {self.montant} FCFA"
    

