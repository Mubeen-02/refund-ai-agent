
def generate_response(decision, policy):
    if decision == "APPROVE":
        return f"Your refund request has been approved based on the following policy: {policy}"
    elif decision == "REJECT":
        return f"Your refund request has been rejected due to this policy: {policy}"
    else:
        return "Your request requires further review and has been escalated to a human agent."
