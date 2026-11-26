# 100QI-partie2-etudes-observationnelles

> Format : ✅ = bonne réponse. Modifier librement le texte, les tableaux, les ✅ et les corrections, puis reconvertir avec `md2txt.py` pour l'export SIDES.

## QI 26 (QRM)

Une cohorte prospective de 9 000 adultes de 65 ans et plus étudie l'association entre une activité physique régulière déclarée à l'inclusion et la survenue d'une démence sur 10 ans. Le RR brut est de 0,60 [IC95% 0,50 – 0,72]. Après ajustement sur l'âge, le sexe, le niveau d'études et les comorbidités cardiovasculaires, le RR ajusté est de 0,82 [IC95% 0,68 – 0,99]. Il est vrai que :

**A.** Une association entre activité physique et moindre risque de démence persiste après ajustement ✅
> Le RR ajusté reste inférieur à 1 avec un IC qui exclut 1.

**B.** Une partie de l'association brute s'explique par les facteurs pris en compte dans l'ajustement ✅
> Le RR passe de 0,60 à 0,82 : les sujets actifs sont plus jeunes, plus diplômés, moins malades, ce qui confondait l'association brute.

**C.** L'association ajustée démontre que l'activité physique protège de la démence
> Une étude observationnelle ne démontre pas la causalité ; l'ajustement renforce la réalité de l'association, pas son caractère causal.

**D.** Une confusion résiduelle par des facteurs non mesurés ou mal mesurés reste possible ✅
> Par exemple, une démence débutante qui réduit déjà l'activité (voir aussi la causalité inverse) ou des facteurs socio-économiques mal captés.

**E.** Il aurait fallu ajuster aussi sur la pression artérielle mesurée pendant le suivi, qui pourrait expliquer une partie de l'effet de l'activité physique
> Un facteur situé sur la chaîne causale (activité → pression artérielle → démence) ne doit pas être pris en compte comme facteur de confusion : on effacerait une partie de l'effet étudié.

**Commentaire :** Piège d'annale visé : brut / ajusté, confusion résiduelle, facteur intermédiaire, « ajustement = causalité » (2016 ECNi café, 2017 ECNi alopécie, 2022 test CRP).

**Notion :** Confusion, ajustement, appariement, score de propension

---

## QI 27 (QRM)

Une étude cas-témoins étudie l'association entre l'utilisation de fluoroquinolones et la survenue d'un anévrisme de l'aorte. Les cas sont les patients hospitalisés pour un premier anévrisme aortique ; pour chaque cas, 4 témoins sans anévrisme, vivants à la date du diagnostic du cas, sont appariés sur l'âge, le sexe et la région de résidence. Il est vrai que :

**A.** L'appariement sur l'âge et le sexe empêche d'étudier l'association entre ces facteurs et l'anévrisme ✅
> Par construction, cas et témoins ont la même répartition d'âge et de sexe.

**B.** Les témoins doivent être indemnes d'anévrisme et vivants à la date du diagnostic du cas ✅
> Ils doivent avoir pu devenir des cas au même moment (même période à risque).

**C.** Les auteurs auraient pu apparier aussi sur l'utilisation de fluoroquinolones pour améliorer la comparabilité
> On ne peut pas apparier sur l'exposition étudiée : son association avec la maladie deviendrait inestimable.

**D.** L'appariement impose une analyse adaptée aux données appariées (régression logistique conditionnelle) ✅
> L'analyse doit respecter la structure en groupes cas-témoins appariés.

**E.** L'appariement contrôle le biais de mémorisation
> L'appariement est une méthode de prise en compte de la confusion ; il n'agit pas sur la qualité du recueil de l'exposition.

**Commentaire :** Piège d'annale visé : appariement, « facteur d'appariement = exposition », appariement contre biais d'information (2016 ECNi café, 2020 test benzodiazépines, 2026 EDN IPP).

**Notion :** Confusion, ajustement, appariement, score de propension

---

## QI 28 (QRM)

Une étude observationnelle sur une base hospitalière compare la réhospitalisation à 1 an chez des patients ayant suivi, ou non, une réhabilitation respiratoire après une hospitalisation pour exacerbation de BPCO. Les groupes sont appariés sur un score de propension. Différence moyenne standardisée (standardised mean difference) : un seuil de 0,10 est retenu pour juger d'un déséquilibre. Tableau 1. Après appariement sur le score de propension

| Caractéristique | Réhabilitation (n = 1 100) | Pas de réhabilitation (n = 1 100) | Différence moyenne standardisée |
|---|---|---|---|
| Âge moyen (ans) | 68,4 | 68,9 | 0,03 |
| Femmes (%) | 30 | 31 | 0,02 |
| Diabète (%) | 41 | 33 | 0,17 |
| VEMS moyen (% de la théorique) | 46 | 45 | 0,06 |

Sur les 3 400 patients éligibles, 1 200 n'ont pas pu être appariés. Il est vrai que :

**A.** Après appariement, les deux groupes sont équilibrés sur l'âge, le sexe et le VEMS ✅
> Différences moyennes standardisées inférieures à 0,10.

**B.** Après appariement, un déséquilibre persiste pour le diabète ✅
> Différence moyenne standardisée de 0,17, au-dessus du seuil de 0,10 : un ajustement complémentaire sur le diabète serait souhaitable.

**C.** Une différence moyenne standardisée de 0,17 signifie que la différence de fréquence du diabète est statistiquement significative
> La différence moyenne standardisée mesure l'ampleur du déséquilibre, indépendamment de l'effectif ; elle ne s'interprète pas comme un p.

**D.** L'exclusion des patients non appariés peut limiter la représentativité des résultats ✅
> Plus d'un tiers des patients éligibles sont écartés : les résultats ne portent que sur les patients « appariables ».

**E.** L'appariement sur le score de propension prend en compte les facteurs de confusion non mesurés, comme la motivation du patient
> Le score n'est construit qu'avec les variables mesurées ; la motivation, non mesurée, reste un facteur de confusion résiduelle plausible.

**Commentaire :** Piège d'annale visé : lecture des différences moyennes standardisées après appariement, patients non appariés, confusion résiduelle (2025 EDN iSGLT2, 2023 ECNi adrénaline, 2022 ECNi consultation pluridisciplinaire).

**Notion :** Confusion, ajustement, appariement, score de propension

---

## QI 29 (QRU)

Une cohorte étudie l'association entre l'exposition professionnelle aux poussières de bois et le cancer des cavités nasales. Pour éviter la confusion par le tabagisme, les auteurs ont restreint l'étude aux sujets n'ayant jamais fumé. Quelle est la proposition exacte ?

**A.** La restriction aux non-fumeurs supprime la confusion par le tabagisme ✅
> Le tabac ne varie plus dans l'échantillon : il ne peut plus confondre l'association.

**B.** La restriction permet d'étudier l'effet du tabagisme sur le cancer des cavités nasales
> Le tabagisme ne varie plus : son effet n'est plus estimable.

**C.** La restriction améliore l'extrapolation des résultats à l'ensemble des travailleurs du bois
> Elle la limite : les résultats ne s'appliquent directement qu'aux non-fumeurs.

**D.** La restriction prend en compte les facteurs de confusion inconnus
> Elle ne concerne que le facteur restreint.

**E.** La restriction limite le biais de mémorisation
> Elle n'agit pas sur la qualité du recueil de l'exposition.

**Commentaire :** Piège d'annale visé : restriction comme méthode de prise en compte de la confusion (2017 ECNi alopécie, non-utilisateurs de finastéride ; 2016 ECNi café).

**Notion :** Confusion, ajustement, appariement, score de propension

---

## QI 30 (QRM)

Une étude cas-témoins étudie l'association entre l'exposition domestique au radon et le cancer bronchique. Les résultats sont présentés selon le statut tabagique.

| Population | OR ajusté sur l'âge et le sexe, radon élevé vs faible [IC95%] |
|---|---|
| Ensemble | 2,0 [1,7 – 2,4] |
| Non-fumeurs | 1,3 [1,0 – 1,7] |
| Fumeurs | 2,8 [2,2 – 3,6] |

Le test d'interaction est significatif (p < 0,001). Il est vrai que :

**A.** Il existe une interaction (modification d'effet) entre le radon et le tabagisme ✅
> L'association avec le radon est nettement plus forte chez les fumeurs, et le test d'interaction est significatif.

**B.** L'interaction est un biais qu'il faut corriger par ajustement sur le tabagisme
> La confusion est un biais à corriger ; l'interaction est une réalité à décrire.

**C.** Les résultats doivent être présentés séparément chez les fumeurs et les non-fumeurs ✅
> En cas d'interaction, un OR global masque l'hétérogénéité : on présente les OR par strate.

**D.** L'OR global suffit à résumer l'effet du radon dans cette population
> Il « moyenne » deux effets différents et ne correspond à aucune des deux strates.

**E.** Le tabagisme est un modificateur de l'effet du radon ✅
> Synonyme d'interaction : l'effet de l'exposition varie selon le niveau du tiers facteur.

**Commentaire :** Piège d'annale visé : confusion contre interaction, lecture d'un tableau stratifié (2018 test bariatrique, 2016 ECNi café, 2020 ECNi pancréas).

**Notion :** Confusion, ajustement, appariement, score de propension

---

## QI 31 (QRM)

Une cohorte de patients atteints de BPCO suivis 5 ans montre que la mortalité est plus élevée chez les patients sous oxygénothérapie de longue durée à domicile que chez ceux qui n'en reçoivent pas (HR brut 2,4 [IC95% 2,0 – 2,9]). Il est vrai que :

**A.** Ce résultat peut s'expliquer par une confusion par l'indication ✅
> L'oxygène est prescrit aux patients les plus graves (hypoxémie, insuffisance respiratoire chronique) : la gravité est liée à la fois au traitement et au décès.

**B.** La prise en compte de la sévérité de la maladie (VEMS, gaz du sang) peut réduire cette confusion ✅
> L'ajustement sur des marqueurs de sévérité réduit la confusion par indication, sans la supprimer totalement.

**C.** Ce résultat montre que l'oxygénothérapie de longue durée est délétère
> Une association brute, observationnelle et probablement confondue ne permet pas de conclure ; l'oxygène prolonge au contraire la survie dans les essais randomisés chez les hypoxémiques.

**D.** Seul un essai randomisé permet de s'affranchir complètement de la confusion par l'indication ✅
> La randomisation retire au médecin le choix du traitement et équilibre la gravité entre les groupes.

**E.** Cette confusion disparaîtrait si la cohorte comportait davantage de patients
> Un effectif plus grand réduit les fluctuations d'échantillonnage, pas les biais ni la confusion.

**Commentaire :** Piège d'annale visé : confusion par l'indication, limites de l'ajustement, « la taille corrige le biais » (2025 EDN iSGLT2, 2023 ECNi adrénaline, 2019 test antipsychotiques).

**Notion :** Confusion, ajustement, appariement, score de propension

---

## QI 32 (QRU)

Dans une étude cas-témoins sur l'association entre la consommation de boissons sucrées et la goutte, les auteurs écrivent : "We adjusted for body mass index because it differed significantly between cases and controls in our sample." Quelle est la proposition exacte ?

**A.** Un facteur est confondant dès que sa fréquence diffère significativement entre cas et témoins
> Ce constat a posteriori ne suffit pas : il faut que le facteur soit lié à l'exposition et à la maladie, sans être un intermédiaire.

**B.** Le choix des facteurs de confusion pris en compte doit être justifié a priori par les connaissances de la littérature ✅
> On identifie les facteurs de confusion avant l'analyse, à partir de ce qu'on sait de leurs liens avec l'exposition et la maladie.

**C.** Un ajustement sur l'indice de masse corporelle augmente la puissance de l'étude
> L'ajustement vise à réduire la confusion, pas à gagner en puissance.

**D.** L'ajustement sur l'indice de masse corporelle contrôle aussi les fluctuations d'échantillonnage
> Les fluctuations d'échantillonnage dépendent de l'effectif.

**E.** Si l'indice de masse corporelle est un intermédiaire entre boissons sucrées et goutte, l'ajustement est indispensable
> Ajuster sur un intermédiaire de la chaîne causale efface une partie de l'effet étudié.

**Commentaire :** Piège d'annale visé : choix a priori des facteurs de confusion, facteur intermédiaire (2021 ECNi pesticides, 2026 EDN IPP, 2020 ECNi pancréas).

**Notion :** Confusion, ajustement, appariement, score de propension

---

## QI 33 (QRM)

Une étude cas-témoins en population étudie les facteurs de risque du cancer du testicule. 400 cas, identifiés par un registre des cancers, sont comparés à 800 témoins tirés au sort dans les listes électorales de la même région. Plusieurs expositions sont étudiées : cryptorchidie, consommation de cannabis, exposition professionnelle aux pesticides. Il est vrai que :

**A.** Le schéma cas-témoins est adapté à l'étude d'une maladie rare ✅
> Il ne nécessite pas de suivre une très large population en attendant la survenue des cas.

**B.** Ce schéma permet d'étudier plusieurs expositions à la fois ✅
> Un avantage classique du cas-témoins, à condition que les hypothèses soient posées a priori.

**C.** Ce schéma permet d'estimer l'incidence du cancer du testicule chez les consommateurs de cannabis
> Le nombre de cas et de témoins est fixé par l'investigateur : on ne peut estimer que des odds ratios.

**D.** Le schéma cas-témoins est moins exposé aux biais que la cohorte
> Il est au contraire plus exposé aux biais de sélection (choix des témoins) et de mémorisation.

**E.** Le recrutement des témoins dans la même population source que les cas limite le biais de sélection ✅
> Les témoins doivent représenter l'exposition de la population d'où viennent les cas (ici la région couverte par le registre).

**Commentaire :** Piège d'annale visé : indications du cas-témoins, population source des témoins (2016 ECNi café, 2021 ECNi pesticides, 2017 ECNi SLA).

**Notion :** Cas-témoins et cohortes

---

## QI 34 (QRM)

Une étude cas-témoins hospitalière étudie l'association entre le tabagisme et le cancer de la vessie. Les cas sont les patients opérés d'un cancer de vessie dans un service d'urologie ; les témoins sont des patients hospitalisés dans le service de pneumologie du même hôpital, sans cancer de vessie. Il est vrai que :

**A.** Les témoins sont définis par l'absence de la maladie étudiée ✅
> Le statut cas/témoin dépend de la maladie, jamais de l'exposition.

**B.** Ce choix de témoins risque de surestimer la fréquence du tabagisme chez les témoins ✅
> Les patients de pneumologie fument plus que la population générale (BPCO, cancer bronchique).

**C.** Ce biais de sélection tend à sous-estimer l'association entre tabac et cancer de la vessie ✅
> Si les témoins sont plus exposés que la population source, l'OR est tiré vers 1.

**D.** Les témoins auraient dû être choisis parmi les non-fumeurs
> Les témoins ne sont jamais définis par l'exposition ; on ne pourrait plus calculer d'OR.

**E.** Le recours à des témoins hospitaliers supprime le biais de mémorisation
> Il le réduit parfois (témoins malades eux aussi), sans le supprimer, et il introduit un risque de biais de sélection.

**Commentaire :** Piège d'annale visé : choix des témoins, témoins hospitaliers, sens du biais (2016 ECNi café, 2020 ECNi pancréas, 2016 tests fluorose).

**Notion :** Cas-témoins et cohortes

---

## QI 35 (QRU)

Une étude cas-témoins sur 300 cas de syndrome de Guillain-Barré et 1 200 témoins retrouve une association avec une vaccination antigrippale dans les 6 semaines précédentes (OR ajusté 1,6, IC95% [1,1 – 2,3]). L'incidence du syndrome de Guillain-Barré est d'environ 2 pour 100 000 personnes par an. Quelle est la proposition exacte ?

**A.** Le risque relatif aurait été une mesure plus pertinente que l'OR dans cette étude
> Le RR n'est pas estimable dans un cas-témoins, car la proportion de cas est fixée par l'investigateur.

**B.** La maladie étant rare, l'OR est une bonne approximation du risque relatif ✅
> Quand l'événement est rare (moins de 10 %), OR et RR sont très proches.

**C.** Ce résultat signifie que 1,6 % des vaccinés développent un syndrome de Guillain-Barré
> L'OR est une mesure relative, pas un risque absolu ; le risque absolu reste de l'ordre de quelques cas par million.

**D.** Le choix de 4 témoins par cas permet de calculer un risque relatif
> Le nombre de témoins par cas n'y change rien ; il améliore seulement la puissance et la précision.

**E.** Ce résultat démontre que le vaccin provoque le syndrome de Guillain-Barré
> Association observationnelle : la causalité ne se déduit pas d'une seule étude.

**Commentaire :** Piège d'annale visé : OR contre RR en cas-témoins, maladie rare, nombre de témoins par cas (2016 ECNi café, 2016 tests fluorose, 2026 EDN IPP).

**Notion :** Cas-témoins et cohortes

---

## QI 36 (QRM)

Une étude cas-témoins étudie l'association entre un variant génétique et une forme rare de cardiomyopathie. Seuls 120 cas sont disponibles. Les auteurs décident de tirer au sort 4 témoins par cas au lieu d'un. Il est vrai que :

**A.** Le choix de 4 témoins par cas augmente la puissance de l'étude ✅
> Quand le nombre de cas est limité, augmenter les témoins est le seul moyen d'augmenter l'effectif.

**B.** Le choix de 4 témoins par cas améliore la précision de l'OR, avec un intervalle de confiance plus étroit ✅
> Plus d'information sur l'exposition dans la population source.

**C.** Au-delà de 4 témoins par cas, le gain de puissance devient faible ✅
> Le gain est rapidement décroissant : passer de 4 à 10 témoins par cas ajoute peu.

**D.** Le choix de plusieurs témoins par cas oblige à apparier les témoins aux cas
> Plusieurs témoins par cas peuvent être tirés au sort sans appariement.

**E.** Le choix de plusieurs témoins par cas permet d'estimer la prévalence du variant chez les malades
> La prévalence de l'exposition chez les malades est estimée à partir des cas, quel que soit le nombre de témoins.

**Commentaire :** Piège d'annale visé : plusieurs témoins par cas, puissance et précision (2021 ECNi pesticides, 2020 test benzodiazépines, 2022 test CRP).

**Notion :** Cas-témoins et cohortes

---

## QI 37 (QRM)

Une cohorte prospective suit 15 000 infirmières pendant 8 ans pour étudier l'association entre le travail posté de plus de 10 ans et la survenue d'un diabète de type 2. Le suivi total est de 40 000 personnes-années chez les exposées (120 cas de diabète) et de 50 000 personnes-années chez les non-exposées (80 cas). Il est vrai que :

**A.** Le taux d'incidence du diabète chez les exposées est de 3,0 pour 1 000 personnes-années ✅
> 120 / 40 000 = 0,003, soit 3,0 pour 1 000 personnes-années.

**B.** Le rapport des taux d'incidence entre exposées et non-exposées est d'environ 1,9 ✅
> Non-exposées : 80 / 50 000 = 1,6 pour 1 000 PA ; rapport 3,0 / 1,6 = 1,875.

**C.** Chaque infirmière contribue au nombre de personnes-années selon sa propre durée de suivi ✅
> Une infirmière diabétique au bout de 2 ans ou perdue de vue à 5 ans contribue 2 ou 5 années.

**D.** Ce schéma ne permet d'estimer qu'un odds ratio
> La cohorte permet d'estimer des incidences, donc des risques relatifs ou des rapports de taux.

**E.** Le nombre de personnes-années est égal au nombre de sujets multiplié par la durée maximale de suivi
> On additionne les durées de suivi individuelles (15 000 × 8 = 120 000 serait un maximum théorique, alors que le total observé est de 90 000).

**Commentaire :** Piège d'annale visé : cohorte, personnes-années, calcul d'incidence et de rapport de taux (2019 test antipsychotiques, 2024 ECNi conseil tabac, 2023 EDN COMIC).

**Notion :** Cas-témoins et cohortes

---

## QI 38 (QRM)

Une étude cas-témoins nichée dans une cohorte de 25 000 sujets ayant donné un échantillon sanguin congelé à l'inclusion étudie l'association entre le taux de vitamine D et le cancer colorectal. Pour chaque cas survenu pendant le suivi, 2 témoins sont tirés au sort parmi les sujets de la cohorte encore indemnes de cancer à la date du diagnostic du cas ; le dosage n'est réalisé que chez les cas et les témoins. Il est vrai que :

**A.** Le dosage réalisé sur un prélèvement antérieur au diagnostic respecte la séquence temporelle entre exposition et maladie ✅
> L'exposition est mesurée avant la maladie, comme dans une cohorte.

**B.** Ce schéma limite le nombre de dosages par rapport à une analyse de toute la cohorte ✅
> Seuls les cas et leurs témoins sont dosés : c'est l'intérêt économique du cas-témoins niché.

**C.** Les témoins doivent être indemnes de cancer au moment du diagnostic du cas ✅
> Échantillonnage sur la densité d'incidence : les témoins sont pris parmi les sujets à risque à ce moment-là.

**D.** Les témoins sont les sujets ayant un taux de vitamine D normal
> Les témoins sont définis par l'absence de la maladie, pas par l'exposition.

**E.** Ce schéma permet de calculer directement l'incidence du cancer chez les sujets carencés en vitamine D
> Seuls les cas et un échantillon de témoins sont analysés : on estime un OR, pas une incidence.

**Commentaire :** Piège d'annale visé : cas-témoins niché, séquence temporelle, définition des témoins (2022 test CRP, 2020 ECNi pancréas, 2016 tests fluorose).

**Notion :** Cas-témoins et cohortes

---

## QI 39 (QRM)

Une cohorte prospective de 120 000 adultes suivie 15 ans étudie l'association entre la consommation de viande transformée et le cancer colorectal. La consommation est mesurée à l'inclusion par un questionnaire alimentaire.

| Consommation (g/jour) | HR ajusté [IC95%] |
|---|---|
| Moins de 10 | 1 (référence) |
| 10 à 29 | 1,25 [1,05 – 1,49] |
| 30 à 49 | 1,60 [1,33 – 1,92] |
| 50 et plus | 2,10 [1,70 – 2,59] |

Le test de tendance est significatif (p < 0,001). Il est vrai que :

**A.** L'augmentation du risque avec la quantité consommée est un argument en faveur d'une relation causale ✅
> Relation dose-effet, confirmée par un test de tendance : critère de Bradford Hill.

**B.** Le recueil de l'exposition avant la survenue du cancer garantit la séquence temporelle ✅
> Dans une cohorte prospective, l'exposition précède la maladie.

**C.** L'ajustement sur les facteurs de confusion est un argument en faveur de la nature causale
> L'ajustement renforce la réalité de l'association (moins de confusion), il n'est pas un critère de causalité.

**D.** La mise en évidence d'un effet cancérogène des nitrites chez l'animal renforcerait l'hypothèse causale ✅
> Plausibilité biologique et preuve expérimentale sont des critères de Bradford Hill.

**E.** Ces résultats permettent d'affirmer que la viande transformée est une cause du cancer colorectal
> Une étude observationnelle seule ne permet pas d'affirmer la causalité ; elle s'inscrit dans un faisceau d'arguments.

**Commentaire :** Piège d'annale visé : critères de causalité, dose-effet, « l'ajustement est un argument de causalité » (2016 ECNi café, 2020 ECNi pancréas, 2021 ECNi pesticides).

**Notion :** Causalité, causalité inverse, temps immortel, dose-effet

---

## QI 40 (QRM)

Une cohorte de 6 000 sujets de plus de 70 ans montre que la perte de poids au cours des 2 années précédant l'inclusion est associée à la survenue d'une maladie d'Alzheimer (HR ajusté 1,8 [IC95% 1,4 – 2,3]). Dans une analyse complémentaire, l'association est forte pour les démences diagnostiquées dans les 3 premières années de suivi (HR 2,6) et disparaît au-delà (HR 1,05 [0,80 – 1,38]). Il est vrai que :

**A.** Ce résultat évoque une causalité inverse : la perte de poids pourrait être une conséquence de la maladie débutante ✅
> La démence évolue à bas bruit des années avant le diagnostic et peut entraîner une perte de poids.

**B.** Exclure les démences diagnostiquées dans les premières années de suivi (fenêtre de latence) limite ce biais ✅
> On ne garde que les cas survenus longtemps après la mesure de l'exposition.

**C.** L'ajustement multivarié corrige la causalité inverse
> Elle ne relève pas de la confusion : l'ajustement n'y change rien.

**D.** La disparition de l'association après 3 ans est en faveur d'un rôle causal de la perte de poids
> C'est l'inverse : une cause devrait encore se manifester à distance ; l'association limitée aux diagnostics proches évoque un marqueur préclinique.

**E.** Une association plus forte à proximité du diagnostic évoque un marqueur précoce de la maladie plutôt qu'une cause ✅
> Comme la CRP avant le cancer bronchique ou le diabète avant le cancer du pancréas.

**Commentaire :** Piège d'annale visé : causalité inverse, fenêtre de latence, marqueur préclinique (2022 test CRP, 2020 ECNi pancréas, 2026 EDN IPP).

**Notion :** Causalité, causalité inverse, temps immortel, dose-effet

---

## QI 41 (QRM)

Une étude sur base médico-administrative inclut les patients à leur sortie d'hospitalisation pour infarctus du myocarde. Sont considérés comme exposés ceux qui ont suivi une réadaptation cardiaque dans les 6 mois suivant la sortie ; les autres sont non exposés. Le suivi commence pour tous à la date de sortie. La mortalité à 2 ans est plus faible chez les exposés (HR ajusté 0,55 [IC95% 0,48 – 0,63]), avec un écart des courbes de survie dès le premier mois. Il est vrai que :

**A.** Cette définition de l'exposition expose à un biais de temps immortel ✅
> Pour être classé exposé, un patient doit survivre jusqu'à sa réadaptation : la période entre la sortie et la réadaptation est « immortelle » pour les exposés.

**B.** Un patient décédé 3 semaines après sa sortie, avant d'avoir pu commencer une réadaptation, est classé non exposé ✅
> Les décès précoces sont tous attribués au groupe non exposé, ce qui le défavorise.

**C.** Ce biais favorise artificiellement le groupe exposé ✅
> Il surestime le bénéfice apparent de la réadaptation.

**D.** L'ajustement sur les facteurs de confusion corrige le biais de temps immortel
> C'est un biais de définition de l'exposition dans le temps : il se corrige par l'analyse (exposition dépendante du temps, date repère), pas par l'ajustement.

**E.** L'écart des courbes dès le premier mois est un argument en faveur d'un effet réel de la réadaptation
> Un effet aussi précoce d'une intervention lente évoque plutôt un temps immortel ou une confusion résiduelle.

**Commentaire :** Piège d'annale visé : temps immortel, effet trop précoce (2023 EDN COMIC, 2022 ECNi consultation pluridisciplinaire).

**Notion :** Causalité, causalité inverse, temps immortel, dose-effet

---

## QI 42 (QRU)

Une étude cas-témoins sur base de médecine générale retrouve une association entre la prescription de sirops antitussifs dans les 6 mois précédents et le diagnostic d'un cancer bronchique (OR ajusté 3,2 [IC95% 2,6 – 3,9]). Quelle est la proposition exacte ?

**A.** Ce résultat suggère que les antitussifs favorisent le cancer bronchique
> L'interprétation causale est très peu plausible ici.

**B.** Ce résultat peut s'expliquer par la prescription d'antitussifs pour les premiers symptômes d'un cancer non encore diagnostiqué ✅
> Biais de causalité inverse (protopathique) : la toux révélatrice du cancer motive la prescription.

**C.** Ce biais aurait été corrigé par un ajustement sur le tabagisme
> L'ajustement prend en compte la confusion, pas le biais de causalité inverse (protopathique).

**D.** Ce biais est une erreur de classement non différentielle de l'exposition
> L'exposition est bien mesurée ; c'est son lien temporel avec la maladie qui est trompeur.

**E.** Ne retenir que les prescriptions récentes, dans le mois précédant le diagnostic, limiterait ce biais
> C'est l'inverse : il faut ignorer les expositions récentes (fenêtre de latence) et ne retenir que les expositions anciennes.

**Commentaire :** Piège d'annale visé : biais de causalité inverse, fenêtre de latence (2026 EDN IPP, 2020 test benzodiazépines, 2022 test CRP).

**Notion :** Causalité, causalité inverse, temps immortel, dose-effet

---

## QI 43 (QRU)

Dans une étude cas-témoins sur l'exposition professionnelle aux solvants chlorés et la maladie de Parkinson, les auteurs présentent les OR ajustés selon la durée d'exposition : moins de 5 ans 1,2 [IC95% 0,9 – 1,6] ; 5 à 15 ans 1,5 [1,1 – 2,0] ; plus de 15 ans 1,4 [1,02 – 1,92]. Ils écrivent dans la discussion : "We observed a clear dose-response relationship." Aucun test de tendance n'est présenté. Quelle est la proposition exacte ?

**A.** La relation dose-effet est démontrée puisque les OR des deux catégories les plus longues sont significatifs
> Une relation dose-effet suppose un risque qui augmente avec l'exposition ; ici il ne croît pas entre 5 à 15 ans et plus de 15 ans.

**B.** En l'absence de test de tendance et devant des OR qui ne croissent pas régulièrement, la relation dose-effet affirmée par les auteurs n'est pas établie ✅
> Les OR sont proches et leurs IC se recouvrent largement ; sans test de tendance, la phrase des auteurs n'est pas justifiée.

**C.** La spécificité de l'association est le principal argument en faveur de la nature causale dans cette étude
> La spécificité est un argument faible, rarement retenu.

**D.** La séquence temporelle est assurée puisque l'exposition professionnelle est ancienne
> Dans un cas-témoins, l'exposition est déclarée après la maladie : la chronologie est plus délicate à établir qu'en cohorte.

**E.** Une relation dose-effet démontrée suffirait à établir la causalité
> C'est un argument parmi d'autres, qui ne suffit pas seul.

**Commentaire :** Piège d'annale visé : « on observe un effet dose incontestable » sans test de tendance, séquence temporelle en cas-témoins (2021 ECNi pesticides, 2017 ECNi alopécie).

**Notion :** Causalité, causalité inverse, temps immortel, dose-effet

---

## QI 44 (QRM)

Une étude cas-témoins étudie l'association entre la prise d'anti-inflammatoires non stéroïdiens (AINS) pendant la grossesse et les malformations cardiaques. Les mères des enfants malformés (cas) et celles d'enfants sans malformation (témoins) sont interrogées par un enquêteur 6 mois à 2 ans après l'accouchement, à l'aide d'un questionnaire sur les médicaments pris pendant la grossesse. L'enquêteur connaît le statut de l'enfant. Il est vrai que :

**A.** Le recueil rétrospectif et déclaratif de l'exposition expose à un biais de mémorisation ✅
> Les prises ponctuelles d'AINS sont difficiles à se rappeler des mois plus tard.

**B.** Les mères d'enfants malformés ont tendance à rechercher davantage une cause et à mieux se souvenir de leurs prises médicamenteuses ✅
> Biais de mémorisation différentiel, classique dans les malformations congénitales.

**C.** Ce biais différentiel tend à surestimer l'OR ✅
> L'exposition est sur-déclarée chez les cas par rapport aux témoins.

**D.** La connaissance du statut de l'enfant par l'enquêteur réduit le biais d'information
> Elle l'aggrave : l'enquêteur peut insister davantage auprès des mères de cas.

**E.** Un ajustement multivarié élimine le biais de mémorisation
> Un biais d'information ne se corrige pas par l'ajustement ; il se prévient par le recueil (dossiers de prescription, délivrances).

**Commentaire :** Piège d'annale visé : biais de mémorisation différentiel, enquêteur non aveugle (2016 ECNi café, 2020 test benzodiazépines, 2021 ECNi pesticides).

**Notion :** Biais de sélection, d'information, de classement

---

## QI 45 (QRM)

Une étude cas-témoins étudie l'association entre l'exposition à la pollution atmosphérique (particules fines) et l'asthme de l'enfant. L'exposition est estimée par un modèle à partir de l'adresse du domicile, sans tenir compte du temps passé à l'école ou à l'extérieur. Cette imprécision est la même chez les cas et chez les témoins. Il est vrai que :

**A.** Il s'agit d'une erreur de classement non différentielle de l'exposition ✅
> L'erreur ne dépend pas du statut cas ou témoin.

**B.** Ce type d'erreur tend à rapprocher l'OR de 1 ✅
> Les groupes « exposés » et « non exposés » sont mélangés : l'association est atténuée.

**C.** Une erreur de classement non différentielle n'a pas d'influence sur l'OR
> Elle l'atténue (biais vers l'absence d'association).

**D.** Si une association significative est trouvée malgré cette imprécision, l'association réelle est probablement au moins aussi forte ✅
> L'erreur non différentielle sous-estime l'association : elle renforce la confiance dans une association positive.

**E.** L'appariement des témoins sur le quartier de résidence aurait corrigé cette erreur de mesure
> L'appariement prend en compte la confusion ; il ne corrige pas une erreur de mesure (et apparier sur le quartier rapprocherait l'exposition des cas et des témoins).

**Commentaire :** Piège d'annale visé : erreur de classement non différentielle, sens du biais (2021 ECNi pesticides, 2024 ECNi conseil tabac, 2017 ECNi alopécie).

**Notion :** Biais de sélection, d'information, de classement

---

## QI 46 (QRM)

Une cohorte construite à partir du SNDS (Système national des données de santé : base de l'Assurance maladie qui chaîne les remboursements de soins de ville, dont les délivrances de médicaments en pharmacie, et les hospitalisations du PMSI) compare le risque de fracture chez les utilisateurs de deux classes d'antidépresseurs. L'exposition est définie par les délivrances en pharmacie ; les fractures sont repérées par les diagnostics d'hospitalisation. Il est vrai que :

**A.** Un médicament délivré n'est pas forcément pris par le patient ✅
> Les données de délivrance ne renseignent pas l'observance réelle.

**B.** Les fractures prises en charge sans hospitalisation ne sont pas repérées ✅
> Seuls les diagnostics hospitaliers sont codés : sous-estimation, notamment des fractures périphériques.

**C.** Le nombre de patients très élevé permet de contrôler tous les facteurs de confusion
> La base ne contient pas certaines données (tabac, IMC, chutes, fragilité) : la confusion résiduelle persiste quel que soit l'effectif.

**D.** Une alerte de pharmacovigilance sur une des classes pendant la période d'étude peut modifier le profil des patients qui la reçoivent ✅
> Déplacement des prescriptions (biais de canalisation) : les patients à risque sont orientés vers l'autre classe.

**E.** L'utilisation d'une base médico-administrative supprime tout biais de sélection
> Elle limite certains biais de sélection (exhaustivité), mais pas les biais de mesure ni la confusion.

**Commentaire :** Piège d'annale visé : limites des bases médico-administratives, déplacement des prescriptions (biais de canalisation) (2025 EDN iSGLT2, 2024 ECNi conseil tabac, 2020 test benzodiazépines).

**Notion :** Biais de sélection, d'information, de classement

---

## QI 47 (QRU)

Une cohorte de 20 000 ouvriers de l'industrie chimique montre que leur mortalité toutes causes est inférieure de 20 % à celle de la population générale du même âge et du même sexe. Quelle est la proposition exacte ?

**A.** L'exposition aux produits chimiques protège contre la mortalité
> Conclusion causale non justifiée par une comparaison avec la population générale.

**B.** Ce résultat peut s'expliquer par un biais de sélection, les personnes en emploi étant en meilleure santé que la population générale ✅
> Effet du travailleur sain : la population générale inclut des personnes trop malades pour travailler.

**C.** Ce résultat s'explique par un biais de mémorisation
> La mortalité n'est pas déclarée par les sujets.

**D.** Ce résultat s'explique par une erreur de classement non différentielle de l'exposition
> Il n'y a pas d'erreur de mesure de l'exposition : c'est le groupe de comparaison qui n'est pas adapté.

**E.** Ce biais disparaîtrait avec un suivi plus long
> Il s'atténue un peu avec le temps mais ne disparaît pas ; la parade est un groupe de comparaison de travailleurs non exposés.

**Commentaire :** Piège d'annale visé : biais de sélection, choix du groupe de comparaison (2024 ECNi conseil tabac, 2016 tests fluorose, 2019 test antipsychotiques).

**Notion :** Biais de sélection, d'information, de classement

---

## QI 48 (QRM)

Une étude évalue la fréquence des troubles cognitifs après un séjour en réanimation. Les auteurs écrivent : "We used the national intensive care registry, which covers all French ICUs. Among the 85 000 eligible adults discharged alive in 2024, a random sample of 2 000 patients was invited to undergo cognitive testing at 1 year; 1 450 agreed." Il est vrai que :

**A.** Le registre national constitue la population source de l'étude ✅
> C'est la population dont sont issus les sujets.

**B.** Les 1 450 patients ayant accepté les tests constituent l'échantillon analysé ✅
> Ce sont les sujets réellement étudiés.

**C.** La population cible est celle à laquelle les auteurs souhaitent appliquer les résultats, par exemple les adultes survivant à un séjour en réanimation en France ✅
> Définition de la population cible.

**D.** Le tirage au sort dans un registre national garantit que les 1 450 patients analysés sont représentatifs de tous les survivants
> Les patients qui refusent (27,5 %) ont sans doute un profil cognitif différent : un biais de sélection reste possible.

**E.** Une étude en population, à partir d'un registre exhaustif, favorise la généralisation des résultats ✅
> La population source couvre l'ensemble des réanimations, ce qui améliore la validité externe.

**Commentaire :** Piège d'annale visé : population source, échantillon, population cible (2021 ECNi pesticides, 2019 test antipsychotiques, 2025 EDN iSGLT2).

**Notion :** Population, sélection, éligibilité

---

## QI 49 (QRM)

Un essai randomisé compare un anticoagulant oral à l'aspirine en prévention secondaire après un AVC ischémique d'origine indéterminée. Les critères de non-inclusion sont : insuffisance rénale sévère, antécédent d'hémorragie intracrânienne, indication formelle à une anticoagulation (fibrillation atriale connue). Seuls les patients avec au moins un facteur de risque supplémentaire de récidive (âge ≥ 75 ans, diabète, hypertension) sont inclus. Il est vrai que :

**A.** L'exclusion des patients ayant un antécédent d'hémorragie intracrânienne vise à les protéger d'un risque hémorragique ✅
> Les critères de non-inclusion visent surtout la sécurité des patients.

**B.** L'exclusion des patients ayant une fibrillation atriale connue s'explique par le fait que l'anticoagulation serait de toute façon indiquée ✅
> Il n'y a pas d'ambivalence (équipoise) : les randomiser dans le bras aspirine serait une perte de chance.

**C.** La sélection de patients à risque élevé de récidive augmente la fréquence du critère de jugement et donc la puissance ✅
> Plus d'événements attendus pour un même effectif.

**D.** La restriction à des patients à haut risque évite un biais de sélection
> Elle n'évite aucun biais ; elle cible la population d'intérêt et augmente la puissance, au prix de l'extrapolation.

**E.** Ces critères d'éligibilité limitent l'extrapolation des résultats aux patients à faible risque de récidive ✅
> Les résultats ne valent directement que pour la population étudiée.

**Commentaire :** Piège d'annale visé : justification des critères de non-inclusion, restriction et puissance, extrapolation (2025 EDN albumine, 2016 tests LIFE, 2021 test rivaroxaban).

**Notion :** Population, sélection, éligibilité

---

## QI 50 (QRU)

Un essai randomisé compare une stratégie transfusionnelle restrictive (seuil d'hémoglobine de 7 g/dl) à une stratégie libérale (seuil de 9 g/dl) chez des patients de réanimation. Les patients ayant une hémorragie active sont exclus. Quelle est la justification principale de cette exclusion ? Quelle est la proposition exacte ?

**A.** Limiter le biais de sélection
> Les critères d'éligibilité ne visent pas à limiter un biais.

**B.** Augmenter la comparabilité des deux groupes
> C'est le rôle de la randomisation.

**C.** Chez ces patients, la transfusion est indiquée quel que soit le taux d'hémoglobine : le seuil comparé n'aurait pas de sens et l'inclusion exposerait à une perte de chance ✅
> Pas d'ambivalence : le traitement serait de toute façon indiqué dans les deux bras.

**D.** Augmenter la validité externe de l'essai
> Exclure des patients limite plutôt la validité externe.

**E.** Diminuer le nombre de sujets nécessaire
> Ce n'est pas la justification de cette exclusion.

**Commentaire :** Piège d'annale visé : justification d'une non-inclusion (sécurité, éthique, ambivalence) plutôt que « limiter un biais » (2025 EDN albumine, remplissage dans le choc septique).

**Notion :** Population, sélection, éligibilité

---
