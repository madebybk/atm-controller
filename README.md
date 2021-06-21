# ATM-Controller

ATM Controller is a simple ATM program with the following flow: *Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw*

## Clone Project

Clone the project using git command:

```bash
git clone https://github.com/madebybk/atm-controller.git
```

This command clones directory *atm_controller* to your local machine. Navigate into the directory with the command:

```bash
cd atm_controller
```

## Requirements

### Python3

[Python3](https://www.python.org/downloads/) must be installed on your machine.

Current Python version may be checked by:

```bash
python --version
```

## Program Process

### 1. Insert Card

The card insertion process is simulated with time.sleep() method.

### 2. PIN Number

A bank API would be implemented in the future to verify password, but at this point of the project, **_1234_** is used as the PIN. The program terminates if user enters incorrect PIN more than 3 consecutive times, and the user would need to restart the login process by reinserting the card.

### 3. Select Account

The program asks user to pick one of the following account options:

- *Checking Account*
- *Savings Account*
- *Finish Transaction*

The account type is saved if either *Checking Account* or *Savings Account* is picked, and the program process continues. If *Finish Transaction* is picked, the program will terminate with a goodbye message.

### 4. See Balance/Deposit/Withdraw

With the selected account type, the program asks user for their transaction action:

- *See Balance*
- *Deposit*
- *Withdraw*
- *Back to Select Account*
- *Finish Transaction*

The transaction action will execute once the user picks an option.

## Test Program

To run the program, enter the following in the root directory of the repository:

```bash
python3 atm_controller.py
```

As mentioned under *Program Process (Step 2)*, **_1234_** is the temporary PIN for this project.
