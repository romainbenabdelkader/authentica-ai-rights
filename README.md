![AUTHENTICA AI Rights Manifest](https://img.shields.io/badge/AUTHENTICA%20AI%20Rights-v1-black?style=flat-square)

# AUTHENTICA — AI Rights Manifest (v1)
# AUTHENTICA  AI Rights Manifest (v1)

The AUTHENTICA AI Rights Manifest defines the first machine-readable
standard for protecting human creative works against unauthorized AI
training, extraction, or replication.

This manifest provides:
- a universal identifier (uid_auth),
- a declaration of origin (human-created),
- explicit rights and restrictions,
- an interoperable JSON-LD schema,
- and a verifiable cryptographic signature.

---

## 📘 Schema

The manifest schema is stored in:

/manifest/schema.json

It defines the required fields:
- @context
- type
- uid_auth
- creator
- origin
- rights
- signature

---

## 📦 Manifest Examples

Examples for different types of works are available under:

/examples/

- example-audio.jsonld  
- example-image.jsonld  
- example-text.jsonld  

Each file contains:
- a UID AUTHENTICA
- AI training permissions
- text/data mining opt-out (TDM)
- SHA256 signature of the work

---

## 🧭 Purpose

The goal of this repository is to provide an **open, sovereign and
verifiable** metadata standard allowing:

- authors to mark their works as *human*,
- institutions to enforce AI-training restrictions,
- platforms to respect opt-out signals,
- and regulators to adopt a unified international format.

The manifest is compatible with:
- EU AI Act  
- EU Copyright Directive  
- TDM Opt-Out (Art. 4)  
- GDPR (no personal data stored)

---

## 🔐 Verifiability

AUTHENTICA manifests include:

- SHA-256 signature of the source file
- a deterministic uid_auth
- an auditable JSON-LD structure

These guarantees allow institutions, platforms and regulators to verify
origin and rights without ambiguity.

---

## 📄 License

Open format free to implement and integrate.

For questions or institutional use:
contact: [romain@lockdna.tech]