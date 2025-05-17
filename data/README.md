# CRSA Dataset Repository

This repository contains the official release of the **CRSA (Context-Rich Semantic Annotation)** dataset and its associated training subsets for both:

- **Automatic Annotation Model Training**  
- **Dialogue Response Generation Model Training**

CRSA is a Chinese task-oriented dialogue dataset constructed under a structured Wizard-of-Oz framework. It features multi-source construction, multi-level annotations, and fine-grained behavior control signals to support the development of controllable, semantically rich dialogue systems.

---

## 📦 Dataset Structure

The repository contains the following components:

| File Name                        | Description |
|----------------------------------|-------------|
| `AnnotationTrainData.json.zip`  | Training set for the CRSA structure prediction (annotation) model. Each sample is an instruction-input-output triple, where output is the structured annotation. |
| `AnnotationTestData.json.zip`   | Test set used to evaluate the annotation model's structured generation performance. |
| `SubtaskTrainData.json.zip`     | Subset of CRSA formatted to support various TOD subtask studies (e.g., DST, intent classification, anomaly detection). |
| `SubtaskTestData.json.zip`      | Evaluation set for subtask-specific models in the TOD pipeline. |
| `train.json.zip`                | Full CRSA training set with three-layer annotations (`Context`, `Dialogue`, `Slots`). |
| `test.json.zip`                 | Full CRSA test set. Mirrors the structure and semantics of `train.json.zip`. |
| `RawData.json.zip`              | Unlabeled dialogues collected from real-world scenarios, prior to any annotation or structure transformation. |
| `user_utterances.zip`           | Crowdsourced user utterance variants for data augmentation and behavior simulation. Useful for user simulator or response rewriting tasks. |
| `system_behaviours_inquiry.csv` | A curated reference of 63 system behaviors and their corresponding inquiry forms, covering the action space used in CRSA. Essential for modeling system-side dialogue policy and flow control. |
| `anomaly_reasons.json`          | Complete taxonomy of user-side dialogue anomalies, with 6 major categories and 39 fine-grained types. Enables anomaly-aware response strategies and controllable generation. |

---

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

Use `AnnotationTrainData.json` with LLaMA-Factory or instruction-tuned models.

### For Dialogue System Training

Use `train.json` with LLaMA-Factory or instruction-tuned models.

### For TOD subtasks Evaluation

Use `SubtaskTrainData.json` with LLaMA-Factory or instruction-tuned models.

### For User Simulator Training

Use `user_utterances.zip` with LLaMA-Factory or instruction-tuned models.

### For TOD related research on unlabeled corpus

Use `RawData.json` with LLaMA-Factory or instruction-tuned models.
