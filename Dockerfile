FROM python:3.10-slim

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    bash \
    bash-completion \
    wget \
    curl \
    unzip \
    gnupg \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Pythonの依存関係をインストール
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Chromeをインストール
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-signing-key.gpg && \
    sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# ChromeDriverをインストール
RUN wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.61/linux64/chromedriver-linux64.zip  && \
unzip chromedriver-linux64.zip  && \
mv chromedriver-linux64/chromedriver /usr/bin/chromedriver  && \ 
chown root:root /usr/bin/chromedriver  && \ 
chmod +x /usr/bin/chromedriver

# ソースコードをコピー
COPY src/ .

# bashをデフォルトシェルに設定
SHELL ["/bin/bash", "-c"]

# bash-completionを有効にする設定を追加
RUN echo "source /etc/bash_completion" >> ~/.bashrc

# エントリーポイントをbashに設定
ENTRYPOINT ["/bin/bash"]