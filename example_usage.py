from client import ChowLiuTreeLearner

def main():
    print("=== Chow-Liu Tree Bayesian Structure Learner ===")
    learner = ChowLiuTreeLearner()
    vars = ["Age", "Income", "Education"]
    mi_mat = [
        [0.0, 0.45, 0.15],
        [0.45, 0.0, 0.72],
        [0.15, 0.72, 0.0]
    ]

    res = learner.learn_tree(vars, mi_mat)
    print("Learned Tree Structure:", res)
    assert len(res["tree_edges"]) == 2
    assert res["total_mutual_information"] == 1.17

    print("Chow-Liu Tree Learner verified successfully!")

if __name__ == "__main__":
    main()
