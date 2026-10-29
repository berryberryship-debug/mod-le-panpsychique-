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
* **V45-V46** : Champs de Ginzburg-Landau. *Script* : `v45_v46_ginzburg_landau.py`. *Critère* : Suivi de l'énergie et étude de convergence sous raffinement de \(dt\) et de \(N\).
* **V53** : Annihilation topologique de vortex. *Script* : `v53_vortex_annihilation.py`. *Critère* : Le winding number passe de 1 à 0.
* **V82** : Test de mémoire historique. *Script* : `v82_test_memoire_historique.py`. *Critère* : Résultat négatif : le test de permutation (\(p = 0.78\)) ne met pas en évidence de dépendance historique détectable dans les conditions simulées.
* **V95 (Soliton de Skyrme)** : Stabilité topologique. *Script* : `v95_skyrme_soliton.py`. *Critère* : Résolution du profil radial avec charge topologique \(B=1\).

### Couche quantique
* **V77-V78** : Décohérence et mémoire non-markovienne. *Scripts* : `v77_qsim_memory.py`, `v78_qsim_nonmarkov.py`. *Critère* : Chute de pureté vers 0.5 (pour les paramètres simulés) et observation de récurrences quantiques.
* **V79** : Test de Bergson. *Script* : `v79_bergson_test.py`. *Critère* : Divergence des trajectoires dues au passé de l'environnement.
* **V89** : Fidélité de Bures. *Script* : `v89_bures_fidelity2.py`. *Critère* : Effondrement de la pureté, résistance de la fidélité vers une asymptote (dépendante de la convention).
* **V90 — Dissolution du Soi** : Intrication entre le "Soi" (S) et le "fond onirique" (E). *Script* : `v90_dissolution_soi.py`. *Critère* : Balayage paramétrique de l’intrication. Pour un état de Bell (\(\theta=\pi/4\)), la pureté locale de S vaut \(0.5\) et la pureté globale SE reste \(1.0\). *Assertions* : \(|P_S-0.5|<10^{-6}\) et \(|P_{SE}-1.0|<10^{-6}\).
* **V91 — Co-détermination TSVF** : Opérateur de transition non hermitien. *Script* : `v91_tsvf_codetermination.py`. *Critère* : Calcul de la valeur faible de \(\sigma_z\) (Aharonov, Albert et Vaidman, 1988). L'angle de post-sélection est choisi pour garantir un recouvrement faible mais non nul. *Assertions dynamiques* : le script vérifie le recouvrement, calcule la valeur faible, et assure que \(|A_w| > 1\) pour ce jeu de paramètres.

### Couche cognitive et phénoménologique
* **V96-V98 (Intersubjectivité sartrienne)** : Le "Regard" de l'Autre modélisé comme une mesure projective. *Scripts* : `v96_regard_projectif.py`, `v97_asymetrie_regard.py`, `v98_rencontre_tsvf.py`. *Critère* : Effondrement du "Pour-Soi" en "En-Soi" et asymétrie des traces partielles.

### Modèles de neurodynamique et systèmes couplés
* **V93 (Modulation d'amplitude)** : Bandes latérales (30 et 50 Hz) et analogie holographique. *Script* : `v93_modulation_amplitude.py`. *Critère* : Vérification de l'identité trigonométrique par FFT.
* **V94 (Forçage vs Coévolution)** : Oscillateurs de Stuart-Landau couplés. *Script* : `v94_forced_vs_coupled.py`. *Critère* : Observation de l'intermodulation et de la modification du spectre lent.

### Couche hybride (Champ-Qubit) : Validation et Énergétique
* **V136.11 — Comparaison des rétroactions** : *Script* : `v136_11_audit_cible.py`. *Critère* : Comparaison des trajectoires d’un modèle à rétroaction bidirectionnelle (A) et d’un modèle unidirectionnel (D). Un écart significatif indique une différence pour les paramètres testés. *Limite* : ce script n'est pas un test de covariance de jauge.
* **V136.12 — Bilan énergétique** : *Script* : `v136_12_energy_audit.py`. *Critère* : Vérification de la conservation pour le modèle fermé (A). Le script calcule \(\Delta E_{\max}\) et \(\Delta N_{\max}\) sur toute la trajectoire. *Assertions dynamiques* : le script lève une erreur si \(\Delta E_{\max} > 10^{-6}\) ou si \(\Delta N_{\max} > 10^{-6}\).
* **V132.8 à V132.10 (Énergétique du couplage)** : Balayage de l'intensité \(g\). *Activité* : Dans le balayage testé, l'activité cumulée du champ augmente avec \(g\). *Loi d'échelle* : Un ajustement descriptif sur 7 points donne \(A(g) \approx 4.325 g^{2.096}\), sensible au point à \(g=5\). Il ne s'agit pas d'une loi physique établie.

## 🖼️ Figures

*(Vérifier que les noms de fichiers ci-dessous correspondent exactement à ceux du dépôt)*

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
* La valeur asymptotique rapportée dépend de la convention de fidélité utilisée : fidélité racine (1/√2) ou fidélité au carré (0.5).
* Les modèles V90, V91, V96-V98 sont des expériences de pensée mathématiques (toy models).
* **Statut de validation** : Le document présente les critères, les limites et les assertions. Il ne fournit pas les sorties nécessaires pour confirmer que chaque test passe. La validation numérique ne sera achevée qu'après exécution des scripts complets, contrôle des sorties et reproduction des calculs.
* L'ajustement en loi de puissance V132.9 est descriptif et basé sur 7 points enregistrés.

## 🚀 Installation et exécution

Pour lancer les simulations, exécutez les commandes suivantes dans votre terminal (les fichiers doivent être présents à la racine du dépôt) :

pip install -r requirements.txt
python v90_dissolution_soi.py
python v91_tsvf_codetermination.py
python v90_v91_coupled.py
python generate_figures.py

## 📚 Références bibliographiques

*   Aharonov, Y., Albert, D. Z., & Vaidman, L. (1988). How the result of a measurement of a component of the spin of a spin-1/2 particle can turn out to be 100. *Physical Review Letters*, 60(14), 1351–1354. [https://doi.org/10.1103/PhysRevLett.60.1351](https://doi.org/10.1103/PhysRevLett.60.1351)
*   Bonnefond, M., & Jensen, O. (2015). Gamma activity coupled to alpha phase as a mechanism for top-down controlled gating. *PLOS ONE*, 10(6), e0128667. [https://doi.org/10.1371/journal.pone.0128667](https://doi.org/10.1371/journal.pone.0128667)
*   Jensen, O., & Mazaheri, A. (2010). Shaping functional architecture by oscillatory alpha activity: Gating by inhibition. *Frontiers in Human Neuroscience*, 4, 186. [https://doi.org/10.3389/fnhum.2010.00186](https://doi.org/10.3389/fnhum.2010.00186)
*   Leith, E. N., & Upatnieks, J. (1962). Reconstructed Wavefronts and Communication Theory. *Journal of the Optical Society of America*, 52(10), 1123–1128. [https://doi.org/10.1364/JOSA.52.001123](https://doi.org/10.1364/JOSA.52.001123)
