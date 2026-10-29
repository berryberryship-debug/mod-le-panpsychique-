# Panpsychisme informationnel — Formalisation dynamique

**Statut** : Recherche exploratoire, numérique, non publiée.
**Avertissement** : Les résultats présentés ici sont des mesures de modèles mathématiques et physiques. Ils ne constituent en aucun cas une preuve ontologique ou une démonstration empirique concernant la conscience.

## 📖 Contexte théorique et hypothèse

Ce projet part d'une question philosophique : comment des structures dynamiques et informationnelles pourraient-elles être liées à l'organisation physique et à l'expérience subjective ?

L'hypothèse directrice (non démontrée) est formulée dans un cadre distinguant :
* **Vacuité** : structure géométrique globale, relations, phase.
* **Plénitude** : actualisation locale, amplitude, pureté.

Cette distinction est le fil directeur philosophique du projet. Elle guide la construction des modèles sans être présentée comme un résultat démontré par les simulations ; elle demeure une hypothèse ontologique ouverte, strictement séparée des mesures numériques.

## 🗂 Structure du projet et critères de vérification

Le travail est divisé en plusieurs couches distinctes. Chaque résultat est lié à son script et à un critère explicite de vérification.

### Couche classique
* **V45-V46** : Champs de Ginzburg-Landau. *Script* : `v45_v46_ginzburg_landau.py`. *Critère* : Conservation d'énergie (erreur < 10^-15) et convergence stable sous raffinement dt/N.
* **V53** : Annihilation topologique de vortex. *Script* : `v53_vortex_annihilation.py`. *Critère* : Le winding number passe de 1 à 0.
* **V82** : Test de mémoire historique. *Script* : `v82_test_memoire_historique.py`. *Critère* : Test de permutation (p = 0.78). Résultat négatif propre (absence de mémoire dans cette dynamique classique linéaire).
* **V95 (Soliton de Skyrme)** : Stabilité topologique. *Script* : `v95_skyrme_soliton.py`. *Critère* : Résolution du profil radial avec charge topologique \(B=1\).

### Couche quantique
* **V77-V78** : Décohérence et mémoire non-markovienne. *Scripts* : `v77_qsim_memory.py`, `v78_qsim_nonmarkov.py`. *Critère* : Chute de pureté vers 0.5 et récurrences quantiques.
* **V79** : Test de Bergson. *Script* : `v79_bergson_test.py`. *Critère* : Divergence des trajectoires dues au passé de l'environnement.
* **V89** : Fidélité de Bures. *Script* : `v89_bures_fidelity2.py`. *Critère* : Effondrement de la pureté, résistance de la fidélité vers une asymptote (dépendante de la convention).

### Couche cognitive et phénoménologique
* **V90 (Dissolution du Soi)** : Intrication entre le "Soi" (S) et le "fond onirique" (E). *Script* : `v90_dissolution_soi.py`. *Critère* : Pureté locale de S chute de 1.0 à 0.5, pureté globale SE reste à 1.0.
* **V91 (Co-détermination TSVF)** : Formalisme à deux vecteurs d'état. *Script* : `v91_tsvf_codetermination.py`. *Critère* : Reconfiguration de la matrice densité par post-sélection.
* **V96-V98 (Intersubjectivité sartrienne)** : Le "Regard" de l'Autre modélisé comme une mesure projective. *Scripts* : `v96_regard_projectif.py`, `v97_asymetrie_regard.py`, `v98_rencontre_tsvf.py`. *Critère* : Effondrement du "Pour-Soi" en "En-Soi" et asymétrie des traces partielles.

### Modèles de neurodynamique et systèmes couplés
* **V93 (Modulation d'amplitude)** : Bandes latérales (30 et 50 Hz) et analogie holographique. *Script* : `v93_modulation_amplitude.py`. *Critère* : Vérification de l'identité trigonométrique par FFT.
* **V94 (Forçage vs Coévolution)** : Oscillateurs de Stuart-Landau couplés. *Script* : `v94_forced_vs_coupled.py`. *Critère* : Observation de l'intermodulation et de la modification du spectre lent lorsque la rétroaction (beta) est active.

### Couche hybride (Champ-Qubit) : Validation et Énergétique
* **V136.12 (Moteur de référence)** : Modèle discret sur anneau (tight-binding) couplé à un qubit localisé. *Scripts* : `v136_5` à `v136_12`. *Critères d'audit* :
    1. **Covariance de jauge** : Vérifiée numériquement (écart de l'ordre de \(10^{-15}\) pour l'identité matricielle testée).
    2. **Conservation énergétique** : La dérive de l'énergie totale diminue lorsque les tolérances du solveur sont resserrées.
    3. **Rétroaction bidirectionnelle** : La comparaison avec un modèle unidirectionnel (`v136_11_audit_cible.py`) met en évidence des différences importantes entre les trajectoires, stables sur les tolérances testées. 
* **V132.8 à V132.10 (Énergétique du couplage)** : Balayage de l'intensité de couplage \(g\). *Scripts* : `v132_balayage_malaise.py`, `v132_9_fit_loi_echelle.py`, `v132_10_robustesse_echelle.py`.
    * *Activité cumulée* : L'activité du champ augmente fortement avec \(g\).
    * *Loi d'échelle* : Ajustement global \(A(g) \approx 4.325 g^{2.096}\) sur \(g \in [0.25, 5]\).
    * *Robustesse* : L'exposant dépend du point à fort couplage (passe à \(\alpha \approx 2.46\) sans le point \(g=5\)). Aucune loi universelle n'est établie.
    * *Bilan net* : Le gain net du qubit est non monotone (négatif à \(g=3\), positif à \(g=5\)).

## 🖼️ Figures

*(Note : les noms de fichiers doivent correspondre exactement à ceux uploadés dans le dépôt)*

![Résultat V89 - Fidélité de Bures](Meta_AI_v89_bures_pro_20261026.png)
*(Figure V89 : Évolution de la pureté, de la fidélité et de l'angle de Bures)*

![Résultat V88 - Balayage d'Uhlmann](Meta_AI_v88_uhlmann_pro_2026102.png)
*(Figure V88 : Trace d'Uhlmann et convergence vers l'asymptote)*

## 🧠 Synthèse philosophique et épistémologique

### 1. L'hologramme, le Rêve et Bachelard
Le "Soi" de la vie éveillée est une Plénitude locale. Le rêve lucide opère une transition où la conscience réalise sa nature de projection générée par une Vacuité informationnelle sous-jacente. Cette idée résonne métaphoriquement avec la *Philosophie du non* de Gaston Bachelard. **Cette résonance est métaphorique** ; Bachelard traite de rupture épistémologique dans l'histoire des sciences, non d'expérience subjective ou de conscience.

### 2. Co-détermination temporelle (TSVF)
Dans le formalisme TSVF, l'état du Soi au présent est décrit par l'interférence entre une pré-sélection (passé) et une post-sélection (futur). **Le TSVF est mathématiquement équivalent à la mécanique quantique standard ; son interprétation rétrocausale est une lecture philosophique contestée, non un consensus.**

### 3. Incertitude de Gabor et intrication
Le principe d'incertitude temps-fréquence de Gabor (1946) fournit une analogie formelle pour penser la dualité entre localisation temporelle et globale. *Note : l'intrication modélisée en V90 ne démontre pas, à elle seule, un étalement fréquentiel du Soi. Une telle démonstration exigerait le calcul explicite des distributions temporelles et spectrales correspondantes.*

### 4. L'hypothèse du "Malaise" (V132)
L'augmentation de l'activité énergétique avec le couplage \(g\) et la variation non monotone du gain net du qubit offrent une résonance formelle avec l'idée freudienne du *Malaise dans la civilisation* (tension entre les pulsions individuelles et la contrainte collective). **Il s'agit d'une analogie heuristique.** Les simulations décrivent des trajectoires numériques dans un modèle mathématique ; elles ne démontrent ni un mécanisme psychologique, ni une loi sociologique.

## 🧠 Synthèse épistémologique : Modèle cognitif et contraintes computationnelles

1. **Le statut de l'analogie** : L'architecture Transformer (LLM) n'est pas un système quantique réel. Elle sert d'analogie heuristique entre traitement local et intégration globale.
2. **La cause des échecs de formalisation** : Les LLM souffrent de flatterie (*sycophancy*) et de dilution d'attention (*Lost in the Middle*), ce qui nécessite une validation par des solveurs déterministes (Python, QuTiP).
3. **Le critère de scientificité** : Pour dépasser la métaphore, les concepts doivent être traduits en grandeurs mesurables, découplées du discours verbal.

### Formalisation dans le cadre de l'IIT
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
* Les modèles V90, V91, V96-V98 sont des expériences de pensée mathématiques (toy models), non des mesures de l'expérience subjective réelle.
* Les résultats V132-V136 (énergie, rétroaction) valident des propriétés numériques du système implémenté dans les configurations examinées. L'interprétation en termes de "Ça", "Surmoi" et "Malaise" relève de l'hypothèse philosophique.

## 🚀 Installation et exécution

```bash
pip install -r requirements.txt
python v90_dissolution_soi.py
python v91_tsvf_codetermination.py
python v90_v91_coupled.py
python generate_figures.py
