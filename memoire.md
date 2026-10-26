# Panpsychisme informationnel : formalisation dynamique des relations entre champ, information et expérience subjective

**Statut** : Recherche exploratoire, numérique, non publiée.

---

## Introduction

Ce travail part d’une question philosophique : comment des structures dynamiques et informationnelles pourraient-elles être liées à l’organisation physique et à l’expérience subjective ? 
L’hypothèse directrice — non démontrée et formulée ici comme un programme de recherche — est que les relations entre organisation, information et manifestation sont aussi importantes que les propriétés locales. Ce cadre distingue la *Vacuité* (structure géométrique, relations, phase) de la *Plénitude* (actualisation locale, amplitude, pureté).

Afin d'éviter tout glissement ontologique, trois niveaux de preuve sont strictement séparés dans ce mémoire :
1. **Numérique** : ce que les scripts calculent.
2. **Méthodologique** : ce que les contrôles permettent de conclure.
3. **Ontologique** : hypothèse philosophique, séparée des résultats numériques.

---

## Chapitre 1 : Cadre théorique et méthodologique

Le projet s'appuie sur une séparation stricte entre deux couches de modélisation physique et mathématique.

### 1.1 Couche classique
Les modèles classiques utilisent les champs de Ginzburg-Landau pour explorer la topologie, l'annihilation de vortex et l'invariance contextuelle (phase contre amplitude). L'objectif est de tester si une dynamique classique linéaire peut conserver une mémoire historique.

### 1.2 Couche quantique
Les modèles quantiques utilisent l'équation maîtresse de Lindblad, la décohérence non-markovienne, la phase de Berry et la phase d'Uhlmann. La mesure finale de robustesse géométrique est effectuée via la **fidélité de Bures**.

### 1.3 Positionnement philosophique et épistémologique
Le cadre s'appuie sur des auteurs comme Leibniz, Bergson (durée), Sartre, Merleau-Ponty, Varela (autopoïèse), Chalmers (problème difficile) et Goff (panpsychisme). La méthodologie suit les principes de Lakatos (programme de recherche), avec des contrôles négatifs et des tests de permutation.

---

## Chapitre 2 : Résultats numériques

### 2.1 Résultats de la couche classique
* **V45-V46 (Ginzburg-Landau)** : Conservation d'énergie et convergence validées (erreur de masse à l'ordre de 10^-15, stabilité sous raffinement dt et N).
* **V53 (Topologie)** : Annihilation de vortex +/- validée (le winding number passe de 1 à 0).
* **V57 (Restauration de symétrie)** : Dissolution des défauts confirmée quand mu^2 devient positif.
* **V82 (Mémoire historique)** : Test négatif propre. La dynamique classique linéaire ne montre pas de mémoire historique (p = 0.78).

### 2.2 Résultats de la couche quantique
* **V77-V78 (Décohérence)** : La décohérence markovienne valide la chute de pureté vers 0.5. La mémoire non-markovienne (cavité) montre des récurrences quantiques.
* **V79 (Test de Bergson)** : Deux histoires menant au même état présent divergent à cause du passé de l'environnement.
* **V86-V88 (Phase d'Uhlmann)** : Balayage fin de gamma confirmant un effondrement, sans plateau résilient.

### 2.3 Le résultat final : V89 (Fidélité de Bures)
Configuration : qubit, Hamiltonien cyclique, canal de déphasage Lindblad, T=20, N=400 pas.

| Gamma | Pureté | Fidélité Bures | Angle de Bures |
| :--- | :--- | :--- | :--- |
| 0.000 | 1.0000 | 1.0000 | 0.0000 |
| 0.050 | 0.5819 | 0.8369 | 0.5792 |
| 0.100 | 0.5150 | 0.7628 | 0.7032 |
| 0.200 | 0.5009 | 0.7174 | 0.7708 |
| 0.300 | 0.5001 | 0.7092 | 0.7825 |
| 0.500 | 0.5000 | 0.7072 | 0.7852 |

**Interprétation** : La pureté (Plénitude) s'effondre rapidement. La fidélité de Bures (Vacuité) résiste plus longtemps mais finit par s'effondrer vers l'asymptote mathématique 1/√2. La structure géométrique est plus résiliente que l'état local, mais sa dégradation est inévitable.

---

## Chapitre 3 : Interprétation et limites

### 3.1 Ce que le travail démontre
* La dynamique classique linéaire est markovienne.
* La dynamique quantique non-markovienne conserve une dépendance à l'histoire.
* La fidélité de Bures décroît de façon monotone avec gamma, sans plateau physique.
* La pureté chute plus vite que la fidélité de Bures.

### 3.2 Ce que le travail ne démontre PAS
* Aucun lien avec la conscience ni avec la phénoménalité.
* Aucune preuve que la Vacuité soit indépendante du substrat physique.
* Aucune mesure directe d'expérience subjective.

### 3.3 Limites méthodologiques
La phase d'Uhlmann est instable numériquement à gamma ≈ 0.025. Le test V82 ne prouve pas que "seule la distribution compte" de façon universelle, mais seulement l'absence de mémoire dans cette équation. Le test V79 montre une dépendance à l'histoire de l'environnement, pas une "durée vécue" au sens de Bergson.

---

## Conclusion générale

Ce travail a construit et testé numériquement un ensemble de modèles dynamiques permettant de comparer deux types de résistance à la décohérence : celle de l’état local (pureté) et celle de la structure relationnelle (fidélité de Bures). Les résultats montrent que la pureté s’effondre rapidement vers le mélange maximal, tandis que la fidélité de Bures décroît plus lentement, avant de converger elle aussi vers l’asymptote mathématique 1/√2. Il n’y a pas de plateau résilient au sens physique : la structure géométrique est plus robuste, mais elle n’est pas indépendante du substrat dynamique.

Sur le plan philosophique, ces résultats ne démontrent aucun lien avec la conscience ou une forme de panpsychisme informationnel. Ils fournissent seulement un cadre formel pour penser la dégradation différentielle de l’actualisation locale et des relations géométriques sous décohérence. La distinction entre Vacuité et Plénitude reste une hypothèse de lecture. Le programme de recherche est donc maintenu comme cadre heuristique, mais sa portée ontologique demeure explicitement hors du champ de ce qui a été établi.
