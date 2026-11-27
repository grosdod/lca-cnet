# Entraînement LCA

Plateforme d'entraînement à la lecture critique d'article (LCA) pour l'EDN.
Site : https://lca.therap.fr

Conception, rédaction et coordination : Pr Hervé Devilliers.

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
- Images : placer les fichiers (PNG, JPG…) dans un sous-dossier, par ex. `contenu/qi/img/ma-serie/`, et les appeler dans l'énoncé par `![Figure 1](img/ma-serie/fig1.png)` (ou une ligne `Image : img/ma-serie/fig1.png`). Le chemin est relatif au fichier .md.
- Une nouvelle notion est acceptée (elle s'ajoute en fin de liste) ; pour choisir sa place, l'ajouter dans `notions.txt`.

### Épreuves LCA complètes : `contenu/lca/<nom>/`

- `sujet.md` : le « sujet corrigé de relecture » (en-tête **Titre de l'article**, **Référence courte**, **Référence complète**, puis `## Vignette`, `## Glossaire`, `## Question 1 – Question à choix multiple`, …, avec **Notion :** sous chaque question).
- Ajouter dans l'en-tête `**Lien vers l'article :** https://doi.org/…` (éditeur ou PubMed).
- `annexe1.md`, `annexe2.md`… : annexes affichées pendant l'épreuve.
- **Ne déposer le PDF de l'article que s'il est en libre accès** (licence CC-BY…) : tout PDF présent dans le dossier est publié.

## Mode enseignant

Ouvrir **https://lca.therap.fr/?edit** (mémorisé dans le navigateur ; `?edit=0` pour l'enlever). Chaque question affiche alors :
- **✎ Modifier** : ouvre le fichier dans l'éditeur GitHub (chercher le titre indiqué, par ex. « ## QI 12 ») ; *Commit changes* publie la correction en 1 à 2 minutes. Un collègue sans droit d'écriture obtient une proposition de modification, à accepter ou refuser.
- **💬 Suggérer une modification** : ouvre un ticket GitHub prérempli (série, numéro, énoncé, propositions).

## Vérifier avant de déposer (facultatif)

```
python outils/build.py
```

Le script signale les QRU sans bonne réponse unique, les propositions manquantes et les notions inconnues. En cas d'erreur, la mise en ligne s'arrête et le site garde sa version précédente.

## Ce qui est public

© Pr Hervé Devilliers, contenu sous licence CC BY-NC-ND 4.0 (voir LICENSE). Les réponses sont encodées dans les données du site et ne sont décodées qu'après validation. Les résultats des étudiants restent dans leur navigateur (aucun compte, aucune donnée collectée).
