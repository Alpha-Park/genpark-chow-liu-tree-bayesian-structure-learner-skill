import sys
import json
from client import ChowLiuTreeLearner

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "learn":
        l = ChowLiuTreeLearner()
        return l.learn_tree(params.get("vars", []), params.get("mi_matrix", []))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
