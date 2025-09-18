# Expense Tracker (Python)

An interactive **Expense Tracker** built in **Python**. It allows users to **add, view, and delete expenses**, and supports **currency conversion** using real-time exchange rates. Expenses are stored in a **JSON file** for persistent data storage.

## Features

* **Add Expense** – Record expenses with `title`, `amount`, and `date`.
* **View Expenses** – See all your expenses in a neat list format.
* **Delete Expense** – Remove any expense by its ID.
* **Currency Conversion** – View your expenses in any supported currency using a real-time API (Fixer API).
* **Persistent Storage** – All expenses are saved in `expenses.json` using Python dictionaries and lists.
* **OOP-based Design** – Uses classes and objects for clean code structure.

## Make sure `expenses.json` exists. If you want to **start fresh**, remove all existing data from `expenses.json` so you can add your own expenses from scratch.

## Usage

1. Run the program:

```bash
python main.py
```

2. Interact with the menu:

```
1. View Expenses
2. Add Expense
3. Delete Expense
4. Convert Expense Currency
5. Exit
```

3. Follow prompts to **add, view, delete, or convert expenses**.

## Example `expenses.json` Format

```json
[
    {
        "id": 1,
        "title": "Coffee",
        "amount": 140,
        "date": "2025-09-18"
    },
    {
        "id": 2,
        "title": "Lunch",
        "amount": 350,
        "date": "2025-09-18"
    }
]
```

> **Tip:** Make sure every expense follows this structure for proper functionality.

## Technologies Used

* **Python 3**
* **JSON** for storage
* **Requests** library for API calls
* **OOP Concepts** – Classes and Objects

## Future Improvements(Coming Soon)

* Add **search/filter** expenses by date or title
* Add **total expenditure summary** in selected currency
* Integrate **more APIs** or offline currency rates