# Expense Splitter Bot

Expense Splitter Bot is a Telegram bot (@donghelperbot) designed to simplify the process of splitting bills among a group of people. Using AI-powered logic, the bot calculates each individual's share, determines who owes whom, and minimizes the number of transactions required for settlement.

## Features

- Add multiple expenses and contributors.
- Automatically calculate individual totals and settlements.
- Simplify transactions to minimize payments.
- Easy-to-use Telegram interface.

---

## Setup

### Prerequisites

- Python 3.8 or higher.
- A Telegram bot token. You can obtain one by creating a bot with [BotFather](https://core.telegram.org/bots#botfather).
- An OpenAI API key (if using an LLM for calculations).
- Libraries specified in `requirements.txt`.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/expense-splitter-bot.git
   cd expense-splitter-bot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your API keys:

   ```
   Telegram_API_KEY=your_telegram_bot_token
   OpenAI_API_KEY=your_openai_api_key
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

---

## Usage

1. **Start the Bot**:

   - Type `/start` to initiate the conversation with the bot.
   - The bot will greet you and provide usage instructions.

2. **Add Expenses**:

   - Use `/add` to enter expense details (e.g., _"Ali paid $60 for lunch, and Hassan's share was $25 and Sara's share was $15."_).
   - When finished adding expenses, type `/done`.

3. **View Settlements**:
   - After typing `/done`, the bot calculates the total costs for each person and provides a simplified list of who should pay whom.

---

## Example Interaction

**User Input**:

```
/start
/add
Ali paid $60 for lunch, and Hassan's share was $25 and Sara's share was $15.
Sara paid $90 for dinner, and Ali's share was $45.
/done
```

**Bot Output**:

```
- Total Costs:
  Ali: $45
  Hassan: $25
  Sara: $90

- Simplified Settlements:
  - Ali should pay Sara $30.
  - Hassan should pay Sara $25.
```

---

## Files in the Repository

- **`bot.py`**: The main script for running the Telegram bot.
- **`LLM_helper.py`**: A utility script for interacting with the LLM for calculations.
- **`.env`**: Contains API keys for Telegram and OpenAI (excluded in `.gitignore`).
- **`requirements.txt`**: Lists all required Python dependencies.

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature-name'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- [OpenAI](https://openai.com) for the LLM integration.
- [Telegram](https://telegram.org) for their easy-to-use bot API.
