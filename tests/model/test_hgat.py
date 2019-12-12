"""
Test the Heterograph conv.
"""
from ..utils import make_hetero_graph
from gnn.model.hgat import HGAT


def test_hgat():

    g, feats = make_hetero_graph()

    attn_mechanism = {
        "atom": {"edges": ["b2a", "g2a"], "nodes": ["bond", "global"]},
        "bond": {"edges": ["a2b", "g2b"], "nodes": ["atom", "global"]},
        "global": {"edges": ["a2g", "b2g"], "nodes": ["atom", "bond"]},
    }
    attn_order = ["atom", "bond", "global"]
    in_feats = [feats[t].shape[1] for t in attn_order]

    model = HGAT(attn_mechanism, attn_order, in_feats)
    output = model(g, feats)
    assert tuple(output.shape) == (3,)
