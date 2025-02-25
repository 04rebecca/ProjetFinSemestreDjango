from django.urls import path
from .views import accueil, liste_produits, liste_ventes, ajouter_produit, ajouter_vente, dashboard, rechercher_vente, liste_transactions, ajouter_transaction

urlpatterns = [
    path('', accueil, name='accueil'),  # Page d'accueil

    # URLs pour le modèle Produit
    path('produits/', liste_produits, name='liste_produits'),
    path('produits/ajouter/', ajouter_produit, name='ajouter_produit'),

    # URLs pour le modèle Vente
    path('ventes/', liste_ventes, name='liste_ventes'),
    path('ventes/ajouter/', ajouter_vente, name='ajouter_vente'),
    path('dashboard/', dashboard, name='dashboard'),   # Page tableau de bord
    path('recherche/', rechercher_vente, name='rechercher_vente'),
    path('transations/', liste_transactions, name='liste_transactions'),
    path('transactions/ajouter/', ajouter_transaction, name='ajouter_transaction'),
]
