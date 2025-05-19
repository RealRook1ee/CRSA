## 💬 User-side Expression and Task Goal Guidance

To ensure **expressiveness**, **realism**, and **diversity** on the user side, the CRSA dataset incorporates a specialized guide: **User-side Requirement Expression and Interaction Process Protocol**. It enables the creation of rich, varied user behaviors aligned with real-world booking experiences.

### 🎯 Task-oriented Slot Expression

Users are encouraged to express goals involving 15 canonical slots, including:

- Location (departure, destination, airport)
- Time (departure_time, arrival_time, flight_duration)
- Preferences (airline, price, cabin, transfer, baggage, meal)
- Identity (personal_info)

Users are free to:

- Ask about, refuse, or revise slot values
- Provide subjective preferences (e.g., "I want something cheap", "I don’t want to arrive too late")
- Change goals mid-conversation (e.g., "Actually, I want to leave from Shanghai instead")

A semantic normalization table supports flexible, natural input.

### 🌀 Simulating Realistic User Behaviors

The protocol encourages various user-side behaviors:

- Slot filling via indirect language
- Multi-turn preference refinement
- Challenging system assumptions
- Introducing chit-chat or task-irrelevant questions

Examples:

 >User: Is there a meal on the flight?
→ Treated as business-relevant query.
 >User: Do you like airplanes?
→ Treated as off-topic, system responds neutrally and redirects.


### 🧩 Dialogue Diversity via Scenario Prototypes

Users are instructed via sample scenarios to explore:

- Vague goal descriptions
- Mid-task goal switching
- Rejections of system proposals
- Passive cooperation or resistance
- Chit-chat or contextual noise

Each user is encouraged to mimic real-life customer behavior with a mix of cooperation, hesitance, exploration, and clarification-seeking dialogue moves.

---