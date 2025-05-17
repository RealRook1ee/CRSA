# CRSA Dataset Repository

This repository contains the official release of the **CRSA (Context-Rich Semantic Annotation)** dataset and its associated training subsets for both:

- **Automatic Annotation Model Training**  
- **Dialogue Response Generation Model Training**

CRSA is a Chinese task-oriented dialogue dataset constructed under a structured Wizard-of-Oz framework. It features multi-source construction, multi-level annotations, and fine-grained behavior control signals to support the development of controllable, semantically rich dialogue systems.

---

## 📦 Dataset Structure

The repository contains the following components:

CRSA-Dataset/
├── raw_corpus/ # Original dialogues before annotation
│ ├── real_user_dialogues.json # From real service logs
│ ├── simulated_dialogues.json # From crowd-annotated and LLM-enhanced simulation
│ └── README.md # Description of data sources and cleaning procedures
│
├── annotated_for_annotation_model/ # Used to train the automatic annotator
│ ├── train.json # Instruction → structured annotation
│ ├── valid.json
│ ├── test.json
│ └── sample_instruction_format.md # Instruction-format annotation example
│
├── annotated_for_dialogue_system/ # Used to train the dialogue generation model
│ ├── train.json # Instruction → system response
│ ├── valid.json
│ ├── test.json
│ └── prompt_design.md # Description of input structure (T, H, M, K)
│
├── schema/ # Slot schema and annotation conventions
│ ├── slot_definitions.md
│ ├── user_anomaly_types.md
│ └── annotation_guidelines.pdf
│
└── LICENSE # License: CC BY 4.0

---

## 🔍 Dataset Overview

| Component                            | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| `raw_corpus/`                       | Contains original dialogues collected from three sources: service logs, crowd simulation, and LLM generation |
| `annotated_for_annotation_model/`  | Instruction-tuning dataset for training Baichuan2-based structure prediction model |
| `annotated_for_dialogue_system/`   | Structured-response generation dataset for training a dialogue system |
| `schema/`                           | Defines the slot-value schema, user behavior types, and annotation protocols |

---

## 🧠 Annotation Format (Multi-Level)

All annotated dialogues follow the **CRSA structured JSON format**, which includes three levels:

- `Context`: Dialogue history segmented by task stage, with accumulated slot values
- `Dialogue`: Current user-system interaction with intent and anomaly analysis
- `Slots`: Global slot summary extracted from the full session

Each turn is manually or automatically annotated with:

- Dialogue phase (e.g., basic_information, ticket_selection)
- System dialogue act
- User anomaly type (if any)
- Semantic slot-value changes
- Key control signals for generation (e.g., $K_a$, $K_s$)

---

## 📚 Usage

### For Automatic Annotation Training

Use `annotated_for_annotation_model/*.json` with LLaMA-Factory or instruction-tuned models.

### For Dialogue System Training

Use `annotated_for_dialogue_system/*.json` with LLaMA-Factory or instruction-tuned models.


