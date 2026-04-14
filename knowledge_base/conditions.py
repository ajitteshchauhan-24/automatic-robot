"""Medical conditions knowledge base"""

CONDITIONS = {
    "opioid_withdrawal": {
        "name": "Opioid Withdrawal",
        "description": "Opioid withdrawal is a group of symptoms that occur due to suddenly stopping or reducing opioid use.",
        "symptoms": "Anxiety, insomnia, muscle aches, sweating, nausea",
        "related_products": ["Lucemyra"]
    },
    "opioid_overdose": {
        "name": "Opioid Overdose",
        "description": "Life-threatening emergency caused by opioid toxicity",
        "symptoms": "Respiratory depression, loss of consciousness, pinpoint pupils",
        "related_products": ["Zimhi"]
    },
    "neuroblastoma": {
        "name": "Neuroblastoma",
        "description": "Pediatric cancer of the nervous system",
        "symptoms": "Abdominal mass, fatigue, weakness",
        "related_products": ["Iwilfin"]
    },
    "malignant_hyperthermia": {
        "name": "Malignant Hyperthermia",
        "description": "Genetic disorder causing severe reaction to anesthesia",
        "symptoms": "Muscle rigidity, rapid heart rate, high fever",
        "related_products": ["Revonto"]
    }
}

def get_condition_info(condition_name: str):
    """Get information about a specific condition"""
    condition_lower = condition_name.lower().replace(" ", "_")
    for key, value in CONDITIONS.items():
        if key == condition_lower or value["name"].lower() == condition_name.lower():
            return value
    return {"error": "Condition not found"}

def get_all_conditions():
    """Get list of all conditions"""
    return [{"name": v["name"], "description": v["description"]} for v in CONDITIONS.values()]