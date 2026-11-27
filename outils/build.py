"""Transforme les fichiers Markdown de contenu/ en JSON pour le site.

Usage : python outils/build.py          (depuis la racine du dépôt)

- contenu/qi/*.md  : séries de QI au format « ## QI n (QRM|QRU) », ✅ = bonne réponse,
                     correction en citation « > », « **Commentaire :** », « **Notion :** ».
- contenu/lca/*/sujet.md : épreuves LCA complètes (format « sujet corrigé de relecture »).
- contenu/notions.txt : ordre d'affichage des notions (une par ligne).

Le script s'arrête avec un message clair si un fichier est mal formé.
"""
import base64, json, re, sys, pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / 'contenu'
SORTIE = RACINE / 'site' / 'data'
erreurs, alertes = [], []


def slug(s):
    s = s.lower()
    for a, b in (('àâä', 'a'), ('éèêë', 'e'), ('îï', 'i'), ('ôö', 'o'), ('ùûü', 'u'), ('ç', 'c')):
        for c in a:
            s = s.replace(c, b)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def parse_bloc(lignes, ou):
    """Lit un bloc de question : énoncé, propositions A-E, corrections, commentaire, notion(s)."""
    enonce, props, commentaire, notions, piege = [], [], '', [], ''
    courante = None
    for l in lignes:
        s = l.rstrip()
        if s.strip() == '---':
            continue
        m = re.match(r'^\*\*([A-E])\.\*\*\s*(.*)$', s)
        if m:
            txt = m.group(2).strip()
            juste = '✅' in txt
            courante = {'lettre': m.group(1), 'texte': txt.replace('✅', '').strip(), 'juste': juste, 'correction': ''}
            props.append(courante)
            continue
        if s.startswith('>') and courante is not None:
            courante['correction'] = (courante['correction'] + '\n' + re.sub(r'^>\s?', '', s)).strip()
            continue
        m = re.match(r'^\*\*Commentaire\s*:\*\*\s*(.*)$', s)
        if m:
            commentaire = m.group(1).strip(); courante = None; continue
        m = re.match(r"^\*\*Piège d'annale visé\s*:\*\*\s*(.*)$", s)
        if m:
            piege = m.group(1).strip(); courante = None; continue
        m = re.match(r'^\*\*Notions?\s*:\*\*\s*(.*)$', s)
        if m:
            notions = [n.strip() for n in m.group(1).split(' ; ') if n.strip()]; courante = None; continue
        if courante is None:
            enonce.append(s)
        elif s.strip():
            # texte libre après les propositions : on le rattache à la correction en cours
            courante['correction'] = (courante['correction'] + '\n' + s).strip()
    texte = '\n'.join(enonce).strip()
    texte = re.sub(r'^Énoncé\s*:\s*', '', texte)
    if len(props) < 2:
        erreurs.append(f'{ou} : moins de 2 propositions trouvées')
    if not any(p['juste'] for p in props):
        erreurs.append(f'{ou} : aucune proposition marquée ✅')
    return {'enonce': texte, 'propositions': props, 'commentaire': commentaire or piege, 'notions': notions}


IMAGES = []  # (source, chemin publié)


def images(texte, dossier):
    """Accepte ![légende](chemin) ou « Image : chemin » ; copie l'image dans site/img/contenu/."""
    texte = re.sub(r'(?m)^Image\s*:\s*(\S+)\s*$', lambda m: f'![]({m.group(1)})', texte)
    def remplace(m):
        alt, chemin = m.group(1), m.group(2)
        if re.match(r'https?:', chemin):
            return m.group(0)
        source = (dossier / chemin).resolve()
        if not source.exists():
            erreurs.append(f'image introuvable : {chemin} (depuis {dossier.name})')
            return m.group(0)
        publie = 'img/contenu/' + source.relative_to(CONTENU).as_posix()
        IMAGES.append((source, publie))
        return f'![{alt}]({publie})'
    return re.sub(r'!\[([^\]]*)\]\(([^)\s]+)\)', remplace, texte)


def source(f, motif):
    """Chemin du fichier dans le dépôt et numéro de ligne du titre de la question (pour le mode enseignant)."""
    for k, l in enumerate(f.read_text(encoding='utf-8').split('\n'), 1):
        if re.match(motif, l):
            return {'fichier': f.relative_to(RACINE).as_posix(), 'ligne': k, 'titre': l.strip()}
    return {'fichier': f.relative_to(RACINE).as_posix(), 'ligne': 1, 'titre': ''}


def lire_qi():
    questions = []
    for f in sorted((CONTENU / 'qi').glob('*.md')):
        txt = images(f.read_text(encoding='utf-8'), f.parent)
        serie = f.stem
        titre = re.search(r'^# (.+)$', txt, re.M)
        blocs = re.split(r'(?m)^## ', txt)[1:]
        for b in blocs:
            lignes = b.split('\n')
            m = re.match(r'^QI\s+(\d+)\s*\((QRM|QRU)\)', lignes[0])
            if not m:
                alertes.append(f'{f.name} : titre ignoré « ## {lignes[0]} »'); continue
            num, typ = m.groups()
            ou = f'{f.name} QI {num}'
            q = parse_bloc(lignes[1:], ou)
            n_justes = sum(p['juste'] for p in q['propositions'])
            if typ == 'QRU' and n_justes != 1:
                erreurs.append(f'{ou} : QRU avec {n_justes} bonne(s) réponse(s)')
            if not q['notions']:
                alertes.append(f'{ou} : pas de ligne **Notion :** (classée « Non classée »)')
                q['notions'] = ['Non classée']
            q.update({'id': f'{slug(serie)}-{num}', 'serie': titre.group(1).strip() if titre else serie,
                      'numero': int(num), 'type': typ,
                      'src': source(f, rf'^## QI\s+{num}\b')})
            questions.append(q)
    return questions


def lire_lca():
    epreuves = []
    for f in sorted((CONTENU / 'lca').glob('*/sujet.md')):
        dossier = f.parent
        txt = images(f.read_text(encoding='utf-8'), dossier)
        meta = {}
        for cle in ('Titre de l\'article', 'Référence courte', 'Référence complète', 'Numéro de LCA',
                    'Lien vers l\'article', 'Article en libre accès'):
            m = re.search(r'^\*\*' + re.escape(cle) + r'\s*:\*\*\s*(.+)$', txt, re.M)
            meta[cle] = m.group(1).strip() if m else ''
        sections = re.split(r'(?m)^## ', txt)[1:]
        vignette, glossaire, annexes, questions = '', '', [], []
        for s in sections:
            titre, _, corps = s.partition('\n')
            t = titre.strip()
            if t.lower().startswith('vignette'):
                vignette = corps.strip()
            elif t.lower().startswith('glossaire'):
                glossaire = corps.strip()
            elif t.lower().startswith('annexe'):
                continue
            else:
                m = re.match(r'^Question\s+(\d+)\s*[–-]\s*(.*)$', t)
                if not m:
                    alertes.append(f'{f} : section ignorée « ## {t} »'); continue
                num, libelle = m.groups()
                lib = libelle.lower()
                typ = 'QRU' if 'unique' in lib else 'QRP' if 'précisé' in lib else 'QRM'
                ou = f'{dossier.name} question {num}'
                q = parse_bloc(corps.split('\n'), ou)
                n_justes = sum(p['juste'] for p in q['propositions'])
                if typ == 'QRU' and n_justes != 1:
                    erreurs.append(f'{ou} : QRU avec {n_justes} bonne(s) réponse(s)')
                q.update({'numero': int(num), 'type': typ, 'src': source(f, rf'^## Question\s+{num}\b')})
                questions.append(q)
        # annexes : fichiers annexe*.md du dossier, PDF publiés seulement s'ils sont dans le dossier
        for a in sorted(dossier.glob('annexe*.md')):
            num = re.sub(r'\D', '', a.stem) or ''
            annexes.append({'titre': f'Annexe {num}'.strip(), 'contenu': a.read_text(encoding='utf-8')})
        pdf = sorted(p.name for p in dossier.glob('*.pdf'))
        epreuves.append({
            'id': slug(dossier.name), 'dossier': dossier.name,
            'titre': meta["Titre de l'article"], 'reference': meta['Référence courte'],
            'reference_complete': meta['Référence complète'], 'lien': meta["Lien vers l'article"],
            'pdf': [f'contenu/lca/{dossier.name}/{p}' for p in pdf],
            'vignette': vignette, 'glossaire': glossaire, 'annexes': annexes, 'questions': questions,
        })
    return epreuves


CLE = b'cnet-lca'


def masquer(q):
    """Retire les réponses du texte clair : bonnes réponses, corrections et commentaire
    sont encodés (XOR + base64) et décodés par le site seulement après validation."""
    secret = {'j': [p['juste'] for p in q['propositions']],
              'c': [p['correction'] for p in q['propositions']],
              'm': q.pop('commentaire', '')}
    for p in q['propositions']:
        p.pop('juste'); p.pop('correction')
    brut = json.dumps(secret, ensure_ascii=False).encode('utf-8')
    q['x'] = base64.b64encode(bytes(b ^ CLE[i % len(CLE)] for i, b in enumerate(brut))).decode()
    return q


def main():
    ordre = [l.strip() for l in (CONTENU / 'notions.txt').read_text(encoding='utf-8').splitlines() if l.strip()]
    qi = lire_qi()
    lca = lire_lca()
    for q in qi:
        for n in q['notions']:
            if n not in ordre:
                alertes.append(f"{q['id']} : notion « {n} » absente de notions.txt (ajoutée en fin de liste)")
                ordre.append(n)
    utilisees = [n for n in ordre if any(n in q['notions'] for q in qi)]
    for a in alertes:
        print('ALERTE :', a)
    if erreurs:
        for e in erreurs:
            print('ERREUR :', e)
        sys.exit(1)
    qi = [masquer(q) for q in qi]
    for e in lca:
        e['questions'] = [masquer(q) for q in e['questions']]
    SORTIE.mkdir(parents=True, exist_ok=True)
    import shutil
    for source, publie in IMAGES:
        cible = RACINE / 'site' / publie
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, cible)
    (SORTIE / 'qi.json').write_text(json.dumps({'notions': utilisees, 'questions': qi}, ensure_ascii=False), encoding='utf-8')
    (SORTIE / 'lca.json').write_text(json.dumps({'epreuves': lca}, ensure_ascii=False), encoding='utf-8')
    print(f'OK : {len(qi)} QI sur {len(utilisees)} notions, {len(lca)} épreuve(s) LCA')


if __name__ == '__main__':
    main()
