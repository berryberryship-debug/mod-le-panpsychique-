# Panpsychisme informationnel — Formalisation dynamique

**Statut** : Recherche exploratoire, numérique, non publiée.
**Avertissement** : Les résultats présentés ici sont des mesures de modèles mathématiques et physiques. Ils ne constituent en aucun cas une preuve ontologique ou une démonstration empirique concernant la conscience.

## 📖 Contexte théorique et hypothèse

Ce projet part d'une question philosophique : comment des structures dynamiques et informationnelles pourraient-elles être liées à l'organisation physique et à l'expérience subjective ?

L'hypothèse directrice (non démontrée) est formulée dans un cadre distinguant :
* **Vacuité** : structure géométrique globale, relations, phase.
* **Plénitude** : actualisation locale, amplitude, pureté.

Cette distinction est le fil directeur philosophique du projet. Elle guide la construction des modèles sans être présentée comme un résultat démontré par les simulations ; elle demeure une hypothèse ontologique ouverte, strictement séparée des mesures numériques.

## 🗂 Structure du projet et critères de réussite

Le travail est divisé en plusieurs couches distinctes. Chaque résultat est lié à son script et à un critère explicite de vérification.

### Couche classique
* **V45-V46** : Champs de Ginzburg-Landau.
  * *Script* : `v45_v46_ginzburg_landau.py`
  * *Critère* : Conservation d'énergie (erreur < 10^-15) et convergence stable sous raffinement dt/N.
* **V53** : Annihilation topologique de vortex.
  * *Script* : `v53_vortex_annihilation.py`
  * *Critère* : Le winding number passe de 1 à 0.
* **V82** : Test de mémoire historique.
  * *Script* : `v82_test_memoire_historique.py`
  * *Critère* : Test de permutation (p = 0.78). Résultat négatif propre (absence de mémoire dans cette dynamique classique).

### Couche quantique
* **V77-V78** : Décohérence et mémoire non-markovienne.
  * *Scripts* : `v77_qsim_memory.py`, `v78_qsim_nonmarkov.py`
  * *Critère* : Chute de pureté vers 0.5 (V77) et observation de récurrences quantiques (V78).
* **V79** : Test de Bergson.
  * *Script* : `v79_bergson_test.py`
  * *Critère* : Divergence des trajectoires dues au passé de l'environnement.
* **V89** : Fidélité de Bures (Résultat final).
  * *Script* : `v89_bures_fidelity2.py`
  * *Critère* : La pureté s'effondre rapidement. La fidélité résiste puis tend vers une asymptote. *Note : pour un qubit déphasé dont l'état tend vers le mélange maximal, la fidélité avec l'état initial pur tend vers \(1/\sqrt{2}\) selon la convention de fidélité avec racine, ou \(0.5\) selon la convention au carré. Ce résultat dépend de l'état de référence et de la définition employée.*

### Couche cognitive : Le Soi et le Fond Onirique
* **V90 (Dissolution du Soi)** : Intrication entre le "Soi" (S) et le "fond onirique" (E).
  * *Script* : `v90_dissolution_soi.py`
  * *Critère* : Pureté locale de S chute de 1.0 à 0.5, pureté globale SE reste à 1.0. *Le modèle établit une redistribution des propriétés de l'état (délocalisation de l'information), sans perte globale.*
* **V91 (Co-détermination TSVF)** : Formalisme à deux vecteurs d'état.
  * *Script* : `v91_tsvf_codetermination.py`
  * *Critère* : Reconfiguration de la matrice densité par post-sélection. *Note : les valeurs faibles (weak values) calculées peuvent être anomales et dépasser l'intervalle spectral des valeurs propres lorsque le chevauchement est faible.*

### Modèles de neurodynamique et systèmes couplés
* **V93 (Modulation d'amplitude)** : Bandes latérales (30 et 50 Hz).
  * *Script* : `v93_modulation_amplitude.py`
  * *Critère* : Vérification de l'identité trigonométrique par FFT.
* **V94 (Forçage vs Coévolution)** : Oscillateurs de Stuart-Landau couplés.
  * *Script* : `v94_forced_vs_coupled.py`
  * *Critère* : Observation de l'intermodulation et de la modification du spectre lent lorsque la rétroaction (beta) est active.

## 🖼️ Figures

*(Assure-toi que les noms de fichiers correspondent exactement à ceux uploadés)*

![Résultat V89 - Fidélité de Bures](Meta_AI_v89_bures_pro_20261026.png)
*(Figure V89 : Évolution de la pureté, de la fidélité et de l'angle de Bures)*

![Résultat V88 - Balayage d'Uhlmann](Meta_AI_v88_uhlmann_pro_2026102.png)
*(Figure V88 : Trace d'Uhlmann et convergence vers l'asymptote)*

## 🧠 Synthèse philosophique et épistémologique

### 1. L'hologramme, le Rêve et Bachelard
Le "Soi" de la vie éveillée est une Plénitude locale. Le rêve lucide opère une transition où la conscience réalise sa nature de projection générée par une Vacuité informationnelle sous-jacente. 
Cette idée résonne métaphoriquement avec la *Philosophie du non* de Gaston Bachelard. **Cette résonance est métaphorique** ; Bachelard traite de rupture épistémologique dans l'histoire des sciences, non d'expérience subjective ou de conscience.

### 2. Co-détermination temporelle (TSVF)
Dans le formalisme TSVF, l'état du Soi au présent est décrit par l'interférence entre une pré-sélection (passé) et une post-sélection (futur). **Le TSVF est mathématiquement équivalent à la mécanique quantique standard ; son interprétation rétrocausale est une lecture philosophique contestée, non un consensus.**

### 3. Incertitude de Gabor et intrication
Le principe d'incertitude temps-fréquence de Gabor (1946) fournit une analogie formelle pour penser la dualité entre localisation temporelle et globale. *Note : l'intrication modélisée en V90 ne démontre pas, à elle seule, un étalement fréquentiel du Soi. Une telle démonstration exigerait le calcul explicite des distributions temporelles et spectrales correspondantes.*

## 🧠 Synthèse épistémologique : Modèle cognitif et contraintes computationnelles

1. **Le statut de l'analogie** : L'architecture Transformer n'est pas un système quantique réel. Elle sert d'analogie heuristique entre traitement local et intégration globale.
2. **La cause des échecs de formalisation** : Les LLM souffrent de flatterie (*sycophancy*) et de dilution d'attention (*Lost in the Middle*).
3. **Le critère de scientificité** : Pour dépasser la métaphore, les concepts doivent être traduits en grandeurs mesurables, découplées du discours verbal.

### Applications concrètes

#### 1. Méthodologie de travail avec l'I.A.
* **Modularisation stricte** : Décomposer chaque étape en sous-problèmes algébriques isolés.
* **Validation par solveurs symboliques** : Exiger du code exécutable vérifiable (Python, `SymPy`, `QuTiP`).
* **Injonction de contradicteur formel** : Forcer le système à chercher les contre-exemples.

#### 2. Formalisation dans le cadre de l'IIT
Pour transposer l'intuition de la mémoire globale sans abus de langage quantique, on utilise un **proxy** inspiré de l'IIT (et non la définition axiomatique complète) :
* **Proxy d'intégration (\(\Phi\))** : 
  \[
 \Phi = D_{\mathrm{KL}}\left( p(X_{t} \mid X_{t-1}) \parallel \prod_{k} p(M_k^{(t)} \mid M_k^{(t-1)}) \right) 
\]
* **Métrique d'information de Fisher** : Géométrie de l'information sur les distributions statistiques.

## ⚠️ Limites explicites

* Aucun lien avec la conscience ni avec la phénoménalité n'est démontré de manière empirique.
* Aucune preuve que la Vacuité soit indépendante du substrat physique.
* Les tests V82 et V79 montrent des dépendances à l'histoire dans des cadres précis, pas une "durée vécue" bergsonienne.
* La valeur de l'asymptote (1/√2 ou 0.5) dépend du modèle et de la convention de fidélité.
* Les modèles V90 et V91 sont des expériences de pensée mathématiques (toy models), non des mesures de l'expérience subjective réelle.

## 🚀 Installation et exécution

```bash
pip install -r requirements.txt
pyth## 🚀 Installation et exécution

```bash
pip install -r requirements.txt
python v90_dissolution_soi.py
python v91_tsvf_codetermination.py
python v90_v91_coupled.py
python generate_figures.pyon v90_dissolution_soi.py
python v91_tsvf_codetermination.py
python v90_v91_coupled.py
python generate_figures.py
