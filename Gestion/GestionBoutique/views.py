from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from .forms import VenteForm, ProduitForm, TransactionForm, CategorieForm
from .models import Produit, Vente, Transaction, Categorie
# Formulaire d'inscription

def accueil(request):
    return render(request, 'GestionBoutique/index.html') 

def dashboard(request):
    produits = Produit.objects.all()  # Récupérer tous les produits
    return render(request, 'GestionBoutique/dashboard.html', {
        'produits': produits
    })

def gestion_categories(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST, request.FILES)  # Incluez request.FILES
        if form.is_valid():
            form.save()
            return redirect('gestion_categories')  # Redirige vers la même page

    else:
        form = CategorieForm()

    categories = Categorie.objects.all()
    return render(request, 'GestionBoutique/gestion_categories.html', {'categories': categories, 'form': form})

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

def modifier_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')  # Changez le nom selon votre configuration
    else:
        form = ProduitForm(instance=produit)

    return render(request, 'GestionBoutique/modifier_produit.html', {'form': form})

def supprimer_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    
    return render(request, 'GestionBoutique/supprimer_produit.html', {'objet': produit})

# Ventes
def modifier_vente(request, id):
    vente = get_object_or_404(Vente, id=id)
    
    if request.method == 'POST':
        form = VenteForm(request.POST, instance=vente)
        if form.is_valid():
            form.save()
            return redirect('liste_ventes')
    else:
        form = VenteForm(instance=vente)

    return render(request, 'GestionBoutique/modifier_vente.html', {'form': form})

def supprimer_vente(request, id):
    vente = get_object_or_404(Vente, id=id)
    if request.method == 'POST':
        vente.delete()
        return redirect('liste_ventes')
    
    return render(request, 'GestionBoutique/supprimer_vente.html', {'objet': vente})

# Transactions
def modifier_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('liste_transactions')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'GestionBoutique/modifier_transaction.html', {'form': form})

def supprimer_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    if request.method == 'POST':
        transaction.delete()
        return redirect('liste_transactions')
    
    return render(request, 'GestionBoutique/supprimer_transaction.html', {'objet': transaction})