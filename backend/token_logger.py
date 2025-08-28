# backend/token_logger.py
import tiktoken
from datetime import datetime

def log_tokens(model: str, prompt: str, response: str):
    """
    Logs the number of tokens used in prompt + response
    Prints to console and appends to backend/logs/token_usage.log
    """
    # load encoder for the given model
    encoding = tiktoken.encoding_for_model(model)

    prompt_tokens = len(encoding.encode(prompt))
    response_tokens = len(encoding.encode(response))
    total_tokens = prompt_tokens + response_tokens

    log_line = (
        f"[{datetime.now()}] "
        f"Prompt Tokens: {prompt_tokens} | "
        f"Response Tokens: {response_tokens} | "
        f"Total Tokens: {total_tokens}"
    )

    # print to terminal
    print(log_line)

    # also save to logs/token_usage.log
    with open("backend/logs/token_usage.log", "a", encoding="utf-8") as f:
        f.write(log_line + "\n")

    return total_tokens
