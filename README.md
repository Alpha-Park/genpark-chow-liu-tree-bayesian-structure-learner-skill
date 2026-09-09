# genpark-chow-liu-tree-bayesian-structure-learner-skill

[![Agentic Skill](https://img.shields.io/badge/GenPark-Agentic__Skill-blue.svg)](https://github.com/Alpha-Park/genpark-chow-liu-tree-bayesian-structure-learner-skill)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20Pip-orange.svg)](#)
[![Dual Org Verified](https://img.shields.io/badge/GitHub-Dual__Org-purple.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Chow-Liu algorithm learning optimal tree-structured Bayesian Networks from mutual information matrices via maximum weight spanning trees.

## Architecture Overview

```mermaid
flowchart TD
    A[Agentic AI / Probabilistic Reasoner] -->|Joint Potentials & Observations| B[MCP Server / Client]
    B --> C[genpark-chow-liu-tree-bayesian-structure-learner-skill Inference Engine]
    C --> D[Variable Elimination / Factor Message Passing / Gibbs Spin Updates]
    D --> E[Exact & Approximate Posterior Marginals]
    E -->|Structured Output| A
```

## Features
- **0 External Pip Dependencies**: Pure Python standard library implementation.
- **MCP Protocol Ready**: Includes Model Context Protocol server script (`mcp_server.py`).
- **Production Standard**: Rigorous probabilistic normalization and convergence guarantees.

## Quick Start
```bash
python example_usage.py
```
