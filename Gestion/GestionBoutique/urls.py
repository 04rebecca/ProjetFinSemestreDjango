from django.urls import path
from .views import accueil, liste_produits, liste_ventes, ajouter_produit, ajouter_vente, dashboard, rechercher_vente, liste_transactions, ajouter_transaction, gestion_categories, modifier_produit, supprimer_produit, modifier_vente, supprimer_vente, modifier_transaction, supprimer_transaction, modifier_categorie, supprimer_categorie
from django.conf import settings
from django.conf.urls.static import static

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
    path('categories/', gestion_categories, name='gestion_categories'),
    path('produits/modifier/<int:id>/', modifier_produit, name='modifier_produit'),
    path('produits/supprimer/<int:id>/', supprimer_produit, name='supprimer_produit'),
    path('ventes/modifier/<int:id>/', modifier_vente, name='modifier_vente'),
    path('ventes/supprimer/<int:id>/', supprimer_vente, name='supprimer_vente'),
    path('transactions/modifier/<int:id>/', modifier_transaction, name='modifier_transaction'),
    path('transactions/supprimer/<int:id>/', supprimer_transaction, name='supprimer_transaction'),
    path('categories/modifier/<int:id>/', modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:id>/', supprimer_categorie, name='supprimer_categorie'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

