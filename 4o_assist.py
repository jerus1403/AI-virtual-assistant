import os
import signal
from utils import open_file, signal_handler
from modules import get_gpt_response, detect_intent, screen_to_text, recognize_speech, text_to_speech
from utils import open_file, signal_handler

# Load conversation context files
script_dir = os.path.dirname(os.path.abspath(__file__))
chat_bot_file_path = os.path.join(script_dir, 'chatbot.txt')
end_conv_context_path = os.path.join(script_dir, 'endConvContext.txt')
screen_context_path = os.path.join(script_dir, 'screenCheckContext.txt')

bot = open_file(chat_bot_file_path)
end_conv_context = open_file(end_conv_context_path)
screen_context = open_file(screen_context_path)


# ANSI escape codes for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


def main():
    prompt = recognize_speech()
    if prompt:
        response, end_conversation = get_gpt_response(
            prompt, bot, end_conv_context)

        print(f"\n{Colors.OKGREEN}David's Response: {response}{Colors.ENDC}")

        text_to_speech(response)
        if end_conversation:
            print("\nDetected end of conversation. Exiting...")
    print("Press Ctrl+C to exit.")
    while True:
        prompt = recognize_speech()
        if prompt:
            if detect_intent(prompt, screen_context):
                screen_text = screen_to_text()
                print(f"\nExtracted Text: {screen_text}")
                response, end_conversation = get_gpt_response(
                    screen_text, bot, end_conv_context)
            else:
                response, end_conversation = get_gpt_response(
                    prompt, bot, end_conv_context)

            print(f"\n{Colors.OKGREEN}David's Response: {
                  response}{Colors.ENDC}")

            text_to_speech(response)
            if end_conversation:
                print("Detected end of conversation. Exiting...")
                break


if __name__ == "__main__":
    main()
