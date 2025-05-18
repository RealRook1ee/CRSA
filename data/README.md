# CRSA Dataset Repository

This repository contains the official release of the **CRSA (Context-Rich Semantic Annotation)** dataset and its associated training subsets for both:

- **Automatic Annotation Model Training**  
- **Dialogue Response Generation Model Training**

CRSA is a Chinese task-oriented dialogue dataset designed for Chinese task-oriented dialogue modeling in the real-world business. It features multi-source construction, multi-level annotations, and fine-grained behavior control signals to support the development of controllable, semantically rich dialogue systems.

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

## 📚 File Descriptions and Usage

### 🧩 1. `AnnotationTrainData.json` & `AnnotationTestData.json`
- **Purpose**: Train instruction-tuned models to automatically annotate dialogues in CRSA format.
- **Format**: Each sample includes `instruction`, `input`, and `output`.

**Example**:
```json
{
  "instruction": "Please analyze and annotate the following dialogue. The output must follow the CRSA JSON format: {"Context": {"basic_information": {"current_step": , "utterances": [], "slots": {"destination": "", "departure": "", "airport": "", "departure_time": "", "airlines": "", "cabin": "", "price": "", "flight_duration": "", "arrival_time": ""}}, "ticket_selection": {"current_step": false, "utterances": [], "ticket_options": [], "user_choice": {}}, "booking_information": {"current_step": false, "utterances": [], "personal_information": {"name": "", "id_number": "", "phone_number": ""}}}, "Dialogue": {"agenda": {"current_step": "basic_information", "utterances": "", "analysis": {"question": "", "statements": []}}, "user": {"utterances": "", "anomaly_analysis": {"has_anomaly": false, "anomaly_reason": ""}}}, "Slots": {"destination": "", "departure": "", "airport": "", "departure_time": "", "airlines": "", "cabin": "", "price": "", "flight_duration": "", "arrival_time": ""}}",
  "input": "'System: Hello, are you looking to book a flight?\nUser: Yes, I need a flight from Wuhan to Qingdao in the afternoon.'",
  "output": "{...annotated JSON output...}"
}
```

---

### 💬 2. `train.json`
- **Purpose**: Train system response generation models in a structured annotation context.
- **Format**: Each sample provides a partially filled dialogue context, current user utterance, and expected system reply.

**Example**:
```json
{
  "instruction": "Generate a proper system response based on the annotated dialogue state.",
  "input": {
    "Context": {
      "basic_information": {
        "current_step": true,
        "utterances": [
          {"speaker": "System", "text": ""},
          {"speaker": "User", "text": ""}
        ],
        "slots": {"destination": ""}
      }
    },
    "Dialogue": {
      "agenda": {
        "current_step": "basic_information",
        "utterances": "",
        "analysis": {"question": "", "system_action": ""}
      },
      "user": {
        "utterances": "",
        "anomaly_analysis": {"has_anomaly": , "anomaly_reason": ""}
      }
    },
    "Slots": {"destination": ""}
  },
  "output": {
        "system_dialogue_act": "",
        "utterances": "",
        "control": {"style": "", "query": "","deviation": "", "flow": ""}
   }
}
```

---

### 🧠 3. `SubtaskTrainData.json`
- **Purpose**: Train and evaluate models on subtasks like response generation (RG), dialogue act (DA), or state tracking (DST).
- **Format**: Input includes structured action/intent tokens, history, and label type.

**Example**:
```json
{
  "dial_id": "flight_goal###726",
  "task": "flight",
  "turn_id": 2,
  "input_text": " <actions> ( flight ) clarify departure <endofactions> <history> USER: …… <endofhistory>",
  "output_text": "请问您说的是出发地吗",
  "train_target": "task(nlu/dst/dp/rg)"
}
```

---

### 👤 4. `user_utterances.zip`
- **Purpose**: Contains user utterance candidates collected via crowdsourcing.
- **Use**: Ideal for user simulation and training data expansion.



---

### 📄 5. `RawData.json.zip`
- **Purpose**: Includes real dialogues without annotations.
- **Format**: Human-readable logs alternating between system and user turns.

**Example**:
```
"1094": {
    "system_1": "您好，请问您需要购买机票吗",
    "user_2": "对，我想买张上海到贵阳的机票",
    "system_3": "请问您的出发时间是什么时候",
    "user_4": "今年十一前的最后一个周日是几月几号",
    "system_5": "是九月二十九日，请问您的出发时间是9月29日吗",
    "user_6": "不，查查后一天的",
    "system_7": "好的，为您查询到九月30号的机票：Query_DB_tickets(departure,destination,time,NonEssentialSlots)。请问您想选择哪个航班",
    "user_8": "如果二十九号晚上走，有什么选择呢",
    "system_9": "好的，为您查询到29号的机票：Query_DB_tickets(departure,destination,time,NonEssentialSlots)。请问您想选择哪个航班",
    "user_10": "就选晚上七点半这趟",
    "system_11": "请问乘机人姓名和联系方式是什么",
    "user_12": "乘机人叫李强，电话19371921811",
    "system_13": "好的，已经为您订好19:30出发，联合航空的航班，乘机人李强，电话19371921811"
  },
"System_1": "Hello, do you need to buy a ticket",
"User_2": "yes, I want to buy a ticket from Shanghai to Guiyang",
"System_3": "when is your departure time, please",
"User_4": "what month is the last Sunday before November this year",
"System_5": "it's September 29. Is your departure time on September 29",
"User_6": "no, check the next day",
"System_7": "OK, I can find your ticket for September 30: query_db_tickets (Department, destination, time, nonessentialslots). Which flight would you like to choose ",
"User_8": "if you leave on the evening of the 29th, what options do you have",
"System_9": "OK, I can find your ticket on the 29th: query_db_tickets (Department, destination, time, nonessentialslots). Which flight would you like to choose ",
"User_10": "just choose the 7:30 p.m. train",
"System_11": "may I know the name and contact information of the passengers",
"User_12": "the passenger is Li Qiang, Tel: 19371921811",
"System_13": "OK, I have booked a flight for you to depart from United Airlines at 19:30. The passenger is Li Qiang. Tel: 19371921811"
```

---

### 🧭 6. `system_behaviours_inquiry.csv`
- **Purpose**: Lists 63 predefined system behaviors with corresponding prompt templates.
- **Use**: Useful for flow control modeling and template analysis.

**Sample**:
| Behavior ID          | System Prompt                        |
|----------------------|--------------------------------------|
| ask_departure_city   | Which city are you departing from?   |
| ask_destination_city | Which city are you flying to?        |

---

### 🚨 7. `anomaly_reasons.json`
- **Purpose**: Defines 6 major categories and 39 fine-grained user-side anomaly reasons.
- **Use**: Support error classification, response repair, or evaluation tasks.

**Sample**:
| anomaly_category     | anomaly_reason        |
|----------------------|-----------------------|
| unclear              | departure_time        |
| Irrelevant           | personal_info         |
| error                | conflict_slots        |

---

## 📄 License
This project is licensed under the [MIT License](../LICENSE).

© 2025 CRSA Authors. All rights reserved.
