
from langgraph.graph import StateGraph, END

from request_parser import parse_refund_request
from policy_retriever import retrieve_policy
from validator import validate_request
from decision_maker import make_decision
from responder import generate_response


def request_parser_node(state):
    state["parsed"] = parse_refund_request(state["user_input"])
    return state


def policy_retrieval_node(state):
    state["policies_matched"] = retrieve_policy(
        state["parsed"]["reason"],
        state["embedding_model"],
        state["index"],
        state["policies"]
    )
    return state


def validation_node(state):
    state["validation"] = validate_request(
        state["parsed"],
        state["policies_matched"] # Changed from state["policy"]
    )
    return state


def decision_node(state):
    state["decision"] = make_decision(state["validation"])
    return state


def response_node(state):
    state["response"] = generate_response(
        state["decision"],
        state["policies_matched"] # Changed from state["policy"]
    )
    return state


def build_refund_graph():
    graph = StateGraph(dict)

    graph.add_node("parse_request", request_parser_node)
    graph.add_node("retrieve_policy", policy_retrieval_node)
    graph.add_node("validate", validation_node)
    graph.add_node("decide", decision_node)
    graph.add_node("respond", response_node)

    graph.set_entry_point("parse_request")

    graph.add_edge("parse_request", "retrieve_policy")
    graph.add_edge("retrieve_policy", "validate")
    graph.add_edge("validate", "decide")
    graph.add_edge("decide", "respond")
    graph.add_edge("respond", END)

    return graph.compile()
