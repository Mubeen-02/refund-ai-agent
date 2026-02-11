
def validate_request(parsed_request, matched_policies):
    text = " ".join(matched_policies).lower()

    if parsed_request["order_id"] is None:
        return "ESCALATE"

    if "not allowed" in text or "not permitted" in text:
        return "REJECT"

    if "allowed" in text:
        return "APPROVE"

    return "ESCALATE"
