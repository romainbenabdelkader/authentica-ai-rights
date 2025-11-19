# AUTHENTICA – AI Rights Manifest (v1)

The AUTHENTICA AI Rights Manifest defines the first sovereign, machine-readable standard for declaring  
the origin, rights, and AI-usage restrictions of creative works.

This specification enables creators, publishers, cultural institutions, and Collective Management Organisations (CMOs)  
to embed a verifiable, blockchain-anchored manifest into any file (audio, image, text, video).

---

## 🚩 Purpose

AUTHENTICA establishes a simple rule:

**Every creative work has the right to declare how AI is allowed or forbidden to use it.**

The manifest allows any work to include:

• its human origin  
• its sovereign identifier (UID_AUTH)  
• AI-training permissions (`allowed`, `prohibited`, `restricted`)  
• TDM opt-out flags (EU DSM)  
• licensing price per million tokens (optional)  
• a LockDNA fingerprint hash  
• a proof-of-origin timestamp (blockchain anchored)  
• optional linkage to CMOs (SACEM, GEMA, PRS, ASCAP…)

---

## 📌 Manifest Structure (JSON-LD)
---{
“@context”: [
“https://www.w3.org/ns/activitystreams”,
“https://schema.lockdna.tech/ai-rights/v1”
],
“type”: “CreativeWork”,
“uid_auth”: “FR-2025-AUTH-000001”,
“name”: “Work Title”,
“creator”: “Author Name”,
“origin”: “human”,
“rightsAI”: {
“ai_training”: “prohibited”,
“tdm_opt_out”: true,
“ai_training_price_per_million_tokens_usd”: 0.025,
“cmo_required”: “SACEM-FR”,
“cmo_authorization_id”: “SACEM-IA-2026-004217”
},
“fingerprint”: “sha256-LOCKDNA-HASH”,
“proofSince”: “2025-11-11T00:40:07Z”,
“signature”: “sha256-SIGNATURE”

## 🏛️ Compatibility with Collective Management Organisations (CMOs)

AUTHENTICA fully respects the legal monopoly of CMOs for mandatory collective management.

When a work belongs to a CMO:

- `ai_training_price_per_million_tokens_usd` = **recommended retail price**  
- AI licensing MUST occur through the CMO  
- `cmo_required` indicates the CMO (ex: `SACEM-FR`)  
- `cmo_authorization_id` can reference a CMO agreement

Example:“rightsAI”: {
“ai_training”: “paid-only”,
“ai_training_price_per_million_tokens_usd”: 0.025,
“cmo_required”: “SACEM-FR”,
“cmo_authorization_id”: “SACEM-IA-2026-004217”
}
---
## 📂 Project Structure
authentica-ai-rights/
│
├── README.md
│
├── manifest/
│   ├── schema.json
│   ├── examples/
│   │   ├── example-audio.jsonld
│   │   ├── example-image.jsonld
│   │   ├── example-text.jsonld
│   │   └── example-video.jsonld
│   └── docs/
│       ├── manifest-spec.md
│       └── cmo-compatibility.md
│
├── lockdna/
│   ├── spec-lockdna-alpha.md
│   └── examples/
│       └── fingerprint_example.json
│
├── api/
│   ├── endpoints.md
│   └── example-calls/
│       └── declaration_example.json
│
├── licensing/
│   ├── cmo-guidelines.md
│   ├── ai-training-policy.md
│   └── publisher-usage.md
│
└── legal/
    ├── open-manifest-license.md
    ├── disclaimer.md
    └── governance.md

## 🔒 LockDNA Fingerprint

Each manifest may include a LockDNA fingerprint:
“fingerprint”: “sha256-LOCKDNA-HASH”
This hash is computed from the source file (audio, image, text, video)  
and anchored to blockchain as legal proof of origin.

---

## 🧪 Included Examples

AUTHENTICA provides examples for:

• audio  
• image  
• text  
• video  
• fingerprint generation  
• declaration API examples  

---

## 🏁 License

This manifest is published under an open specification license,  
allowing CMOs, governments, creators, and institutions to adopt AUTHENTICA freely.
