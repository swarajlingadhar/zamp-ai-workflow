def find_category(message):
    message = message.lower()

    if "payment" in message or "transaction" in message:
        return "Payment Issue"

    if "password" in message or "login" in message:
        return "Account Issue"

    if "refund" in message:
        return "Refund"

    return "General Query"


def find_priority(message):
    message = message.lower()

    if "fraud" in message or "urgent" in message:
        return "High"

    if "failed" in message or "error" in message:
        return "Medium"

    return "Low"


def assign_team(category):
    if category == "Payment Issue":
        return "Payments Team"

    if category == "Account Issue":
        return "Account Support"

    if category == "Refund":
        return "Refund Team"

    return "General Support"


def generate_response(category):
    responses = {
        "Payment Issue": "Our payments team will review your issue.",
        "Account Issue": "Our account support team will help you.",
        "Refund": "Our refund team will check your request.",
        "General Query": "Our support team will review your request."
    }

    return responses[category]