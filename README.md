AUTHENTICA  AI Rights & Origin Manifest

Standard ouvert de transparence IA, preuve d’origine et conformité européenne (AI Act)


AUTHENTICA définit un cadre souverain et interopérable permettant :

•	la preuve d’origine d’une œuvre (création humaine)

•	la transparence IA imposée par le AI Act

•	le TDM opt-out (directive européenne)

•	un identifiant universel UID_AUTH

•	un manifeste machine readable, compatible DSP, IA et OGC

•	une architecture ouverte, sans dépendance à une plateforme.

Ce dépôt contient les éléments publics du standard.

Les composants sensibles (registre sécurisé, génération UID_AUTH, signature cryptographique, LockDNA, anti-contournement) sont accessibles uniquement sous NDA.


1. Objectif du standard

Le AI Act impose :

1.	la traçabilité des contenus

2.	l’indication de l’origine humaine/IA

3.	des signaux lisibles par les systèmes IA

4.	le respect du TDM opt-out

AUTHENTICA fournit exactement cette couche manquante entre :

• les auteurs

• les sociétés de gestion collective (OGC)

• les plateformes (DSP)

• les IA génératives

• le cadre réglementaire européen.


2. Architecture du protocole

Le protocole AUTHENTICA repose sur trois briques :

1) UID_AUTH (identifiant souverain) déjà opérationnel

Format lisible, horodaté, stable, permettant :

•	la référence d’une œuvre,

•	la déclaration humaine/IA,

•	la compatibilité juridique inter-pays

•	l’interopérabilité avec les OGC


Exemple :

FR-2025-AUTH-MUS-000001

L’UID_AUTH est émis par une autorité identitaire (OGC ou opérateur délégué dans un pilote)



2) Manifeste IA (JSON-LD) déjà opérationnel

Inclut :

•	origine humaine

•	TDM opt-out

•	restrictions d’usage IA

•	hash d’intégrité

•	UID_AUTH

•	timestamp

•	issuer

•	conformité RGPD (aucune donnée personnelle)

Le manifeste est lisible par les IA, DSP, régulateurs et outils juridiques.


3) Empreinte native LockDNA spécifiée, R&D en cours

Le protocole AUTHENTICA prévoit une empreinte extraite du contenu réel (audio, image, vidéo, texte), permettant :

•	robustesse aux compressions,découpage, transcodages

•	invariance dans le temps

•	indépendance du format

•	détection autonome dans les usages illicites IA

LockDNA est un module propriétaire en développement, soumis à R&D DSP/audio & vision.

Il n’est pas inclus dans le présent dépôt.


3. Propriétés principales

•	Standard ouvert : interopérable, neutre, sans dépendance propriétaire

•	Preuve d’origine souveraine : UID_AUTH + hash + manifeste IA

•	Compatible AI Act : transparence, provenance, déclaration, TDM opt-out

•	RGPD compliant : aucune donnée personnelle dans le manifeste

•	Multimédia : spécifié pour audio, vidéo, image, texte

•	Machine-readable : JSON-LD, basé sur schema.org et vocabulaires droits

•	Non intrusif : ne modifie pas le fichier original.


4. Intégration avec les sociétés de gestion collective (OGC)

AUTHENTICA est conçu pour être utilisé par :

• SACEM

• ADAMI

• SPEDIDAM

• PRS

• STIM

• GEMA

• SIAE

• SABAM, etc….

Le protocole ne remplace pas les OGC

Il fournit la couche technique qui leur manque :

•	preuve d’origine

•	transparence IA

•	UID unifié

•	compatibilité réglementaire

•	registres vérifiables

•	traçabilité des usages IA

L’OGC reste en charge de :

•	la gestion des droits

•	les répartitions

•	les flux financiers

•	les règles internes


AUTHENTICA = infrastructure technique souveraine, pas un concurrent


5. Exemples de manifeste (JSON-LD)

→ Œuvre audio
{
  "@context": "https://schema.authentica.org/ai-rights/v1",
  "@type": "CreativeWork",

  "uid_auth": "FR-2025-AUTH-MUS-000001",
  "name": "Example Audio Work",
  "creator": "Anonymous",
  "origin": "human",

  "rights": {
    "ai_training": "prohibited",
    "tdm_opt_out": true
  },

  "hash": {
    "algorithm": "sha256",
    "value": "EXAMPLE-AUDIO-HASH"
  },

  "issued_at": "2025-11-11T00:40:07Z",
  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  }
}
6. Gouvernance et interopérabilité

AUTHENTICA définit :

•	un namespace par OGC / autorité

•	un format stable de manifeste

•	un schéma d’émission UID_AUTH

•	les propriétés minimales exigées par le AI Act


Interoperable avec :

• son propres vocabulaires

• schema.org CreativeWork

• ODRL (Open Digital Rights Language)

• JSON Schema


7. Statut du projet (2025)

•	UID_AUTH : opérationnel, ouvert

•	Manifeste IA Act : opérationnel, stable

•	MVP LockTrace Genesis : disponible en démonstration

•	Pilote institutionnel : en cours de cadrage

•	LockDNA (empreinte native) : spécification complète, implémentation en R&D

Les composants internes (registre, signature, anti-contournement) sont fournis exclusivement sous NDA


8. Licence

Ce dépôt concerne uniquement la spécification du standard

L’implémentation complète d’AUTHENTICA ne fait pas partie du code ouvert
