const defaultResult =  0;
let currentResult = defaultResult;
let logEntries = [];

// Gets input from input field
// 입력 필드에서 입력값 가져옴
function getUserNumberInput() {
    return parseInt(userInput.value);
}

// Generates and wirtes calculation
// 계산 로그 생성과 작성
function createAndWriteOutPut(operator, resultBeforeCalc, calcNumber) {
    const calcDescription = `${resultBeforeCalc} ${operator} ${calcNumber}`;
    outputResult(currentResult, calcDescription); // from vendor.js
}


function add() {
    const enteredNumber = getUserNumberInput();
    const initialResult = currentResult;
    currentResult += enteredNumber;
    createAndWriteOutPut('+', initialResult, enteredNumber)
    logEntries.push(enteredNumber);
    console.log(logEntries[1]);
}

function subtract() {
    const enteredNumber = getUserNumberInput();
    const initialResult = currentResult;
    currentResult -= enteredNumber;
    createAndWriteOutPut('-', initialResult, enteredNumber);
}

function multiply() {
    const enteredNumber = getUserNumberInput();
    const initialResult = currentResult;
    currentResult *= enteredNumber;
    createAndWriteOutPut('*', initialResult, enteredNumber);
}

function divide() {
    const enteredNumber = getUserNumberInput();
    const initialResult = currentResult;
    currentResult /= enteredNumber;
    createAndWriteOutPut('/', initialResult, enteredNumber);
}

addBtn.addEventListener('click', add);
subtractBtn.addEventListener('click', subtract);
multiplyBtn.addEventListener('click', multiply);
divideBtn.addEventListener('click', divide);