let userBalance = 100;
let transactions = Array(10).fill("NA");

function checkPIN() {
    const pin = document.getElementById("pin-input").value;
    const pinMessage = document.getElementById("pin-message");
    
    if (pin === '1212') {
        pinMessage.innerText = "Correct PIN";
        document.getElementById("pin-section").style.display = "none";
        document.getElementById("banking-section").style.display = "block";
    } else {
        pinMessage.innerText = "Incorrect PIN. Try again.";
    }
}

function displayBalance() {
    document.getElementById("balance").innerText = `Balance: $${userBalance}`;
}

function showWithdrawForm() {
    document.getElementById("withdraw-form").style.display = "block";
}

function withdrawFunds() {
    const amount = parseInt(document.getElementById("withdraw-amount").value);
    if (amount <= userBalance && amount > 0 && amount % 10 === 0) {
        userBalance -= amount;
        addTransaction(`Withdraw $${amount}`);
        document.getElementById("withdraw-message").innerText = `Successfully withdrawn $${amount}, new balance is $${userBalance}`;
    } else {
        document.getElementById("withdraw-message").innerText = "Invalid amount or insufficient funds.";
    }
    document.getElementById("withdraw-form").style.display = "none";
}

function showDepositForm() {
    document.getElementById("deposit-form").style.display = "block";
}

function depositFunds() {
    const amount = parseInt(document.getElementById("deposit-amount").value);
    if (amount > 0) {
        userBalance += amount;
        addTransaction(`Deposit $${amount}`);
        document.getElementById("deposit-message").innerText = `Successfully deposited $${amount}, new balance is $${userBalance}`;
    } else {
        document.getElementById("deposit-message").innerText = "Invalid amount. Please enter a positive number.";
    }
    document.getElementById("deposit-form").style.display = "none";
}

function printTransactions() {
    const transactionsList = document.getElementById("transactions-list");
    transactionsList.innerHTML = "";
    transactions.forEach(transaction => {
        const listItem = document.createElement("li");
        listItem.textContent = transaction;
        transactionsList.appendChild(listItem);
    });
}

function addTransaction(transaction) {
    transactions = transactions.slice(1).concat(transaction);
}

function returnCard() {
    alert("Thank you for using A2Z Banking!");
    location.reload();
}
