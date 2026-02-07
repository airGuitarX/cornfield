# 玉米地

什么都可能有～的～玉米地～🌽～

Personal site built with [Hugo](https://gohugo.io/) and [hugo-theme-stack](https://github.com/CaiJimmy/hugo-theme-stack).

## Prerequisites

- [Hugo](https://gohugo.io/installation/) (extended version recommended for the theme)

## Setup

```bash
# Install Hugo (macOS)
brew install hugo

# Clone the repo and init theme submodule
git clone <repo-url> cornfield && cd cornfield
git submodule update --init --recursive
```

## Development

```bash
# Build site to ./public
hugo

# Local server (default: http://localhost:1313)
hugo server

# Include draft posts
hugo server -D

# Full rebuild (ignore cache)
hugo server --disableFastRender --ignoreCache

# Show effective config
hugo config
```

## Build for release

Build the site before pushing so `./public` is up to date:

```bash
hugo
```
