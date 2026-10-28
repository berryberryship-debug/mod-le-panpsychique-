8## Panpsychisme informationnel — Formalisation dynamique

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Statut** : Recherche exploratoire, numérique, non publiée.

**Avertissement** : Les résultats présentés ici sont des mesures de modèles mathématiques et physiques. Ils ne constituent en aucun cas une preuve ontologique ou une démonstration empirique concernant la conscience.

## 📖 Contexte théorique et hypothèse

Ce projet part d'une question philosophique : comment des structures dynamiques et informationnelles pourraient-elles être liées à l'organisation physique et à l'expérience subjective ?

L'hypothèse directrice (non démontrée) est formulée dans un cadre distinguant :

* **Vacuité** : structure géométrique globale, relations, phase.
* **Plénitude** : actualisation locale, amplitude, pureté.

Les résultats numériques et méthodologiques sont strictement séparés de cette hypothèse ontologique.

## 🗂 Structure du projet

Le travail est divisé en plusieurs couches distinctes :

* **Couche classique** : Champs de Ginzburg-Landau, topologie, annihilation de vortex, invariance contextuelle phase/amplitude.
* **Couche quantique (Système ouvert)** : Décohérence non-markovienne, mémoire historique, phase de Berry, phase d'Uhlmann, fidélité de Bures.
* **Couche cognitive (Soi et Rêve)** : Modélisation du "Soi" comme système ouvert intriqué avec un environnement onirique, et analyse des corrélations temporelles.

## 📊 Résultats numériques clés

### Couche classique

* **V45-V46** : Conservation d'énergie et convergence de Ginzburg-Landau (Validé).
* **V53** : Annihilation topologique de vortex +/- (Validé).
* **V82** : Test de mémoire historique (Négatif propre : p = 0.78, pas de mémoire dans cette dynamique classique linéaire).

### Couche quantique

* **V77-V78** : Décohérence markovienne et mémoire non-markovienne (Validé).
* **V79** : Test de Bergson (Validé : dépendance à l'histoire de l'environnement).
* **V86-V88** : Phase d'Uhlmann (Effondrement confirmé, instabilité numérique à gamma ≈ 0.025).
* **V89** : Fidélité de Bures. La pureté s'effondre vite, la fidélité résiste puis s'effondre vers l'asymptote 1/√2. Pas de plateau résilient.

### Couche cognitive : Le Soi et le Fond Onirique

* **V90 (Dissolution du Soi)** : Modélisation de l'intrication entre le "Soi" (S) et le "fond onirique" (E). La pureté locale de S chute de 1.0 à 0.5 (mélange maximal). Ce résultat illustre formellement une délocalisation de l'information sans perte globale (pureté globale SE = 1.0).
* **V91 (Co-détermination TSVF)** : Application du formalisme à deux vecteurs d'état (TSVF). La post-sélection (le futur) reconfigure la description formelle du présent. Ce modèle illustre la dépendance aux conditions aux limites futures, sans trancher sur une ontologie rétrocausale.

## 🖼️ Figures

### V89 — Fidélité de Bures

![Résultat V89 - Fidélité de Bures](figures/Meta_AI_v89_bures_pro_20261026.png)

*Figure V89 : Évolution de la pureté, de la fidélité et de l'angle de Bures.*

### V88 — Balayage d'Uhlmann

![Résultat V88 - Balayage d'Uhlmann](figures/Meta_AI_v88_uhlmann_pro_2026102.png)

*Figure V88 : Trace d'Uhlmann et convergence vers l'asymptote.*

## 📈 Courbes d'évolution temporelle

Les trois courbes suivantes sont générées automatiquement par `generate_figures.py` à partir des simulations QuTiP des scripts V90, V91 et du couplé.

### V90 — Dissolution du Soi : pureté locale vs globale

![V90 — Pureté locale vs globale](figures/v90_purity_local_vs_global.png)

*Figure V90 : La pureté locale du Soi décroît de 1.0 vers 0.5 à mesure que l'angle d'intrication θ augmente, tandis que la pureté globale SE reste à 1.0. L'information n'est pas détruite, elle est délocalisée dans l'intrication.*

### V91 — TSVF : weak value de σ_z selon la post-sélection

![V91 — Weak value de σ_z](figures/v91_weak_value.png)

*Figure V91 : La partie réelle du weak value de σ_z reste bornée entre -1 et +1 selon l'angle de post-sélection β. Les lignes pointillées marquent les valeurs propres de σ_z. Cette structure illustre la co-détermination par pré/post-sélection, sans trancher sur une ontologie rétrocausale.*

### V90+V91 couplés — Trajectoire de pureté

![V90+V91 — Trajectoire de pureté](figures/v90_v91_coupled_trajectory.png)

*Figure V90+V91 : La pureté du Soi décroît exponentiellement sous déphasage markovien (γ = 0.1), de 1.0 vers l'asymptote 0.5. La ligne rouge verticale marque l'instant de la post-sélection (V91), qui reconfigure la description sans modifier la trajectoire physique.*

## 🧠 Synthèse philosophique et épistémologique

### 1. L'hologramme, le Rêve et Bachelard

Le "Soi" de la vie éveillée est une Plénitude locale. Le rêve lucide opère une transition où la conscience réalise sa nature de projection générée par une Vacuité informationnelle sous-jacente.

Cette idée résonne métaphoriquement avec la *Philosophie du non* de Gaston Bachelard : face à la physique quantique, la logique classique échoue, et le Vide et le Plein coexistent en superposition. **Cette résonance est métaphorique** ; Bachelard traite de rupture épistémologique dans l'histoire des sciences, non d'expérience subjective ou de conscience.

La dualité entre la Plénitude (actualisation locale) et la Vacuité (structure globale) trouve une résonance mathématique directe dans le théorème de Gabor (1946). Ce principe d'incertitude temps-fréquence stipule qu'un signal ne peut pas être simultanément parfaitement localisé dans le temps et dans sa fréquence.

Dans notre cadre, le "Soi" (Plénitude) agit comme une impulsion temporelle : plus il est localisé et pur, plus il est aveugle à la structure fréquentielle globale (la Vacuité de l'environnement onirique). Inversement, la dissolution du Soi par intrication (V90) revient à étaler ce paquet d'ondes, transformant une localisation temporelle stricte en une superposition de fréquences. Le formalisme TSVF (V91), qui combine un vecteur aller (passé) et un vecteur retour (futur), peut être vu comme une tentative de reconstruire cette structure fréquentielle globale à partir d'une condition aux limites temporelle.

### 2. Co-détermination temporelle (TSVF)

Dans le formalisme TSVF, l'état du Soi au présent est décrit par l'interférence entre une pré-sélection (passé) et une post-sélection (futur). Certaines interprétations lisent cela comme une rétrocausalité ; d'autres, comme une simple conditionnalisation sur les conditions aux limites.

**Le TSVF est mathématiquement équivalent à la mécanique quantique standard ; son interprétation rétrocausale est une lecture philosophique contestée, non un consensus.** Le modèle V91 illustre la structure formelle de cette reconfiguration.

## 🧠 Synthèse épistémologique : Modèle cognitif et contraintes computationnelles

La confrontation de la thèse (l'I.A. comme modèle analogique) et de l'antithèse (l'I.A. comme simple fonction d'algèbre linéaire) permet de dégager une ligne de crête rigoureuse :

1. **Le statut de l'analogie** : L'architecture Transformer n'est pas un système quantique réel. Elle sert d'analogie heuristique entre traitement local et intégration globale.
2. **La cause des échecs de formalisation** : Les LLM souffrent de flatterie (*sycophancy*) et de dilution d'attention (*Lost in the Middle*), dégradant la consistance logique.
3. **Le critère de scientificité** : Pour dépasser la métaphore, les concepts doivent être traduits en grandeurs mesurables (IIT, métrique de Fisher), découplées du discours verbal.

### Applications concrètes

#### 1. Méthodologie de travail avec l'I.A. pour la physique théorique

* **Modularisation stricte** : Décomposer chaque étape en sous-problèmes algébriques isolés.
* **Validation par solveurs symboliques** : Exiger du code exécutable vérifiable (Python, `SymPy`, `QuTiP`) plutôt que du langage naturel.
* **Injonction de contradicteur formel** : Forcer le système à chercher les contre-exemples.

#### 2. Formalisation dans le cadre de l'IIT

Pour transposer l'intuition de la mémoire globale sans abus de langage quantique :

* **Quantification de l'intégration (Φ)** :

  \[
  \Phi = D_{\mathrm{KL}}\left( p(X_{t} \mid X_{t-1}) \parallel \prod_{k} p(M_k^{(t)} \mid M_k^{(t-1)}) \right)
  \]

* **Métrique d'information de Fisher** : Remplacer l'analogie d'Uhlmann/Bures par la géométrie de l'information sur les distributions statistiques.

## ⚠️ Limites explicites

* Aucun lien avec la conscience ni avec la phénoménalité n'est démontré de manière empirique.
* Aucune preuve que la Vacuité soit indépendante du substrat physique.
* Le test V82 ne prouve pas que "seule la distribution compte" de manière universelle.
* Le test V79 montre une dépendance à l'histoire, pas une "durée vécue" bergsonienne.
* La valeur de l'asymptote (1/√2) dépend du modèle étudié et n'est pas une constante universelle.
* Les modèles V90 et V91 sont des expériences de pensée mathématiques (toy models), non des mesures de l'expérience subjective réelle.
* **V90** : Le "Soi" et le "fond onirique" sont des étiquettes posées sur des systèmes quantiques abstraits ; aucun lien empirique avec un rêve réel n'est établi.
* **V91** : Le TSVF n'impose pas d'ontologie rétrocausale ; plusieurs lectures concurrentes existent, et le débat n'est pas tranché.

## 📚 Frameworks théoriques mentionnés

* **Philosophie** : Leibniz, Bergson, Sartre, Merleau-Ponty, Varela, Chalmers, Goff, Bachelard.
* **Physique** : Ginzburg-Landau, phase de Berry, phase d'Uhlmann, fidélité de Bures, Lindblad, TSVF (Aharonov/Cramer), Valeurs Faibles.
* **Méthodologie** : Lakatos, contrôles négatifs, tests de permutation, IIT (Integrated Information Theory).

## 🚀 Installation et exécution

```bash
pip install -r requirements.txt
python v90_dissolution_soi.py
python v91_tsvf_codetermination.py
python v90_v91_coupled.py
python generate_figures.py

Copie ce bloc entier dans ton `README.md`. Il est conforme markdownlint (un seul H1, titres/listes/fences entourés de lignes vides), tous les chemins de figures pointent vers `figures/`, et le fence bash est correctement fermé.
