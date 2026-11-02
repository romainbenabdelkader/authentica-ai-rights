# AUTHENTICA AI Rights & Origin Manifest

Statut : brouillon public.

[English documentation](README.en.md)

AUTHENTICA AI Rights & Origin Manifest est un profil JSON-LD ouvert pour declarer l'origine d'un contenu, la reserve de droits, le TDM opt-out et les restrictions d'entrainement IA associees a une oeuvre ou un actif numerique.

Ce depot publie uniquement les composants ouverts du manifeste :

- contexte JSON-LD
- schema JSON
- exemples machine-readable
- regles minimales de validation

AUTHENTICA n'est pas un systeme de surveillance, de sanction automatique, de DRM, de watermarking ou de decision juridique automatique.

## Architecture

Les roles sont separes:

- AURA definit des declarations d'origine signees et des preuves d'integrite des fichiers. Ses schemas exigent `aura_uid`, mais aucun identifiant institutionnel ni UID_AUTH. La verification locale ne depend pas d'AUTHENTICA.
- UID_AUTH definit un format d'identifiant declare pour l'oeuvre ou l'actif. Le schema de ce depot exige le champ `uid_auth` ; cette exigence ne s'etend pas au socle AURA.
- AUTHENTICA fournit le profil de droits et de reserve IA/TDM. C'est le role de ce depot: definir le contexte, le schema, les exemples et les regles minimales de validation du manifeste.

AUTHENTICA peut utiliser UID_AUTH comme identifiant et des concepts compatibles avec AURA pour la preuve technique, mais AUTHENTICA ne controle pas AURA, AURA ne depend pas d'AUTHENTICA, et UID_AUTH reste un standard d'identification distinct.

Ce document JSON-LD n'est pas, a lui seul, un manifeste AURA signe. Les schemas
UID_AUTH et AUTHENTICA utilisent des vocabulaires et contraintes differents.
Voir les [limites de compatibilite et les versions publiees](ARCHITECTURE.md).
Les exemples ne constituent pas un test d'interoperabilite entre ces formats.

Aucune plateforme proprietaire, fournisseur, modele IA, hebergeur de depot, assistant logiciel ou service commercial n'est requis pour lire, creer, verifier ou auditer les manifestes publies dans ce depot.

## Ce que le manifeste peut declarer

Un manifeste AUTHENTICA peut contenir :

- `uid_auth` : identifiant stable de l'oeuvre ou de l'actif
- `name` : titre ou nom public
- `creator` : createur, pseudonyme, institution ou valeur `Anonymous`
- `origin` : declaration d'origine, par exemple `human`, `ai`, `hybrid` ou `unknown`
- `issued_at` : date d'emission en ISO-8601
- `issuer` : entite declarant ou emettant le manifeste
- `rights.ai_training` : permission ou interdiction declaree pour l'entrainement IA
- `rights.tdm_opt_out` : signal de reserve TDM
- `hash` : empreinte d'integrite du fichier ou de l'actif reference

## Ce que le manifeste ne prouve pas

Le manifeste ne prouve pas a lui seul :

- la titularite juridique
- la validite du droit d'auteur
- une infraction
- une responsabilite
- l'utilisation effective d'une oeuvre par un systeme IA
- la qualite de createur au sens juridique

AUTHENTICA fournit un artefact technique verifiable. La loi, l'audit, le regulateur ou le juge decident des qualifications juridiques.

## RGPD et minimisation

Le profil est concu pour fonctionner sans donnee personnelle obligatoire.

Les implementations devraient privilegier :

- `Anonymous`, un pseudonyme ou un identifiant institutionnel lorsque c'est suffisant
- les hash cryptographiques plutot que le contenu integre
- les declarations minimales utiles
- l'absence de suivi comportemental ou de journalisation d'usage non necessaire

Si une implementation ajoute des donnees personnelles ou relie un manifeste a une personne identifiable, cette implementation reste responsable de sa base legale, de l'information des personnes, des durees de conservation et des droits RGPD.

## Exemple minimal

Exemple de structure uniquement : `EXAMPLE-AUDIO-HASH` et les valeurs
`EXAMPLE-...` des fichiers sous `examples/` sont des valeurs fictives, pas des
empreintes cryptographiques. Aucun actif correspondant ni signature AURA n'est
fourni. Le schema accepte ces chaines ; leur validation ne prouve aucune integrite.

```json
{
  "@context": "https://raw.githubusercontent.com/romainbenabdelkader/authentica-ai-rights/main/manifest/manifest-v1.jsonld",
  "@type": "CreativeWork",
  "uid_auth": "FR-2025-AUTH-MUS-000001",
  "name": "Example Audio Track",
  "creator": "Anonymous",
  "origin": "human",
  "issued_at": "2025-11-11T00:40:07Z",
  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  },
  "rights": {
    "ai_training": "prohibited",
    "tdm_opt_out": true
  },
  "hash": {
    "algorithm": "sha256",
    "value": "EXAMPLE-AUDIO-HASH"
  }
}
```

## Validation locale

```bash
python3 -m pip install 'jsonschema>=4,<5'
python3 scripts/validate_examples.py
```

La validation controle la structure declaree avec `manifest/schema.json` et la
bibliotheque requise `jsonschema`, sans activer de controle supplementaire des
formats de dates ou d'URI. Si la bibliotheque ne peut pas etre importee, le
script s'arrete avec le code 2 et ne valide aucun exemple. Il renvoie 0 si tous
les exemples respectent le schema, ou 1 si un exemple est invalide. Il ne recalcule pas
les empreintes, ne verifie aucune signature et n'authentifie pas l'emetteur.

Tests de regression (dependance installee):

```bash
python3 -m unittest discover -s tests -v
```

## Composants non inclus

Ce depot ne contient pas de registre securise, de service de certification, de module de fingerprinting, de detection d'usage, de surveillance ou d'anti-contournement.

Des produits ou modules commerciaux peuvent exister separement, mais ils ne font pas partie du profil ouvert publie ici et ne sont pas requis pour lire ou implementer ce manifeste.

## Licence

Les fichiers publics de ce depot sont publies sous licence MIT. Voir `LICENSE`.
