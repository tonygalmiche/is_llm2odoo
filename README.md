# is_llm2odoo — Recherche intelligente par IA pour Odoo 14

## Description

Ce module Odoo 14 intègre un serveur VLLM (compatible API OpenAI) pour offrir une **recherche en langage naturel** dans Odoo. L'utilisateur décrit sa recherche en français (ex : *"Liste des factures de ce mois"*) et le module utilise l'IA pour :

1. **Identifier automatiquement le modèle Odoo** concerné (factures, commandes, contacts…)
2. **Générer un domaine de filtre Odoo** à partir de la question
3. **Proposer le type de vue** le plus adapté (liste, graphique ou tableau croisé dynamique)
4. **Déterminer le regroupement** optimal pour les vues analytiques
5. **Afficher les résultats** directement dans Odoo

Les recherches peuvent être **enregistrées comme favoris** pour être réutilisées.

## Fonctionnalités

- Recherche en langage naturel (français)
- Détection automatique du modèle Odoo cible
- Génération et validation automatique des domaines Odoo
- Suggestion du type de vue (liste, graphique, pivot)
- Regroupement intelligent (par date, par champ relationnel…)
- Gestion des dates relatives ("ce mois", "cette année", "depuis 2019"…)
- Recherche sur les champs relationnels (Many2one)
- Sauvegarde des recherches en tant que filtres/favoris
- Support multimodal (images et PDF via VLLM vision)
- Traçabilité des réponses IA pour audit et débogage
- Sécurité par utilisateur (chaque utilisateur ne voit que ses propres recherches)

## Modèles

| Modèle | Description |
|---|---|
| `is.search.general` | Enregistrement et exécution des recherches en langage naturel |
| `is.vllm` | Modèle abstrait réutilisable pour communiquer avec un serveur VLLM |
| `res.company` | Extension pour la configuration du serveur VLLM (URL, clé API, modèle, température…) |

## Configuration

Dans **Paramètres > Sociétés**, un onglet **VLLM** permet de configurer :

- **URL du serveur VLLM** (ex : `http://localhost:8000`)
- **Clé API** (optionnelle)
- **Nom du modèle** (ex : `meta-llama/Llama-2-7b-chat-hf`)
- **Température** (0 = déterministe, 1 = créatif, défaut : 0.7)
- **Nombre max de tokens** (défaut : 2048)

## Sécurité

Deux groupes d'utilisateurs :

- **Recherche générale IA** : accès à ses propres recherches uniquement
- **Administrateur IA** : accès à toutes les recherches

## Dépendances

**Modules Odoo :**
- `base`
- `mail`

**Python :**
- `requests`
- `pdf2image` (optionnel, pour le support PDF en mode vision)

## Licence

LGPL-3
