AUTHENTICA AI Rights Manifest (v1)

The AUTHENTICA AI Rights Manifest defines the first sovereign, machine-readable standard for declaring the origin, rights, and AI-usage restrictions of creative works.

This specification provides creators, publishers, cultural institutions, and collective management organisations with a verifiable digital manifest that can be embedded into any file (audio, image, text, video).

⸻

🎯 Purpose

AUTHENTICA establishes a simple, universal principle:

Every creative work has the right to declare how AI is allowed or forbidden to use it.

The manifest allows any work to define:
    •    its human origin
    •    its unique sovereign identifier (UID_AUTH)
    •    its AI usage permissions or prohibitions
    •    its tdm_opt_out / opt-in status
    •    its provenance and synchronised fingerprint (LockDNA)

It also ensures interoperability with:
    •    the EU AI Act
    •    GDPR
    •    W3C JSON-LD best practices
    •    all blockchain anchoring systems (optional)

⸻

📦 Manifest Schema (v1)

{
  "@context": [
    "https://schema.authentica.org/manifest-v1.jsonld",
    "https://www.w3.org/ns/activitystreams"
  ],
  "type": "CreativeWork",
  "uid_auth": "FR-2025-AUTH-000001",
  "name": "Work Title",
  "creator": "Author or rights holder",
  "origin": "human",
  "rightsAI": {
    "ai_training": "prohibited",
    "tdm_opt_out": true
  },
  "fingerprint": "sha256-LOCKDNA-HASH",
  "signature": "sha256-SIGNATURE"
}
