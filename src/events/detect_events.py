def detect_event(previous_state, current_state):

    if previous_state is None:
        return "system_start"

    if current_state["interaction"] == "competitive":
        return "competitive_interaction"

    if current_state["activity_level"] == "high":
        return "high_activity"

    if current_state["dominant_species"] != previous_state["dominant_species"]:
        return "species_change"

    if current_state["behavior"] == "feeding":
        return "feeding_activity"

    return "normal_activity"