AUTHENTICA – Universal Proof-of-Origin Protocol

AUTHENTICA est une infrastructure souveraine dédiée à la preuve d’origine et à la protection des œuvres numériques (musique, image, vidéo, texte).
Elle permet à chaque œuvre de prouver seule son origine humaine, son intégrité et sa chronologie, sans watermark, sans dépendance à une plateforme et en totale conformité RGPD et AI Act.

Principes fondamentaux

AUTHENTICA repose sur trois piliers :

1.    Empreinte native extraite du fichier
L’empreinte est calculée à partir du contenu réel du fichier (données binaires, caractéristiques spectrales, structure interne).
Elle n’est jamais intégrée ni injectée dans l’œuvre.

2.    Manifest JSON-LD externe
Chaque œuvre possède un manifest lisible par machine contenant :

– l’origine (humaine / IA / mixte)

– les droits liés à l’IA (interdiction, autorisation, conditions)

– l’UID_AUTH (identifiant souverain)

– la signature cryptographique

– la date de génération

Ce manifest n’altère jamais le fichier, il est stocké séparément.

3.    UID_AUTH Identifiant Souverain Universel

Un numéro unique, chronologique, vérifiable, permettant d’attester :

l’antériorité

la propriété

l’origine humaine

la cohérence du fichier dans le temps

L’UID_AUTH peut être vérifié instantanément.

Architecture du protocole

L’écosystème AUTHENTICA se compose de :

    •    Module LockDNA
Extraction d’empreinte native depuis les fichiers audio, vidéo, image, texte.

    •    Manifest AI Rights
Spécification JSON-LD décrivant les droits, l’origine, les interdictions IA, la signature.

    •    API de vérification
Permet de vérifier une œuvre, sa signature, son empreinte et son UID_AUTH.

    •    Compatibilité avec les sociétés de gestion collective
	
Le protocole est conçu pour être compatible avec SACEM, GEMA, PRS, ASCAP, etc...

Il ne remplace pas la gestion collective : il la renforce.

Usage avec les OGC (SACEM, GEMA, PRS…)

Lorsque l’œuvre appartient à une société de gestion collective :

    •    L’œuvre conserve son UID_AUTH.
	
    •    Le manifest peut inclure l’identifiant de la société (exemple : SACEM-FR).
	
    •    La société reste seule en charge de la perception et de la redistribution.
	
    •    AUTHENTICA agit comme preuve d’origine, preuve d’intégrité, preuve d’antériorité, et preuve d’usage IA.

 Ce que le protocole garantit
 
    •    L’œuvre ne peut pas être modifiée sans briser son empreinte.
   
    •    Aucun watermark n’est ajouté.
	
    •    L’empreinte reste stable même après compression (mp3, streaming, transcodage).
	
    •    La vérification reste possible des années plus tard.
	
    •    Le protocole fonctionne pour : audio, vidéo, image, texte.

 Statut

Le protocole AUTHENTICA est actuellement en phase active de déploiement, avec :

 un MVP fonctionnel

 un pilote en préparation

 un manifest standardisé

 un UID_AUTH opérationnel
