# CRSA

CRSA is a Chinese single-domain task-oriented dialogue dataset focused on **airline ticket booking**. It contains **1,480** dialogue sessions and **12,136** utterances. The dataset supports fine-grained annotations over dialogue acts, slot values, task phases, user anomalies, and system control strategies. All dialogues follow a multi-turn, system-led task progression structure. CRSA offers a robust benchmark for training controllable, adaptive, and context-aware TOD systems.

Refer to our paper for more details: [CRSA: A Chinese Task-Oriented Dialogue Dataset with Rich Contextual Semantic Annotations]

## 🧰 Annotation Protocols

We provide structured annotation protocols (Appendix A of our paper), including:

- `annotation_guidelines/system_guideline.md`: System-side behavior and flow control rules
- `annotation_guidelines/user_guideline.md`: User-side expression and task goal guidance
- `annotation_guidelines/anomaly_definitions.md`: Six types of user anomalies and system response strategies

---

## 📊 Data

In `data/` directory. CRSA data includes JSON-formatted files: `train.json`, `valid.json`, `test.json`.

Data statistics:

| Split    | Dialogues | Turns  | Avg. Turns | Avg. Slots | Avg. Values |
|----------|-----------|--------|------------|------------|-------------|
| Train    | 1,100     | ~9,000 | 17.5       | 15         | 1670        |
| Valid    | 190       | ~1,540 | 17.5       | 15         | 1670        |
| Test     | 190       | ~1,600 | 17.5       | 15         | 1670        |

## 🎯 Goal Types and Statistics

We define different dialogue types based on user behavior and goal structure:

| Type                  | Count | Goal Change Rate | Anomaly Rate | Avg. Sub-goals | Avg. Dialog Acts | Avg. Turns |
|-----------------------|-------|------------------|--------------|----------------|------------------|------------|
| Simple                | 352   | 0.12             | 0.15         | 1.2            | 2.1              | 12.6       |
| Multi-intent          | 480   | 0.28             | 0.19         | 2.7            | 2.4              | 17.3       |
| Multi-intent+Anomaly  | 648   | 0.34             | 0.31         | 3.1            | 2.7              | 21.2       |

---

## 📂 Data Format

Each annotated dialogue consists of the following structure:

### 🔹 `Context`

Stores structured multi-turn history of the dialogue, segmented into phases:

- `basic_information`: early slot-filling (e.g. departure, destination, date)
- `ticket_selection`: option listing, user preferences, user selection
- `booking_information`: personal details for ticket booking
- `utterances`: list of system/user utterances within each phase
- `slots`: all accumulated slot values (e.g., `departure_time`, `price`)
- `ticket_options`: candidate flights (in selection phase)
- `user_choice`: the final chosen option (if any)
- `current_step`: boolean indicating whether a phase is ongoing

### 🔹 `Dialogue`

Captures the **last system-user interaction** with intent-level annotation:

- `agenda`: the system's utterance, decomposed into:
  - `statements`: factual content
  - `question`: system inquiry
  - `current_step`: the dialogue phase
- `user`: the user reply, with:
  - `utterances`: user natural utterance
  - `anomaly_analysis`:
    - `has_anomaly`: whether an anomaly exists
    - `anomaly_reason`: type of anomaly (e.g., Irrelevant_demand)
    - `system_Dialogue_action`: expected system action response

### 🔹 `Slots`

Final extracted task-relevant information for the session:

```json
{
  "destination": "昆明",
  "departure": "济南",
  "departure_time": "19号下午",
  "airlines": "",
  "cabin": "",
  "price": "",
  ...
}
---

## ⚙️ Code

See `scripts/` for:
- Data preprocessing
- Format conversion
- Metric evaluation (BLEU, ROUGE, TCR, ADFC, CRAM, etc.)

See `auto_annotation/` for:
- Baichuan2-based multi-task annotation model
- Scripts for semi-automatic labeling

---

## 🧪 Evaluation & Benchmarks

CRSA supports benchmarks for:
- Dialogue state tracking (DST)
- Intent classification and act prediction
- System Response Generation
- Controllable Response (flow, style, query)
- User Simulation

Example: LoRA-finetuned Baichuan2-7B achieves high TCR, ADFC, and CRAM when trained on CRSA.

---

## 📈 Result

![example](examples/visualization.png)

---

## 📚 Citation

📄 License
This dataset is released under the CC BY 4.0 License.
