# AUTHENTICA  AI Rights Manifest (v1)
The AUTHENTICA AI Rights Manifest defines the first sovereign, machine readable standard for declaring
the origin, rights, and AI usage restrictions of creative works.

This specification provides creators, publishers, cultural institutions, and collective management organizations
with a verifiable format to express:

	•	Human origin
	•	Authorship and ownership
	•	AI-training permissions
	•	TDM (Text & Data Mining) restrictions
	•	Mandatory fingerprint / signature
	•	Verification and auditability

📁 Repository Structure

authentica-ai-rights/

│
├── README.md
├── manifest/
│   ├── manifest-v1.jsonld
│   └── schema.json
│
└── examples/
    ├── example-audio.jsonld
    ├── example-image.jsonld
    └── example-text.jsonld

🔍 Purpose

The AUTHENTICA AI Rights Manifest is designed to:

	•	Protect human-made works from unauthorized AI training
	•	Provide a standard for legal and cultural institutions
	•	Enable transparent, verifiable rights metadata
	•	Establish a sovereign alternative to opaque AI datasets
	•	Support compliance with the EU AI Act & GDPR

⸻

📡 Machine Readable Rights

Each manifest contains:

	•	uid_auth Unique sovereign identifier
	•	origin “human” or “machine”
	•	rights.ai_training  “allowed”, “prohibited”, or “restricted”
	•	tdm_opt_out Legal opt-out flag for dataset mining
	•	signature SHA-256 signature of the work

⸻

🧪 Examples

The /examples folder contains example JSON-LD manifests for:

	•	Audio
	•	Image
	•	Text
  •	video

⸻

🛡 Vision

AUTHENTICA establishes the foundation for a sovereign, verifiable layer of rights for creative works
in the age of artificial intelligence ensuring transparency, fairness, and trust.
