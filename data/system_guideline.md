## 📘 System-side Behavior and Flow Control Rules

The CRSA dataset uses a system-initiated, multi-turn dialogue structure. The following core principles govern system behavior:

### 📌 Three-stage Dialogue Flow

1. **Basic Information Collection**: Departure city, destination, departure time, etc.
2. **Option Recommendation & Selection**: System proposes candidates, user chooses.
3. **Supplementary & Finalization**: User info, order confirmation, dialogue closure.

### 🔍 Stage-based Slot Management

- **Mandatory Slots**: `departure`, `destination`, `departure_time`, `personal_info`
- **Optional Slots**: `price`, `airline`, `duration`, `meal`, `baggage`, etc.
- Each stage defines which slots must or should be filled.

### 🧠 Dialogue Flow Control

User input is classified into:

- Slot-related queries → Must be fully addressed
- Business-relevant but slot-independent queries → Attempt informative reply
- Non-task-related queries → Politely guide user back to the main task

Each system utterance is composed of two distinct parts:

- **Contextual Description**: Provides background or status updates
- **Intent Directive**: Asks specific slot-related questions or guides task flow

System replies follow a decision tree based on user responses:

- Expected → Progress to next slot or stage
- Unexpected → Handle via error strategies or guidance
- Ambiguous → Clarify or re-ask

System actions include: `ask`, `clarify`, `confirm`, `refuse`, `recommend`, `end`, etc. (63 types total).

These actions are dynamically selected based on:

- Dialogue stage
- Current slot filling state
- Detected user anomalies (e.g., off-topic, vague, contradictory)

### 📊 Handling Out-of-Scope User Queries

- **Slot-related**: Fully answered
- **Task-relevant**: Informative replies
- **Task-irrelevant**: Neutral reply + re-guidance

Each system utterance = [Context] + [Directive] for clear structure and controllability.