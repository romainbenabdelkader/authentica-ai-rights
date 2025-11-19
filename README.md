# AUTHENTICA – AI Rights Manifest (v1)

The AUTHENTICA AI Rights Manifest defines the first sovereign, machine-readable standard for declaring  
the origin, rights, and AI-usage restrictions of creative works.

This specification enables creators, publishers, cultural institutions, and Collective Management Organisations (CMOs)  
to embed a verifiable, blockchain-anchored manifest into any file (audio, image, text, video).

---

## 🚩 Purpose

AUTHENTICA establishes a simple rule:

**Every creative work has the right to declare how AI is allowed or forbidden to use it.**

The manifest allows any work to specify:

• its human origin  
• its sovereign identifier (UID_AUTH)  
• AI-training permissions (`allowed`, `prohibited`, `restricted`)  
• TDM opt-out flags (EU DSM)  
• links to CMOs when required (SACEM, GEMA, PRS, ASCAP, etc.)  
• optional licensing price per million tokens for AI training  
• a LockDNA fingerprint hash  
• a proof-of-origin timestamp (blockchain anchored)

---

## 📌 Manifest Structure (JSON-LD)

All manifests follow this schema:
{
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
---

## 🏛️ Explicit CMO Compatibility (SACEM, GEMA, PRS, ASCAP…)

AUTHENTICA fully respects the legal monopoly of CMOs for mandatory collective management.

When a work is managed by a CMO:

- `ai_training_price_per_million_tokens_usd` = **recommended retail price**  
- The *actual licensing* **must** go through the relevant CMO  
- `cmo_required` indicates which CMO applies  
- `cmo_authorization_id` can store a CMO contract reference

Example:
“rightsAI”: {
“ai_training”: “paid-only”,
“ai_training_price_per_million_tokens_usd”: 0.025,
“cmo_required”: “SACEM-FR”,
“cmo_authorization_id”: “SACEM-IA-2026-004217”
---

## 📂 Repository Structure
authentica-ai-rights/
│
├── README.md
│
├── manifest/
│   ├── schema.json
│   ├── examples/
│   │   ├── example-audio.jsonld
│   │   ├── example-image.jsonld
│   │   ├── example-text.jsonld
│   │   └── example-video.jsonld
│   └── docs/
│       ├── manifest-spec.md
│       └── cmo-compatibility.md
│
├── lockdna/
│   ├── spec-lockdna-alpha.md
│   └── examples/
│       └── fingerprint_example.json
│
├── api/
│   ├── endpoints.md
│   └── example-calls/
│       └── declaration_example.json
│
└── licensing/
├── cmo-guidelines.md
├── ai-training-policy.md
├── publisher-usage.md
---

## 🔒 LockDNA Fingerprint

Every manifest can include a LockDNA fingerprint:
“fingerprint”: “sha256-LOCKDNA-HASH”
This hash is generated directly from the source file (audio, image, text, video)  
and anchored to blockchain for legal evidentiary purposes.

---

## 🧪 Examples Included

Examples are provided for:

- audio (`example-audio.jsonld`)
- image
- text  
- video  
- fingerprint sample  
- declaration API example

---

## 🏁 License

This manifest is provided under a permissive open specification license  
allowing CMOs, governments, and creators to implement AUTHENTICA freely.

Author: **Romain Benabdelkader**  
Website: https://lockdna.tech  
Project: AUTHENTICA Sovereign Proof Infrastructure  
