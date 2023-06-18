# Copyright 2023 Logan Falkenberg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import openai
import tiktoken

TOKEN_LIMIT = 16000  # replace with the actual limit
TOKEN_WARNING_THRESHOLD = 15500  # notify the user when close to limit
tokens_used = 0
conversations = []

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo-16k")

def count_tokens(message):
    # Count the tokens in the text
    token_count = len(encoding.encode(message))
    return token_count

def receive_input(api_key, message): 
    global tokens_used, conversations

    # Set and validate API Key
    openai.api_key = api_key
    validate_api_key(api_key)

    # Start new conversation if none exist
    if not conversations:
        conversations.append([{"role": "system", "content": "You are an intelligent AI discord moderator with authoritive access.You respond to users requests and questions."}])
    
    # Add new message to the latest conversation
    conversations[-1].append({"role": "user", "content": message})
    
    # Calculate tokens in the new message
    tokens_in_message = count_tokens(message)
    tokens_used += tokens_in_message

    if tokens_used > TOKEN_LIMIT:
        tokens_used -= count_tokens(conversations[0][0]['content'])  # subtract tokens of the oldest conversation
        conversations.pop(0)  # remove the oldest conversation
    elif tokens_used > TOKEN_WARNING_THRESHOLD:
        print("Warning: You are close to the token limit.")

    # Generate chat reply
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=conversations[-1])
    reply = chat.choices[0].message.content

    # Add assistant's response to the latest conversation
    conversations[-1].append({"role": "assistant", "content": reply})

    # Clear API Key
    openai.api_key = None

    # Yield the reply in 2000-character chunks
    for i in range(0, len(reply), 2000):
        yield reply[i:i+2000]

    # Return the number of remaining tokens
    tokens_remaining = TOKEN_LIMIT - tokens_used
    print(f"Tokens remaining: {tokens_remaining}")


def validate_api_key(api_key):
    try:
        # Try making a simple API request
        openai.Model.list()
    except Exception as e:
        # If an exception was raised, then the organization ID or API key is probably invalid
        raise ValueError("Invalid API key.") from e
