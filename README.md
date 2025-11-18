# AUTHENTICA — AI Rights Manifest (v1)

The AUTHENTICA AI Rights Manifest defines the first sovereign, machine-readable
standard for declaring the **origin**, **rights**, and **AI-usage restrictions** of creative works.

This specification provides creators, publishers, cultural institutions, and
collective management organizations with a verifiable digital manifest
that can be embedded into any file (audio, image, text, video).

---

## 🌐 Purpose

AUTHENTICA establishes a simple rule:

**Every creative work has the right to declare how AI is allowed—or forbidden—to use it.**

The manifest allows any work to include:

- its human origin  
- its unique sovereign identifier (**uid_auth**)  
- its creator  
- its AI-usage permissions  
- its cryptographic signature  
- its date of proof

This standard is open, extensible, and compatible with the EU AI Act and GDPR.

---

## 🧩 Repository Structure

```
authentica-ai-rights/
│
├── README.md
├── manifest/
│   ├── manifest-v1.jsonld       # The official v1 manifest format
│   └── schema.json              # JSON-LD schema for validation
│
└── examples/                    # Examples for different media types
    ├── example-audio.jsonld
    ├── example-image.jsonld
    ├── example-text.jsonld
    └── example-video.jsonld
```

---

## 📜 Manifest Specification (v1)

The manifest is a JSON-LD document containing the following fields:

- **@context** — reference to the AUTHENTICA AI Rights schema  
- **type** — usually "CreativeWork"  
- **uid_auth** — universal sovereign identifier (e.g. FR-2025-AUTH-000001)  
- **name** — work title  
- **creator** — author or rights holder  
- **origin** — "human", "hybrid", or "ai"  
- **rights**:  
  - **ai_training** — "prohibited", "allowed", or "restricted"  
  - **tdm_opt_out** — boolean (EU text-and-data-mining opt-out)
- **signature** — SHA-256 or Ed25519 hash  
- **proofSince** (optional) — date of original creation or deposit  

See `manifest/manifest-v1.jsonld` for the authoritative version.

---

## 🧪 Example Files

Sample manifests for all media types are available in `/examples`:

- `example-audio.jsonld`
- `example-image.jsonld`
- `example-text.jsonld`
- `example-video.jsonld`

Each example demonstrates how to declare human origin, rights, and AI restrictions.

---

## 🔐 Sovereign Identifier (uid_auth)

The **uid_auth** follows the AUTHENTICA sovereign format:

```
FR-2025-AUTH-000001
```

It can be generated automatically through the AUTHENTICA infrastructure.

---

## ⚖️ Licensing

This specification is released under **CC0-1.0**  
→ Free to use, adapt, and integrate in any system.

---

## ✉️ Contact

Author: **Romain Benabdelkader**  
Website: https://lockdna.tech  
Project: AUTHENTICA – Sovereign Proof Infrastructure  