from openai import OpenAI
import warnings
from config.settings import GPT_PIOT_API_KEY

client = OpenAI(api_key=GPT_PIOT_API_KEY)
conversations = []
# Ignore DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)


def get_gpt_response(user_input, bot, end_conv_context):
    conversations.append({
        "role": "user",
        "content": user_input,
    })
    messages_input = conversations.copy()
    prompt = [{
        "role": "system",
        "content": bot,
    }]
    messages_input.insert(0, prompt[0])

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,  # Adjust temperature for faster response
        top_p=0.8,
        messages=messages_input,
    )
    chat_response = response.choices[0].message.content

    conversations.append({
        "role": "assistant",
        "content": chat_response,
    })

    # Check for end conversation intent
    intent_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.0,
        messages=[
            {"role": "system", "content": end_conv_context},
            {"role": "user", "content": user_input}
        ],
    )

    end_conversation = intent_response.choices[0].message.content.strip(
    ).lower() == "yes"
    return chat_response, end_conversation


def detect_intent(user_input, screen_context):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[
            {"role": "system", "content": screen_context},
            {"role": "user", "content": user_input}
        ],
    )
    intent = response.choices[0].message.content.strip().lower()
    return intent == "yes"
