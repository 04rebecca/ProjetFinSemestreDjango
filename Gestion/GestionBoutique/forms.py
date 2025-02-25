from django import forms
from django.shortcuts import render
from .models import Produit, Vente, Transaction
from django.db.models import Sum

def tableau_de_bord(request):
    # Statistiques des produits
    total_produits = Produit.objects.count()
    total_quantite_stock = Produit.objects.aggregate(Sum('quantite'))['quantite__sum'] or 0

    # Statistiques des ventes
    total_ventes = Vente.objects.count()
    montant_total_ventes = Vente.objects.aggregate(Sum('total'))['total__sum'] or 0

    # Statistiques des transactions
    total_transactions = Transaction.objects.count()
    montant_total_transactions = Transaction.objects.aggregate(Sum('montant'))['montant__sum'] or 0

    # Récupérer les produits
    produits = Produit.objects.all()

    context = {
        'total_produits': total_produits,
        'total_quantite_stock': total_quantite_stock,
        'total_ventes': total_ventes,
        'montant_total_ventes': montant_total_ventes,
        'total_transactions': total_transactions,
        'montant_total_transactions': montant_total_transactions,
        'produits': produits,
    }
    return render(request, 'GestionBoutique/dashboard.html', context)

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'quantite', 'categorie']  

    def clean_prix(self):
        prix = self.cleaned_data.get('prix')
        if prix <= 0:
            raise forms.ValidationError("Le prix doit être un nombre positif.")
        return prix
    
class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['produit', 'quantite_vendue', 'total', 'date']  # Liste des champs à inclure

    def clean(self):
        cleaned_data = super().clean()
        quantite_vendue = cleaned_data.get("quantite_vendue")
        total = cleaned_data.get("total")

        # Validation de la quantité vendue
        if quantite_vendue is not None and quantite_vendue <= 0:
            self.add_error('quantite_vendue', "La quantité vendue doit être supérieure à 0.")

        # Validation du total
        if total is not None and total <= 0:
            self.add_error('total', "Le total doit être supérieur à 0.")

        return cleaned_data
    
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['service', 'montant', 'type_transaction', 'date_transaction']  # Liste des champs à inclure

    def clean(self):
        cleaned_data = super().clean()
        montant = cleaned_data.get("montant")

        # Validation du montant
        if montant is not None and montant <= 0:
            self.add_error('montant', "Le montant doit être supérieur à 0.")

        return cleaned_data    