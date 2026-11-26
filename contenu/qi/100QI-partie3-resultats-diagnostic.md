# 100QI-partie3-resultats-diagnostic

> Format : ✅ = bonne réponse. Modifier librement le texte, les tableaux, les ✅ et les corrections, puis reconvertir avec `md2txt.py` pour l'export SIDES.

## QI 51 (QRM)

Un essai randomisé compare un nouvel antiagrégant plaquettaire au clopidogrel après une angioplastie coronaire. Le tableau 2 présente les principaux résultats.

| Critère | HR [IC95%] | p |
|---|---|---|
| Critère de jugement principal : décès CV, infarctus ou AVC | 0,78 [0,65 – 0,94] | 0,008 |
| Thrombose de stent | 0,90 [0,76 – 1,07] | 0,23 |
| Hémorragie majeure | 1,25 [1,02 – 1,53] | 0,03 |

Il est vrai que :

**A.** Le nouvel antiagrégant réduit significativement le risque du critère de jugement principal ✅
> L'IC95% du HR est entièrement inférieur à 1, en cohérence avec p = 0,008.

**B.** Le risque de thrombose de stent est significativement réduit puisque le HR est inférieur à 1
> L'IC contient 1 (0,76 – 1,07) et p = 0,23 : la différence n'est pas significative.

**C.** Le nouvel antiagrégant augmente significativement le risque d'hémorragie majeure ✅
> L'IC est entièrement supérieur à 1 et p = 0,03.

**D.** Le HR du critère de jugement principal est significatif car il est compris entre les bornes de son intervalle de confiance
> Une estimation est toujours comprise dans son IC ; c'est la position de l'IC par rapport à 1 qui compte.

**E.** Un IC95% d'un HR qui contient 1 correspond à une valeur de p supérieure à 0,05 ✅
> Correspondance entre IC et test : pour un ratio, la valeur neutre est 1.

**Commentaire :** Piège d'annale visé : lecture d'un IC de ratio, cohérence IC / p, « significatif car compris dans son IC » (2024 EDN COVIT-TRIAL, 2026 EDN BEST-CLI, 2016 tests LIFE).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 52 (QRM)

Un essai randomisé en double aveugle compare la dexaméthasone à un placebo chez des adultes hospitalisés pour une pneumopathie communautaire. La mortalité à 30 jours est de 8 % dans le groupe dexaméthasone et de 12 % dans le groupe placebo. Il est vrai que :

**A.** La réduction absolue du risque de décès est de 4 points de pourcentage ✅
> 12 % − 8 % = 4 %.

**B.** Le nombre de patients à traiter pour éviter un décès est de 25 ✅
> NNT = 1 / réduction absolue = 1 / 0,04 = 25.

**C.** La réduction relative du risque de décès est d'environ 33 % ✅
> RR = 8 / 12 = 0,67 ; réduction relative = 1 − 0,67 = 0,33.

**D.** La réduction relative du risque est de 4 %
> 4 % est la réduction absolue ; la réduction relative rapporte cette différence au risque du groupe contrôle (4 / 12).

**E.** Si la mortalité du groupe placebo était de 3 %, la même réduction relative conduirait au même NNT
> À réduction relative égale, la réduction absolue serait de 1 point environ et le NNT d'environ 100 : le NNT dépend du risque de base.

**Commentaire :** Piège d'annale visé : réduction absolue et relative, NNT, influence du risque de base (2020 ECNi oxygène, 2017 complémentaires Göteborg, 2025 EDN albumine).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 53 (QRU)

Dans un essai randomisé de prévention, un vaccin contre le zona est associé à un risque relatif de zona de 0,25 [IC95% 0,18 – 0,35] par rapport à un placebo. Quelle est la proposition exacte ?

**A.** Le vaccin réduit le risque absolu de zona de 75 points de pourcentage
> 75 % est une réduction relative ; la réduction absolue dépend de l'incidence dans le groupe placebo.

**B.** Le vaccin réduit le risque relatif de zona de 75 % ✅
> Réduction relative = 1 − RR = 1 − 0,25 = 0,75.

**C.** Le vaccin réduit le risque de zona de 25 %
> C'est confondre RR et réduction relative.

**D.** 25 % des personnes vaccinées ont présenté un zona
> Le RR est un rapport de risques, pas un risque absolu.

**E.** Le résultat n'est pas significatif car l'intervalle de confiance est asymétrique
> L'IC d'un ratio est asymétrique par construction (échelle logarithmique) ; il exclut 1, le résultat est significatif.

**Commentaire :** Piège d'annale visé : RR, réduction relative et absolue, asymétrie de l'IC d'un ratio (2017 complémentaires Göteborg, 2020 ECNi oxygène).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 54 (QRM)

Un essai randomisé compare deux chimiothérapies (A et B) dans le cancer du pancréas métastatique. Le critère de jugement principal est la survie globale, estimée par la méthode de Kaplan-Meier et comparée par un test du log-rank (p = 0,002). Les probabilités de survie lues sur les courbes sont les suivantes.

| Temps depuis la randomisation | Survie, groupe A | Survie, groupe B |
|---|---|---|
| 6 mois | 80 % | 70 % |
| 12 mois | 62 % | 50 % |
| 18 mois | 50 % | 38 % |

Il est vrai que :

**A.** La médiane de survie est de 18 mois dans le groupe A ✅
> La médiane se lit au temps où la courbe passe à 50 %.

**B.** La médiane de survie est de 12 mois dans le groupe B ✅
> La survie du groupe B atteint 50 % à 12 mois.

**C.** 38 % des patients du groupe B sont décédés à 18 mois
> 38 % est la probabilité de survie ; la proportion estimée de décédés est de 62 %.

**D.** Le test du log-rank compare l'ensemble des deux courbes de survie ✅
> Il compare les survies sur toute la durée du suivi, pas à un temps donné.

**E.** La courbe de survie du groupe A décroît en partie du fait des patients perdus de vue
> La courbe ne décroît qu'aux décès ; les perdus de vue sont censurés.

**Commentaire :** Piège d'annale visé : lecture des courbes de Kaplan-Meier, médiane de survie, log-rank (2024 EDN COVIT-TRIAL, 2022 ECNi consultation pluridisciplinaire, 2016 tests LIFE).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 55 (QRM)

Un essai randomisé compare une chirurgie de revascularisation à un traitement médical optimal dans une cardiopathie ischémique. Les courbes de mortalité cumulée se croisent : la mortalité est plus élevée dans le groupe chirurgie pendant les 6 premiers mois (mortalité périopératoire), puis plus faible ensuite. Sur l'ensemble du suivi de 5 ans, le HR global est de 0,95 [IC95% 0,80 – 1,13]. Il est vrai que :

**A.** L'effet de la chirurgie varie au cours du temps ✅
> Le risque est d'abord plus élevé (période opératoire), puis plus faible.

**B.** L'hypothèse des risques proportionnels du modèle de Cox n'est pas respectée ✅
> Un HR constant suppose des risques proportionnels ; des courbes qui se croisent la contredisent.

**C.** Le HR global de 0,95 résume correctement l'effet de la chirurgie à tout moment du suivi
> Il « moyenne » un excès de risque précoce et un bénéfice tardif : il ne décrit aucune des deux périodes.

**D.** Une analyse par période (avant et après 6 mois) est plus informative ✅
> Elle permet de décrire séparément le risque précoce et le bénéfice tardif.

**E.** L'absence de différence significative sur l'ensemble du suivi démontre que les deux stratégies sont équivalentes
> Absence de preuve n'est pas preuve d'absence, a fortiori quand l'effet change de sens au cours du temps.

**Commentaire :** Piège d'annale visé : HR non constant, risques non proportionnels, interaction avec le temps (2024 EDN COVIT-TRIAL, 2026 EDN BEST-CLI).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 56 (QRU)

Dans le tableau 1 d'une étude, la durée d'hospitalisation est décrite par : « 6 jours (4 ; 11), médiane (25e ; 75e percentile) ». Quelle est la proposition exacte ?

**A.** La durée moyenne d'hospitalisation est de 6 jours
> 6 jours est la médiane ; la moyenne serait plus élevée, car la distribution est asymétrique.

**B.** La moitié des patients ont été hospitalisés 6 jours ou moins ✅
> Définition de la médiane.

**C.** 75 % des patients ont été hospitalisés plus de 11 jours
> 25 % des patients ont été hospitalisés plus de 11 jours (11 est le 75e percentile).

**D.** L'écart-type de la durée d'hospitalisation est de 7 jours
> 7 jours (11 − 4) est l'intervalle interquartile, pas un écart-type.

**E.** La distribution de la durée d'hospitalisation est symétrique
> L'écart entre la médiane et le 75e percentile (5 jours) est plus grand qu'avec le 25e (2 jours) : distribution asymétrique à droite, d'où le choix de la médiane.

**Commentaire :** Piège d'annale visé : médiane et percentiles, variable asymétrique (2019 test antipsychotiques, 2021 ECNi pesticides, 2023 EDN COMIC).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 57 (QRM)

Une cohorte de 300 patients opérés d'une chirurgie cardiaque étudie l'association entre une anémie préopératoire et la survenue d'une insuffisance rénale aiguë postopératoire.

|  | Insuffisance rénale aiguë | Pas d'insuffisance rénale | Total |
|---|---|---|---|
| Anémie | 60 | 90 | 150 |
| Pas d'anémie | 30 | 120 | 150 |

Il est vrai que :

**A.** Le risque relatif d'insuffisance rénale aiguë associé à l'anémie est de 2,0 ✅
> (60/150) / (30/150) = 0,40 / 0,20 = 2,0.

**B.** L'odds ratio associé à l'anémie est d'environ 2,7 ✅
> (60 × 120) / (90 × 30) = 7 200 / 2 700 = 2,67.

**C.** L'odds ratio surestime ici le risque relatif parce que l'événement est fréquent ✅
> Avec 30 % d'événements, l'OR s'éloigne du RR ; ils ne sont proches que pour un événement rare.

**D.** Dans une cohorte, le risque relatif est directement estimable ✅
> Les incidences sont mesurées dans chaque groupe : le RR est la mesure naturelle.

**E.** L'odds ratio et le risque relatif sont toujours égaux quand l'étude est une cohorte
> Leur proximité dépend de la fréquence de l'événement, pas du schéma d'étude.

**Commentaire :** Piège d'annale visé : calcul du RR et de l'OR, l'OR surestime le RR quand l'événement est fréquent (2023 EDN COMIC, 2016 tests fluorose, 2022 test CRP).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 58 (QRM)

Un essai randomisé de 20 000 patients hypertendus compare une nouvelle association fixe d'antihypertenseurs à l'association de référence. Le critère de jugement principal est la pression artérielle systolique à 1 an. La différence moyenne est de −1,2 mmHg [IC95% −1,8 ; −0,6], p < 0,001. Il est vrai que :

**A.** La différence est statistiquement significative ✅
> L'IC de la différence exclut 0.

**B.** Une baisse de 1,2 mmHg est probablement peu pertinente sur le plan clinique ✅
> Une différence aussi faible a peu d'impact attendu sur les événements cardiovasculaires.

**C.** Une différence statistiquement significative est forcément cliniquement pertinente
> Avec un très grand effectif, une différence minime devient significative : significativité et pertinence clinique sont deux questions distinctes.

**D.** La très petite valeur de p traduit l'importance de l'effet du traitement
> La valeur de p dépend aussi de l'effectif ; elle ne mesure pas l'ampleur de l'effet.

**E.** L'étroitesse de l'intervalle de confiance s'explique par le grand effectif de l'essai ✅
> La précision de l'estimation augmente avec l'effectif.

**Commentaire :** Piège d'annale visé : significativité statistique contre pertinence clinique, p et taille d'effet (2024 ECNi marche active, 2023 ECNi FAIT).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 59 (QRU)

Un essai randomisé de 80 patients compare deux techniques d'anesthésie locorégionale. La survenue d'une douleur sévère à H24 donne un RR de 0,60 [IC95% 0,25 – 1,45]. Quelle est la proposition exacte ?

**A.** L'essai démontre l'absence de différence entre les deux techniques
> L'IC est compatible avec une réduction de 75 % comme avec une augmentation de 45 %.

**B.** La largeur de l'intervalle de confiance traduit un effectif faible et donc une estimation imprécise ✅
> Peu de patients et peu d'événements : estimation très imprécise.

**C.** Le résultat est significatif car le RR est inférieur à 1
> L'IC contient 1 : non significatif.

**D.** Le résultat serait significatif en différence absolue de risque
> Mesure relative et mesure absolue concluent de la même façon.

**E.** Un IC large traduit un biais de mesure
> La largeur de l'IC reflète l'imprécision (fluctuations d'échantillonnage), pas un biais.

**Commentaire :** Piège d'annale visé : largeur de l'IC, absence de preuve, ratio contre différence (2020 ECNi oxygène, 2023 test ASPIRE).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 60 (QRM)

Le tableau 1 d'une étude sur les patients hospitalisés pour une pancréatite aiguë présente les caractéristiques suivantes, chez 400 patients.

| Caractéristique | Valeur |
|---|---|
| Âge, moyenne (écart-type), ans | 58 (16) |
| Hommes, n (%) | 236 (59) |
| CRP à l'admission, médiane (25e ; 75e percentile), mg/l | 85 (30 ; 190) |
| Pancréatite biliaire, n (%) | 168 (42) |

Il est vrai que :

**A.** La CRP est décrite par une médiane parce que sa distribution est asymétrique ✅
> Quelques valeurs très élevées tireraient la moyenne vers le haut ; la médiane est plus représentative.

**B.** Un quart des patients avaient une CRP supérieure à 190 mg/l à l'admission ✅
> 190 mg/l est le 75e percentile.

**C.** La moitié des patients avaient une CRP comprise entre 30 et 190 mg/l ✅
> L'intervalle interquartile contient les 50 % de valeurs centrales.

**D.** Les patients avaient en moyenne entre 42 et 74 ans
> 58 ± 16 décrit la dispersion des âges individuels autour de la moyenne (environ deux tiers des patients si la distribution est normale), pas un intervalle pour la moyenne.

**E.** La proportion d'hommes est de 59 %, soit 236 patients ✅
> 236 / 400 = 0,59.

**Commentaire :** Piège d'annale visé : lecture du tableau 1, médiane et percentiles, écart-type contre IC (2019 test antipsychotiques, 2021 ECNi pesticides, 2023 EDN COMIC).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 61 (QRM)

Dans un essai randomisé comparant un anticoagulant à un placebo chez 2 000 patients, une hémorragie majeure survient chez 30/1 000 patients (3,0 %) du groupe anticoagulant et 15/1 000 (1,5 %) du groupe placebo, RR 2,0 [IC95% 1,1 – 3,7], p = 0,03. Il est vrai que :

**A.** L'anticoagulant double significativement le risque d'hémorragie majeure ✅
> RR 2,0 avec un IC qui exclut 1.

**B.** L'augmentation absolue du risque d'hémorragie majeure est de 1,5 point de pourcentage ✅
> 3,0 % − 1,5 % = 1,5 %.

**C.** Il faut traiter environ 67 patients pour provoquer une hémorragie majeure supplémentaire ✅
> Nombre de patients à traiter pour nuire (NNH) = 1 / 0,015 ≈ 67.

**D.** Le risque d'hémorragie majeure augmente de 100 points de pourcentage
> L'augmentation relative est de 100 % ; l'augmentation absolue est de 1,5 point.

**E.** Ce résultat serait non significatif s'il était exprimé en différence absolue de risque
> Ratio et différence concluent de la même façon sur les mêmes données.

**Commentaire :** Piège d'annale visé : RR, différence absolue, NNH sur un effet indésirable (2016 tests LIFE, 2022 test ticagrélor, 2021 test rivaroxaban).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 62 (QRM)

Un essai randomisé compare un programme d'activité physique adapté à des conseils simples chez des patients atteints de cancer du sein. Le critère de jugement principal est un score de qualité de vie (0 à 100) à 6 mois. Résultats : groupe activité, moyenne 51,5 [IC95% 48,5 – 54,5] ; groupe conseils, moyenne 46,0 [IC95% 43,0 – 49,0]. Différence 5,5 points [IC95% 1,3 – 9,7], p = 0,01. Il est vrai que :

**A.** La différence de qualité de vie entre les deux groupes est statistiquement significative ✅
> L'IC de la différence exclut 0.

**B.** Le chevauchement des intervalles de confiance des deux moyennes prouve l'absence de différence significative
> Deux IC individuels peuvent se chevaucher alors que l'IC de la différence exclut 0 ; seul l'IC de la différence (ou le test) permet de conclure.

**C.** C'est l'intervalle de confiance de la différence qui permet de conclure sur la comparaison ✅
> C'est lui qui teste la différence entre les groupes.

**D.** L'IC95% de la moyenne du groupe activité signifie que 95 % des patientes de ce groupe ont un score entre 48,5 et 54,5
> L'IC porte sur la moyenne, pas sur les valeurs individuelles (celles-ci sont décrites par l'écart-type).

**E.** Pour une différence de moyennes, la valeur neutre de l'intervalle de confiance est 1
> Pour une différence, la valeur neutre est 0 ; elle est de 1 pour un ratio.

**Commentaire :** Piège d'annale visé : chevauchement des IC, valeur neutre d'une différence, IC contre dispersion (2018 ECNi COLOR II, 2017 complémentaires calcanéum).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 63 (QRM)

Dans un essai randomisé, les auteurs présentent les résultats suivants pour le critère de jugement principal.

| Groupe | Randomisés | Analysés | Événements, n (%) |
|---|---|---|---|
| Traitement | 150 | 150 | 45 (35,0) |
| Contrôle | 150 | 148 | 60 (40,5) |

Les auteurs indiquent une analyse en intention de traiter. Il est vrai que :

**A.** Le pourcentage d'événements du groupe traitement est erroné ✅
> 45 / 150 = 30,0 %, et non 35,0 %.

**B.** Le pourcentage d'événements du groupe contrôle est cohérent avec les effectifs analysés ✅
> 60 / 148 = 40,5 %.

**C.** Le nombre de patients analysés dans le groupe contrôle n'est pas cohérent avec une analyse en intention de traiter stricte ✅
> En ITT stricte, les 150 randomisés devraient être analysés ; 2 patients manquent.

**D.** Une incohérence entre effectifs et pourcentages n'a pas d'importance si le résultat est significatif
> Les erreurs de présentation doivent être repérées : elles font douter de la fiabilité des données.

**E.** Le pourcentage d'événements se calcule en rapportant le nombre d'événements au nombre de patients randomisés, quelle que soit l'analyse choisie
> Il se calcule sur l'effectif analysé ; en ITT stricte, analysés et randomisés coïncident.

**Commentaire :** Piège d'annale visé : repérer les erreurs des auteurs (effectifs, pourcentages), cohérence avec l'ITT (2019 test antipsychotiques, 2022 ECNi ventilation au masque).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 64 (QRU)

Un essai randomisé montre qu'un traitement de maintenance réduit le risque de progression d'un myélome, avec un hazard ratio de 0,70 [IC95% 0,58 – 0,85] estimé par un modèle de Cox. Quelle est la proposition exacte ?

**A.** 30 % de patients en moins ont présenté une progression dans le groupe traité
> Le HR n'est pas un rapport de proportions observées à une date donnée.

**B.** La survie médiane sans progression est allongée de 30 %
> Le HR ne se traduit pas directement en gain de médiane.

**C.** À chaque instant du suivi, le risque instantané de progression est réduit d'environ 30 % chez les patients traités ✅
> Interprétation du HR sous l'hypothèse des risques proportionnels.

**D.** Le risque absolu de progression est réduit de 30 points de pourcentage
> Le HR est une mesure relative.

**E.** Le résultat n'est pas significatif car le HR est inférieur à 1
> L'IC exclut 1 : le résultat est significatif.

**Commentaire :** Piège d'annale visé : interprétation d'un hazard ratio (2022 ECNi consultation pluridisciplinaire, 2024 EDN COVIT-TRIAL, 2026 EDN BEST-CLI).

**Notion :** Lecture des résultats (mesures d'association, IC, p, tableaux, figures)

---

## QI 65 (QRM)

Un nouveau test sanguin de dépistage du cancer colorectal est évalué chez 1 000 personnes de 50 à 74 ans, toutes explorées par coloscopie (examen de référence).

|  | Cancer à la coloscopie | Pas de cancer | Total |
|---|---|---|---|
| Test + | 46 | 114 | 160 |
| Test − | 4 | 836 | 840 |
| Total | 50 | 950 | 1 000 |

Il est vrai que :

**A.** La sensibilité du test est de 92 % ✅
> Se = 46 / 50 = 92 %.

**B.** La valeur prédictive positive du test est d'environ 29 % ✅
> VPP = 46 / 160 = 28,75 %.

**C.** La valeur prédictive négative du test est supérieure à 99 % ✅
> VPN = 836 / 840 = 99,5 %.

**D.** Le taux de faux positifs du test est d'environ 71 %
> Le taux de faux positifs est FP / non-malades = 114 / 950 = 12 % (= 1 − Sp) ; 71 % est la proportion de faux positifs parmi les tests positifs (1 − VPP).

**E.** Une spécificité de 88 % signifie que 88 % des personnes ayant un test positif sont indemnes de cancer
> La spécificité est la proportion de tests négatifs chez les non-malades (836 / 950).

**Commentaire :** Piège d'annale visé : calculs Se, VPP, VPN, taux de faux positifs à partir d'un 2x2, faible prévalence (2019 ECNi épaule, 2024 EDN deep learning, 2018 ECNi endocan).

**Notion :** Études diagnostiques et pronostiques

---

## QI 66 (QRU)

On évalue une stratégie fondée sur un dosage unique de troponine ultrasensible à l'admission pour permettre la sortie rapide des urgences de patients consultant pour une douleur thoracique, en éliminant un infarctus du myocarde. Quelle est la proposition exacte ?

**A.** Le test doit avoir avant tout une spécificité élevée
> Une spécificité élevée sert à confirmer un diagnostic, pas à l'éliminer.

**B.** Le test doit avoir avant tout une sensibilité élevée, qui garantit peu de faux négatifs et une valeur prédictive négative élevée ✅
> Pour éliminer, il faut que très peu de malades aient un test négatif.

**C.** La valeur prédictive positive est le paramètre déterminant de cette stratégie
> La VPP sert à confirmer ; la question est ici de ne pas renvoyer à domicile un patient avec un infarctus.

**D.** La sensibilité dépend de la prévalence de l'infarctus aux urgences
> Se et Sp sont indépendantes de la prévalence (hors biais de spectre).

**E.** Un test très spécifique garantit une valeur prédictive négative élevée
> La VPN repose surtout sur la sensibilité (et sur une prévalence faible).

**Commentaire :** Piège d'annale visé : test d'exclusion, sensibilité et VPN (2019 ECNi épaule, 2018 ECNi endocan, 2021 test coroscanner).

**Notion :** Études diagnostiques et pronostiques

---

## QI 67 (QRM)

Une étude évalue la performance d'un test salivaire de dépistage d'une infection virale. Les auteurs ont recruté 100 patients hospitalisés pour une forme sévère confirmée et 100 volontaires sains asymptomatiques. Dans une seconde étude, chez des patients consultant en ville, seuls les patients dont le test salivaire était positif ont eu le test de référence. Il est vrai que :

**A.** Le recrutement de malades sévères et de volontaires sains expose à un biais de spectre ✅
> Les cas sévères sont faciles à détecter et les sujets sains faciles à classer négatifs : Se et Sp sont surestimées.

**B.** Les performances doivent être évaluées chez des patients consécutifs pour lesquels le diagnostic est suspecté en pratique ✅
> C'est la population dans laquelle le test sera utilisé.

**C.** La seconde étude expose à un biais de vérification ✅
> Les faux négatifs ne sont jamais identifiés, ce qui fausse l'estimation de la sensibilité.

**D.** Le biais de vérification n'a pas d'influence sur l'estimation de la sensibilité
> Ignorer les faux négatifs surestime la sensibilité.

**E.** La prévalence de 50 % dans la première étude rend la sensibilité inutilisable
> La sensibilité ne dépend pas de la prévalence ; c'est le choix des patients (spectre) qui pose problème.

**Commentaire :** Piège d'annale visé : biais de spectre, biais de vérification, série consécutive (2021 test coroscanner, 2024 EDN deep learning, 2019 ECNi épaule).

**Notion :** Études diagnostiques et pronostiques

---

## QI 68 (QRM)

Un score clinique de risque d'appendicite (0 à 50 points) est évalué chez 600 enfants consultant aux urgences pour une douleur abdominale ; l'examen de référence est l'histologie ou le suivi à 1 mois. Le tableau présente les performances pour plusieurs seuils.

| Seuil de positivité | Sensibilité | Spécificité |
|---|---|---|
| 10 ou plus | 98 % | 40 % |
| 20 ou plus | 90 % | 70 % |
| 30 ou plus | 80 % | 85 % |
| 40 ou plus | 60 % | 95 % |

Il est vrai que :

**A.** Le seuil de 30 ou plus maximise l'indice de Youden ✅
> Youden = Se + Sp − 1 : 0,38 ; 0,60 ; 0,65 ; 0,55. Maximum à 30.

**B.** Le seuil de 10 ou plus est le plus adapté pour éliminer une appendicite et éviter une imagerie ✅
> Avec 98 % de sensibilité, un score inférieur à 10 laisse très peu de faux négatifs.

**C.** Élever le seuil de positivité augmente la spécificité au prix d'une baisse de la sensibilité ✅
> Moins de patients sont classés positifs : moins de faux positifs, mais plus de faux négatifs.

**D.** Sur la courbe ROC correspondante, la diagonale représente les performances de l'examen de référence
> La diagonale représente un test non informatif (Se = 1 − Sp à chaque seuil).

**E.** L'aire sous la courbe ROC dépend de la prévalence de l'appendicite dans l'échantillon
> La courbe et son aire sont construites à partir de Se et Sp, indépendantes de la prévalence.

**Commentaire :** Piège d'annale visé : choix d'un seuil, indice de Youden, courbe ROC (2018 ECNi endocan, 2024 EDN deep learning, 2023 test sevrage de dialyse).

**Notion :** Études diagnostiques et pronostiques

---

## QI 69 (QRM)

Une étude compare la saturation en oxygène mesurée par un nouvel oxymètre de pouls connecté à la saturation artérielle mesurée par gaz du sang, chez 300 patients de réanimation. Le coefficient de corrélation est r = 0,92 (p < 0,001). Selon la méthode de Bland et Altman, l'oxymètre surestime la saturation de 2,5 points en moyenne, avec des limites d'agrément de −3 à +8 points. Il est vrai que :

**A.** Une corrélation forte et significative ne signifie pas que les deux mesures concordent ✅
> Deux mesures peuvent varier ensemble tout en différant systématiquement.

**B.** La méthode de Bland et Altman évalue l'accord entre les deux mesures ✅
> Elle décrit le biais moyen et l'étendue des écarts individuels.

**C.** Des limites d'agrément de −3 à +8 points peuvent être jugées cliniquement inacceptables pour décider d'une oxygénothérapie ✅
> Une surestimation de 8 points peut faire méconnaître une hypoxémie.

**D.** La corrélation significative démontre que l'oxymètre peut remplacer les gaz du sang
> Corrélation n'est pas concordance : l'interchangeabilité se juge sur l'accord.

**E.** Un coefficient de 0,92 signifie que 92 % des mesures sont concordantes
> Le coefficient de corrélation mesure l'intensité de la liaison linéaire, pas une proportion de mesures concordantes.

**Commentaire :** Piège d'annale visé : corrélation contre concordance (2023 test sevrage de dialyse, 2019 ECNi épaule).

**Notion :** Études diagnostiques et pronostiques

---

## QI 70 (QRM)

Des auteurs développent un score prédisant la mortalité à 30 jours après une pneumopathie communautaire, à partir d'une base de 12 000 patients d'un réseau hospitalier. Le score est développé sur 80 % des patients et testé sur les 20 % restants, tirés au sort dans la même base (AUC 0,78). Il est vrai que :

**A.** La validation sur un échantillon tiré de la même base ne protège pas d'une estimation optimiste des performances ✅
> Les patients viennent des mêmes centres, des mêmes pratiques : seule une validation externe le permet.

**B.** Une validation externe, dans d'autres centres ou une autre population, est nécessaire avant une utilisation en pratique ✅
> Étape suivante classique dans l'évaluation d'un score ou d'un biomarqueur.

**C.** Il s'agit d'un score pronostique et non diagnostique ✅
> Il prédit un événement futur (décès à 30 jours), pas la présence actuelle d'une maladie.

**D.** Une AUC de 0,78 démontre que l'utilisation du score améliore la survie des patients
> Le bénéfice clinique se démontre par un essai comparant des décisions guidées ou non par le score.

**E.** Ce score peut remplacer les scores pronostiques existants
> Il faut d'abord montrer sa valeur ajoutée par rapport aux scores existants.

**Commentaire :** Piège d'annale visé : étapes de validation d'un biomarqueur ou d'un score, diagnostic contre pronostic (2018 ECNi endocan, 2023 test sevrage de dialyse, 2024 EDN deep learning).

**Notion :** Études diagnostiques et pronostiques

---

## QI 71 (QRU)

Une étude rapporte, chez 40 patients, une sensibilité de 95 % et une spécificité de 90 % pour une échographie pulmonaire dans le diagnostic de pneumothorax, par rapport au scanner. Quelle information manque principalement pour interpréter ces performances ? Quelle est la proposition exacte ?

**A.** La prévalence du pneumothorax dans l'échantillon
> Se et Sp ne dépendent pas de la prévalence ; elle serait utile pour les valeurs prédictives.

**B.** Les intervalles de confiance à 95 % de la sensibilité et de la spécificité ✅
> Sur 40 patients, l'imprécision est grande : l'IC permet de juger la fiabilité de l'estimation.

**C.** La valeur prédictive négative
> Elle découle des données mais n'aide pas à interpréter Se et Sp.

**D.** Les écarts-types de la sensibilité et de la spécificité
> Pour une proportion, on donne un IC.

**E.** Une valeur de p
> Il n'y a pas de test d'hypothèse à faire sur une sensibilité.

**Commentaire :** Piège d'annale visé : « il manque la prévalence / la VPN » contre « il manque les IC » (2019 ECNi épaule, 2018 ECNi endocan).

**Notion :** Études diagnostiques et pronostiques

---

## QI 72 (QRU)

Un test de dépistage a une sensibilité de 90 % et une spécificité de 95 %. Il est proposé dans une population où la prévalence de la maladie est de 2 %. Quelle est la valeur prédictive positive du test dans cette population ? Quelle est la proposition exacte ?

**A.** 90 %
> C'est la sensibilité.

**B.** 95 %
> C'est la spécificité.

**C.** Environ 27 % ✅
> Pour 10 000 personnes : 200 malades dont 180 VP ; 9 800 non-malades dont 490 FP. VPP = 180 / 670 = 26,9 %.

**D.** Environ 67 %
> C'est la VPP pour une prévalence de 10 %.

**E.** Environ 99,8 %
> C'est la VPN dans cette population.

**Commentaire :** Piège d'annale visé : calcul d'une VPP selon la prévalence, faible VPP d'un dépistage (2019 ECNi épaule, 2024 EDN deep learning, 2017 complémentaires Göteborg).

**Notion :** Études diagnostiques et pronostiques

---
