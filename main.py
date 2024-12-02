import telebot
from LLM_helper import llm
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

def LLM_function(combined_message):
    # Define the prompt template for expense calculation and settlement
    template = '''
    You are a financial assistant tasked with settling shared expenses between a group of people.
    Your responsibilities are:
    1. Calculate the total costs incurred by each individual based on the input details.
    2. Determine how much each person owes or is owed to balance out the expenses.
    3. Minimize the number of transactions required to settle the balances.
    4. Present the results in a clear and structured format.

    Example Input:
    "Ali paid $60 for lunch, and Hassan's share was $25 and Sara's share was $15. Sara paid $90 for dinner, and Ali's share was $45."

    Example Output:
    - Total Costs:
      Ali: $45
      Hassan: $25
      Sara: $90
    - Simplified Settlements:
      - Ali should pay Sara $30.
      - Hassan should pay Sara $25.

    Now, process the following details and provide the output:
    {combined_message}
    '''

    # Create the prompt template and invoke the LLM
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"combined_message": combined_message}).content
    return response





# Create bot with the token
bot = telebot.TeleBot(os.getenv("Telegram_API_KEY"))

# Variable to store user data
user_data = []

# Start command
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Hello! I'm here to help you split the bill. To add a cost, use /add. When you're done, use /done.")

# Add messages to the list
@bot.message_handler(commands=['add'])
def add_expenses(message):
    bot.reply_to(message, "Please send the expenses you would like to add. Type /done when you are finished.")

# Store user messages in the list
@bot.message_handler(func=lambda message: True, content_types=['text'])
def calculate_Settlements(message):
    global user_data
    if message.text.startswith("/done"):
        combined_message = "\n".join(user_data)
        response = LLM_function(combined_message)
        bot.reply_to(message, f"{response}")
        user_data = []  # Reset the list
    elif not message.text.startswith("/"):  # Ignore other commands
        user_data.append(message.text)
        bot.reply_to(message, f"Added: {message.text}")

bot.polling()
