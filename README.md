AUTHENTICA AI Rights Manifest (v1)

The AUTHENTICA AI Rights Manifest defines the first sovereign, machine-readable standard for declaring the origin, rights, and AI-usage restrictions of creative works.
It is designed to provide creators, publishers, cultural institutions and collective management organisations with a verifiable digital manifest that can be embedded into any file (audio, image, text, video).

Purpose

AUTHENTICA establishes a universal principle:
Every creative work has the right to declare how AI is allowed or forbidden to use it.

The manifest enables any work to define:
    •    its human origin
    •    its sovereign identifier (UID_AUTH)
    •    its AI permissions / prohibitions
    •    its tdm_opt_out / opt_in status
    •    its provenance and LockDNA fingerprint
    •    its signature for integrity

The system is interoperable with the EU AI Act, GDPR, W3C JSON-LD standards, and optional blockchain anchoring.

Manifest Schema (v1)

A manifest includes the following fields:
    •    @context: JSON-LD context
    •    type: usually “CreativeWork”
    •    uid_auth: sovereign universal identifier
    •    name: work title
    •    creator: author or rights holder
    •    origin: “human”, “hybrid”, or “ai”
    •    rightsAI: AI-usage policy
    •    fingerprint: LockDNA hash
    •    signature: cryptographic signature
    {
  "@context": [
    "https://schema.authentica.org/manifest-v1.jsonld",
    "https://www.w3.org/ns/activitystreams"
  ],
  "type": "CreativeWork",
  "uid_auth": "FR-2025-AUTH-000001",
  "name": "Work Title",
  "creator": "Author Name",
  "origin": "human",
  "rightsAI": {
    "ai_training": "prohibited",
    "tdm_opt_out": true
  },
  "fingerprint": "sha256-LOCKDNA-HASH",
  "signature": "sha256-SIGNATURE"
}
CMO (Collective Management Organisation) Compatibility

AUTHENTICA respects the legal monopoly of CMOs (SACEM, ADAMI, SPEDIDAM, SCPP, SPPF, GEMA, PRS, ASCAP…).
When a work belongs to a CMO:
    •    ai_training_price_per_million_tokens_usd serves as the recommended retail price
    •    All licensing must occur through the relevant CMO
    •    cmo_required identifies the CMO
    •    cmo_authorization_id can reference an official agreement{
  "rightsAI": {
    "ai_training": "paid-only",
    "ai_training_price_per_million_tokens_usd": 0.025,
    "cmo_required": "SACEM-FR",
    "cmo_authorization_id": "SACEM-IA-2026-004217"
  }
}
    
    
