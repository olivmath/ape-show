# Introduction to Blockchain with Python

## Quickstart Guide

### Setup environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

```bash
poetry init
poetry shell
```

### Install dependencies

**Ape Worx**

```bash
pip3 install eth-ape
pip3 install ape-solidity
pip3 install ape-vyper
```

```bash
poetry add eth-ape
poetry add ape-solidity
poetry add ape-vyper
```

```
ape run deploy --network ethereum:anvil:node
```

## Development 15min

- Defining the project
- Writing smart contract
- Testing smart contract
- Deploying smart contract
- Interacting with smart contract

## Conclusion 3min

- Learnings and contribution
- Next steps
