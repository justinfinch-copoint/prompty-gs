# Use the official Python devcontainer image
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ARG TZ
ENV TZ="$TZ"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    less \
    procps \
    sudo \
    fzf \
    zsh \
    man-db \
    unzip \
    gnupg2 \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Set `DEVCONTAINER` environment variable to help with orientation
ENV DEVCONTAINER=true

# Create workspace and config directories
RUN mkdir -p /workspace /home/vscode/.claude /commandhistory

# Persist bash history
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && touch /commandhistory/.bash_history \
    && chown -R vscode:vscode /commandhistory

# Set working directory
WORKDIR /workspace

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy and set up post-create script
COPY post-create.sh /tmp/post-create.sh
RUN chmod +x /tmp/post-create.sh

# Set environment variables
ENV CLAUDE_CONFIG_DIR=/home/vscode/.claude
ENV SHELL=/bin/zsh

# Set ownership of workspace and config directories
RUN chown -R vscode:vscode /workspace /home/vscode/.claude

# Switch to vscode user for shell setup
USER vscode

# Set up zsh with powerline10k theme and enhancements
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.0/zsh-in-docker.sh)" -- \
  -p git \
  -p fzf \
  -a "source /usr/share/doc/fzf/examples/key-bindings.zsh" \
  -a "source /usr/share/doc/fzf/examples/completion.zsh" \
  -a "export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  -x

USER vscode
 