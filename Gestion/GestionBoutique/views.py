from django.shortcuts import render, redirect
from .forms import VenteForm, ProduitForm, TransactionForm
from .models import Produit, Vente, Transaction
# Formulaire d'inscription

def accueil(request):
    return render(request, 'GestionBoutique/index.html') 

def dashboard(request):
    produits = Produit.objects.all()  # Récupérer tous les produits
    return render(request, 'GestionBoutique/dashboard.html', {
        'produits': produits
    })

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')  # Rediriger vers la page de liste des produits
        else:
            print(form.errors)  # Afficher les erreurs dans la console pour le débogage
    else:
        form = ProduitForm()
    return render(request, 'GestionBoutique/ajouter_produit.html', {'form': form})
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'GestionBoutique/liste_produits.html', {'produits': produits})

def ajouter_vente(request):
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_ventes')  # Rediriger vers la page de liste des ventes
        else:
            print(form.errors)  # Afficher les erreurs dans la console pour le débogage
    else:
        form = VenteForm()
    return render(request, 'GestionBoutique/ajouter_vente.html', {'form': form})
def liste_ventes(request):
    ventes = Vente.objects.all()
    return render(request, 'GestionBoutique/liste_ventes.html', {'ventes': ventes})

def rechercher_vente(request):
    query = request.GET.get('q')
    ventes = Vente.objects.all()
    if query:
        ventes = Vente.objects.filter(produit__nom__icontains=query)
    return render(request, 'GestionBoutique/recherche.html', {'ventes': ventes, 'query': query})

def ajouter_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_transactions')  # Rediriger vers la page de liste des produits
        else:
            print(form.errors)  # Afficher les erreurs dans la console pour le débogage
    else:
        form = TransactionForm()
    return render(request, 'GestionBoutique/ajouter_transaction.html', {'form': form})
def liste_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'GestionBoutique/liste_transactions.html', {'transactions': transactions})