# 飯番 meshiban

## 概要

今日飯を作るやつを決めるDiscord BOT

## 技術スタック

- language: python 3.12
- libraryManager: UV
- library: Discord.py
- fmt & lint: ruff
- test: pytest
- infra: なおき

## 環境構築

`mise` をローカルにインストール (Debian/Ubuntu 系の場合)

```bash
sudo apt update -y && sudo apt install -y curl
sudo install -dm 755 /etc/apt/keyrings
curl -fSs https://mise.jdx.dev/gpg-key.pub | sudo tee /etc/apt/keyrings/mise-archive-keyring.asc 1> /dev/null
echo "deb [signed-by=/etc/apt/keyrings/mise-archive-keyring.asc] https://mise.jdx.dev/deb stable main" | sudo tee /etc/apt/sources.list.d/mise.list
sudo apt update -y
sudo apt install -y mise
```

プロジェクトの `.mise.toml` から依存関係をインストール

```bash
mise install
```

プロジェクトを `mise` で構築

```bash
mise run setup
```
