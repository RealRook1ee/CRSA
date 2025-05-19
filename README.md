# CRSA

CRSA is a Chinese single-domain task-oriented dialogue dataset focused on **airline ticket booking**. It contains **1,480** dialogue sessions and **26,048** utterances. The dataset supports fine-grained annotations over dialogue acts, slot values, task phases, user anomalies, and system control strategies. All dialogues follow a multi-turn, system-led task progression structure. CRSA offers a robust benchmark for training controllable, adaptive, and context-aware TOD systems.

Details are available in our EMNLP 2025 submission (currently under review).

## 🧰 Annotation Protocols

We provide structured annotation protocols (Appendix A of our paper), including:

- `data/system_guideline.md`: System-side behavior and flow control rules
- `data/user_guideline.md`: User-side expression and task goal guidance
- `data/anomaly_definitions.md`: Six types of user anomalies and system response strategies

---

## 📊 Data

In `data/` directory. CRSA data includes JSON-formatted files: `train.json`, `valid.json`, `test.json`.

Data statistics:

| Split    | Dialogues | Turns   | Avg. Turns | Avg. Slots | Avg. Values |
|----------|-----------|---------|------------|------------|-------------|
| Train    | 1,100     | ~18,838 | 17.1       | 14.8       | 1670        |
| Valid    | 190       | ~3,427  | 18.0       | 15.2       | 1670        |
| Test     | 190       | ~3,783  | 19.9       | 15.2       | 1670        |

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
{
    "Context": {
      "basic_information": {
        "current_step": false,
        "utterances": [...],
        "slots": {...}
      },
      "ticket_selection": {
        "current_step": true,
        "utterances": [...],
        "ticket_options": [...],
        "user_choice": {}
      },
      "booking_information": {
        "current_step": false,
        "utterances": [],
        "personal_information": {...}
      }
    },
    "Dialogue": {
      "agenda": {
        "current_step": "ticket_selection",
        "utterances": "",
        "analysis": {
          "question": ".",
          "system_Dialogue_action": ""
        }
      },
      "user": {
        "utterances": "",
        "anomaly_analysis": {
          "has_anomaly": false,
          "anomaly_reason": ""
        }
      }
    },
    "Slots": {
      "destination": "",
      "departure": "",
      "departure_time": "",
      "airport": "",
      "price": "",
      "airlines": "",
      "cabin": "",
      "name": "",
      "ID": "",
      "Infant_or_not": "",
      "seat_type: "",
      "transit": "",
      "discount": "",
      "meal": "",
      "baggage": ""
    }
  },
  "output": {
    "system_dialogue_act": "",
    "utterances": "",
    "control": {
      "style": "kind",
      "query": "brief",
      "deviation": "skip",
      "flow": "Slots-seq-2"
    }
  }
}

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

Final extracted task-relevant information for the session.
CRSA defines 15 task-relevant slot types to support comprehensive user intents and booking constraints. 

Each slot captures a specific aspect of the user's goal in airline ticket booking.

Below are the slot definitions:

| Slot Name         | Description                                                              |
| ----------------- | ------------------------------------------------------------------------ |
| `departure`       | Departure city or location from which the user wishes to fly             |
| `destination`     | Target city or location to which the user wants to travel                |
| `departure_time`  | Preferred date and/or time of departure                                  |
| `flight_duration` | Estimated or preferred duration of the flight                            |
| `airport`         | Specific airport name or preference                                      |
| `price`           | Price constraints                                                        |
| `cabin`           | Preferred cabin class                                                    |
| `transit`         | Whether the user prefers direct flights or allows transfer               |
| `airlines`        | Preferred airline or carrier                                             |
| `seat_type`       | Preferred seat location                                                  |
| `meal`            | Whether the flight should include onboard meals                          |
| `baggage`         | Free luggage allowance requirements or expectations                      |
| `discount`        | User's concern or eligibility regarding discounts                        |
| `round_trip`      | Whether the user requires a round-trip booking                           |
| `personal_info`   | User's personal booking information                                      |

---

## 🧪 Evaluation & Benchmarks

CRSA supports benchmarks for:
- Dialogue state tracking (DST)
- Intent classification and act prediction
- System Response Generation
- Controllable Response (flow, style, query)
- User Simulation

---


## 📚 License

This dataset is released under the CC BY 4.0 License.
