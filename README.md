# AUTHENTICA AI Rights & Origin Manifest

Statut : brouillon public.

AUTHENTICA AI Rights & Origin Manifest est un profil JSON-LD ouvert pour declarer l'origine d'un contenu, la reserve de droits, le TDM opt-out et les restrictions d'entrainement IA associees a une oeuvre ou un actif numerique.

Ce depot publie uniquement les composants ouverts du manifeste :

- contexte JSON-LD
- schema JSON
- exemples machine-readable
- regles minimales de validation

AUTHENTICA n'est pas un systeme de surveillance, de sanction automatique, de DRM, de watermarking ou de decision juridique automatique.

## Relation avec AURA

AURA et AUTHENTICA doivent rester separes.

- AURA est un standard ouvert, neutre et non capturable pour la preuve technique d'origine et d'integrite.
- AUTHENTICA est un profil applicatif possible pour declarer des droits, des restrictions IA et des signaux de reserve.

AUTHENTICA peut utiliser des concepts compatibles avec AURA, mais AUTHENTICA ne controle pas AURA et AURA ne depend pas d'AUTHENTICA.

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

```json
{
  "@context": "https://schema.authentica.org/manifest-v1.jsonld",
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
python3 scripts/validate_examples.py
```

La validation verifie que les exemples JSON-LD sont du JSON valide, contiennent les champs requis et respectent le schema minimal du depot.

## Composants non inclus

Ce depot ne contient pas de registre securise, de service de certification, de module de fingerprinting, de detection d'usage, de surveillance ou d'anti-contournement.

Des produits ou modules commerciaux peuvent exister separement, mais ils ne font pas partie du profil ouvert publie ici et ne sont pas requis pour lire ou implementer ce manifeste.

## Licence

Les fichiers publics de ce depot sont publies sous licence MIT. Voir `LICENSE`.
