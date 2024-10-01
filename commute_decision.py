
# Importing required libraries
from sympy import symbols, Or, And, Not, Implies, satisfiable

# Task 1: Define the Conditions as Propositions
Rain, HeavyTraffic, EarlyMeeting, Strike, Appointment, RoadConstruction = symbols(
    'Rain HeavyTraffic EarlyMeeting Strike Appointment RoadConstruction'
)

# Task 2: Define the Commuting Options
WFH = symbols('WFH')  # Work From Home
Drive = symbols('Drive')  # Drive to work
PublicTransport = symbols('PublicTransport')  # Take public transport

# Task 3: Create the Knowledge Base (KB) - Propositional Logic Rules

# Rule 1: WFH if it's raining or there’s an early meeting.
rule_wfh = Implies(Or(Rain, EarlyMeeting), WFH)

# Rule 2: Drive if it’s not raining and there’s no heavy traffic.
rule_drive = Implies(And(Not(Rain), Not(HeavyTraffic)), Drive)

# Rule 3: PublicTransport if there’s no strike and it’s not raining.
rule_public_transport = Implies(And(Not(Strike), Not(Rain)), PublicTransport)

# Rule 4: Drive if there is an appointment in the afternoon.
rule_appointment_drive = Implies(Appointment, Drive)

# Rule 5: Avoid driving if there's road construction (we negate Drive).
rule_avoid_drive_construction = Implies(RoadConstruction, Not(Drive))

# Combine all rules into the Knowledge Base (KB)
KB = And(rule_wfh, rule_drive, rule_public_transport, rule_appointment_drive, rule_avoid_drive_construction)

# Task 4: Define Queries
def query_commute(option, conditions):
    """
    This function evaluates whether a certain commuting option (WFH, Drive, or PublicTransport)
    is suggested based on current conditions.

    :param option: The commuting option to query (WFH, Drive, PublicTransport).
    :param conditions: A dictionary of the current conditions (True or False values).
    :return: True if the option is suggested, otherwise False.
    """
    # Combine current conditions into the model
    model = And(
        *(symbols(condition) if state else Not(symbols(condition)) for condition, state in conditions.items())
    )

    # Check if the knowledge base and the model lead to the desired commuting option
    return satisfiable(And(KB, model, option)) is not False

# Task 5: Perform Model Checking with Different Scenarios
def evaluate_scenario(conditions):
    """
    This function checks the suggested commuting options (WFH, Drive, PublicTransport)
    based on the given conditions.

    :param conditions: A dictionary of the current conditions (True or False values).
    :return: None. Prints the suggested commuting options.
    """
    print(f"Conditions: {conditions}")
    if query_commute(WFH, conditions):
        print("Suggestion: Work from Home (WFH)")
    elif query_commute(Drive, conditions):
        print("Suggestion: Drive to work")
    elif query_commute(PublicTransport, conditions):
        print("Suggestion: Take Public Transport")
    else:
        print("No suitable commuting option found.")

# Task 6: Modify the Conditions and Check Scenarios

# Scenario 1: It’s raining, and there’s heavy traffic.
print("Scenario 1:")
conditions_1 = {
    'Rain': True,
    'HeavyTraffic': True,
    'EarlyMeeting': False,
    'Strike': False,
    'Appointment': False,
    'RoadConstruction': False
}
evaluate_scenario(conditions_1)

# Scenario 2: There’s a public transport strike, and it’s not raining.
print("\nScenario 2:")
conditions_2 = {
    'Rain': False,
    'HeavyTraffic': False,
    'EarlyMeeting': False,
    'Strike': True,
    'Appointment': False,
    'RoadConstruction': False
}
evaluate_scenario(conditions_2)

# Scenario 3: There’s no rain, traffic is light, and there’s no strike.
print("\nScenario 3:")
conditions_3 = {
    'Rain': False,
    'HeavyTraffic': False,
    'EarlyMeeting': False,
    'Strike': False,
    'Appointment': False,
    'RoadConstruction': False
}
evaluate_scenario(conditions_3)

# Task 7: Add More Rules and Recheck

# Scenario 4: You have an appointment and there's road construction.
print("\nScenario 4 (with new rules):")
conditions_4 = {
    'Rain': False,
    'HeavyTraffic': False,
    'EarlyMeeting': False,
    'Strike': False,
    'Appointment': True,
    'RoadConstruction': True
}
evaluate_scenario(conditions_4)
