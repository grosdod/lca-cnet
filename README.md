# Entraînement LCA – CNET

Plateforme d'entraînement à la lecture critique d'article (LCA) du Collège National des Enseignants de Thérapeutique.
Site : https://lca.therap.fr

## Ajouter des questions

Il suffit de déposer des fichiers Markdown sur GitHub (bouton **Add file → Upload files**) : le site se met à jour tout seul en 1 à 2 minutes (onglet **Actions** pour suivre).

### Questions isolées (QI) : `contenu/qi/`

Un fichier par série, au format des séries produites dans le projet :

```markdown
# Titre de la série

## QI 1 (QRM)

Énoncé (tableaux Markdown acceptés)… Il est vrai que :

**A.** Proposition juste ✅
> Correction de la proposition A.

**B.** Proposition fausse
> Correction de la proposition B.

**Commentaire :** Piège d'annale visé…

**Notion :** Randomisation
```

- `✅` marque les bonnes réponses ; une QRU doit en avoir exactement une.
- `**Notion :**` doit reprendre un intitulé de `contenu/notions.txt` (vocabulaire des annales). Plusieurs notions : les séparer par ` ; `.
- Une nouvelle notion est acceptée (elle s'ajoute en fin de liste) ; pour choisir sa place, l'ajouter dans `notions.txt`.

### Épreuves LCA complètes : `contenu/lca/<nom>/`

- `sujet.md` : le « sujet corrigé de relecture » (en-tête **Titre de l'article**, **Référence courte**, **Référence complète**, puis `## Vignette`, `## Glossaire`, `## Question 1 – Question à choix multiple`, …, avec **Notion :** sous chaque question).
- Ajouter dans l'en-tête `**Lien vers l'article :** https://doi.org/…` (éditeur ou PubMed).
- `annexe1.md`, `annexe2.md`… : annexes affichées pendant l'épreuve.
- **Ne déposer le PDF de l'article que s'il est en libre accès** (licence CC-BY…) : tout PDF présent dans le dossier est publié.

## Vérifier avant de déposer (facultatif)

```
python outils/build.py
```

Le script signale les QRU sans bonne réponse unique, les propositions manquantes et les notions inconnues. En cas d'erreur, la mise en ligne s'arrête et le site garde sa version précédente.

## Ce qui est public

Le dépôt et le site sont publics : questions, corrections et épreuves. Les résultats des étudiants restent dans leur navigateur (aucun compte, aucune donnée collectée).
