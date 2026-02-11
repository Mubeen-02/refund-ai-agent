
import re

def parse_refund_request(user_text):
    """
    Extracts structured information from a refund request.
    """
    order_id_match = re.search(r"\b\d{5,}\b", user_text)

    return {
        "order_id": order_id_match.group(0) if order_id_match else None,
        "reason": user_text.lower(),
        "raw_text": user_text
    }
