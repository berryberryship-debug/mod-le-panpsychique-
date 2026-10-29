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
* **V94 (Forçage vs Coévolution)** : Oscillateurs de Stuart-Landau couplés. *Script* : `v94_forced_vs_coupled.py`. *Critère* : Observation de l'intermodulation et de la modification du spectre lent.

### Couche hybride (Champ-Qubit) : Validation et Énergétique
* **V136.11 à V136.12 (Moteur de référence)** : Modèle discret sur anneau (tight-binding) couplé à un qubit localisé.
    * *Critère de covariance* : Vérifiée numériquement (écart ~ \(10^{-15}\)).
    * *Critère de conservation* : Le modèle A (rétroaction bidirectionnelle) conserve l'énergie à l'erreur du solveur. Le modèle D (unidirectionnel) est un système ouvert non conservatif ; il sert uniquement de test causal pour prouver l'importance de la rétroaction.
* **V132.8 à V132.10 (Énergétique du couplage)** : Balayage de l'intensité \(g\).
    * *Activité* : L'activité cumulée du champ augmente fortement avec \(g\).
    * *Loi d'échelle* : Un ajustement descriptif (sur 7 points enregistrés) donne \(A(g) \approx 4.325 g^{2.096}\). L'exposant est sensible au point à \(g=5\) (passe à ~2.46 si on l'enlève), il ne s'agit donc pas d'une loi universelle.
    * *Bilan* : Le gain net du qubit est non monotone (négatif à \(g=3\), positif à \(g=5\)).

## 🖼️ Figures

![Résultat V89 - Fidélité de Bures](Meta_AI_v89_bures_pro_20261026.png)
*(Figure V89 : Évolution de la pureté, de la fidélité et de l'angle de Bures)*

![Résultat V88 - Balayage d'Uhlmann](Meta_AI_v88_uhlmann_pro_2026102.png)
*(Figure V88 : Trace d'Uhlmann et convergence vers l'asymptote)*

## 🧠 Synthèse philosophique et épistémologique

### 1. L'hologramme, le Rêve et Bachelard
Le "Soi" de la vie éveillée est une Plénitude locale. Le rêve lucide opère une transition où la conscience réalise sa nature de projection générée par une Vacuité informationnelle sous-jacente. Cette idée résonne métaphoriquement avec la *Philosophie du non* de Gaston Bachelard. **Cette résonance est métaphorique**.

### 2. Co-détermination temporelle (TSVF)
Dans le formalisme TSVF, l'état du Soi au présent est décrit par l'interférence entre une pré-sélection (passé) et une post-sélection (futur). **Le TSVF est mathématiquement équivalent à la mécanique quantique standard ; son interprétation rétrocausale est une lecture philosophique contestée.**

### 3. L'hypothèse du "Malaise" (V132)
L'augmentation de l'activité énergétique avec le couplage \(g\) offre une résonance formelle avec l'idée freudienne du *Malaise dans la civilisation*. **Il s'agit d'une analogie heuristique.** Les simulations ne démontrent ni un mécanisme psychologique, ni une loi sociologique.

## ⚠️ Limites explicites

* Aucun lien avec la conscience n'est démontré de manière empirique.
* La valeur de l'asymptote (1/√2) dépend du modèle.
* Les modèles V90, V91, V96-V98 sont des expériences de pensée mathématiques (toy models).
* Les résultats V132-V136 valident des propriétés numériques du système implémenté. L'interprétation en termes de "Ça", "Surmoi" et "Malaise" relève de l'hypothèse philosophique.
* L'ajustement en loi de puissance V132.9 est descriptif et basé sur 7 points enregistrés.

## 🚀 Installation et exécution

```bash
pip install -r requirements.txt
python v90_dissolution_soi.py
python v91_tsvf_codetermination.py
python v90_v91_coupled.py
python generate_figures.py📚 Références bibliographiques

### Bonnefond, M., & Jensen, O. (2015). Gamma activity coupled to alpha phase as a mechanism for top-down controlled gating. PLOS ONE, 10(6), e0128667. https://doi.org/10.1371/journal.pone.0128667
· Jensen, O., & Mazaheri, A. (2010). Shaping functional architecture by oscillatory alpha activity: Gating by inhibition. Frontiers in Human Neuroscience, 4, 186. https://doi.org/10.3389/fnhum.2010.00186
· Leith, E. N., & Upatnieks, J. (1962). Reconstructed Wavefronts and Communication Theory. Journal of the Optical Society of America, 52(10), 1123–1128. https://doi.org/10.1364/JOSA.52.001123

```
