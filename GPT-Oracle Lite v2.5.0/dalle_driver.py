import openai

def receive_draw_input(api_key, message):
    # Check message length early and return if it exceeds the limit
    if len(message) > 400:
        return "Input prompt was too long, please try again. Max limit is 400 characters."

    # Set API key
    openai.api_key = api_key

    # Generate the image and return its URL
    response = openai.Image.create(
        prompt=message,
        n=1,
        size="1024x1024",
    )
    
    # Clear API key
    openai.api_key = None

    return response["data"][0]["url"]