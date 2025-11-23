AUTHENTICA

European Proof-of-Origin Protocol for Creative Works

Version publique documentation non confidentielle

1. Mission

Dans un monde où l’IA génère, transforme et diffuse plus vite que le droit, une question devient essentielle :

Comment prouver de manière souveraine, vérifiable et universelle qu’une œuvre est réellement d’origine humaine et antérieure à toute copie ?

AUTHENTICA apporte une réponse européenne :

•	une preuve d’origine souveraine
	
•	un identifiant vérifiable (UID_AUTH)
	
•	un manifeste AI Act en JSON-LD
	
•	une empreinte native extraite du fichier source (LockDNA – en phase de spécification R&D)
	

AUTHENTICA vise à devenir la couche de vérité des œuvres créatives européennes.


2. Positionnement institutionnel

AUTHENTICA est conçu pour être interopérable avec l’ensemble des écosystèmes européens du droit d’auteur.

Compatibilité par conception avec :

•	France : SACEM, SACD, SCAM, ADAMI, SPEDIDAM, SCPP, SPPF 

•	Nordics : STIM, Teosto, KODA

•	Royaume-Uni : PRS for Music

•	Allemagne : GEMA

•	Italie : SIAE

•	Belgique : SABAM

Ainsi qu’avec les standards :

•	DDEX, ISRC, ISWC, EIDR

•	et les exigences du AI Act 2026 et du TDM opt-out.


Plusieurs échanges exploratoires en Europe ont confirmé la nécessité d’une infrastructure de certification partagée, en amont des dépôts et des collections.

(Aucune collaboration formelle n’est déclarée.)


3. Architecture (version publique)

3.1. UID_AUTH

Identifiant souverain, horodaté, vérifiable, utilisable hors plateforme.

Spécification publique disponible :
https://github.com/romainbenabdelkader/uid-auth

3.2. Manifeste AI-Rights (JSON-LD)

Compatible AI Act et conforme RGPD (zéro donnée personnelle).

Champs disponibles :

•	origin: human
	
•	tdm_opt_out: true
	
•	politique d’entraînement IA
	
•	compatibilité CMO (cmo_required, cmo_authorization_id)


3.3. Empreinte native (LockDNA)

Module d’empreinte multimodale (audio, image, vidéo, texte)
conçu pour être :

•	extrait directement du fichier source
	
•	robuste aux compressions
	
•	indépendant des plateformes
	
•	vérifiable hors ligne
	
•	conforme RGPD.

Actuellement en phase de spécification et de R&D.
Le MVP utilise une simulation contrôlée en attendant l’intégration native.


4. MVP actuel : LockTrace Genesis

Le MVP démontre :

•	certification immédiate

•	hash sécurisé + horodatage

•	génération des données nécessaires au manifeste AI Act (export automatisé prévu)

•	journalisation & dashboard

•	API simple d’intégration

•	support UID_AUTH (protocole spécifié intégration MVP en préparation)

•	simulation contrôlée de l’empreinte native (pré-LockDNA)

Objectif du MVP :
démontrer toute la chaîne de certification avant l’intégration de l’empreinte native LockDNA et du manifeste IA automatisé.


5. Intégration avec les OGC (CMO Mode)

AUTHENTICA respecte pleinement les prérogatives légales des sociétés de gestion collective.

Lorsqu’une œuvre relève d’une OGC, AUTHENTICA devient :

•	une preuve d’origine souveraine

•	un complément du dépôt

•	un outil de transparence IA

•	un support technique au TDM opt-out

•	un mécanisme probant en cas de litige


AUTHENTICA n’altère aucune mission des OGC.
Il renforce leur capacité à défendre les œuvres européennes dans un paysage numérique dominé par l’IA.


6. Vision européenne

AUTHENTICA n’est ni une application, ni une plateforme.
C’est une infrastructure de vérité, comparable à :

•	SSL/TLS (sécurité Web)
	
•	robots.txt (interactions automatiques)

•	ISRC / ISWC (identification des œuvres)

•	DDEX (interopérabilité éditoriale)

L’objectif :
une preuve d’origine universelle, souveraine, interopérable, et vérifiable en Europe comme dans le reste du monde.


7. Structure du dépôt

authentica-ai-rights/
│
├── README.md
├── manifest/
│   ├── schema.json
│   └── examples/
│       ├── music.json
│       ├── image.json
│       └── video.json
│
├── uid_auth/
│   └── spec-uidauth-v1.md
│
└── legal/
    ├── disclaimer.md
    └── open-manifest-license.md



	

8.  Contact
   
   
Romain Benabdelkader

Fondateur AUTHENTICA
France

romain@lockdna.tech
