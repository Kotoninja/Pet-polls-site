var questionLengtText = document.querySelector(".question-length-counter");
var questionInput = document.querySelector("input[name='question']");


// console.log(questionLengtText)

function changeColor(length) {
    if (length < 25) {
        return "green";
    } else if (length >= 25 && length <= 40) {
        return "sandybrown";
    } else {
        return "red";
    };
};

function checkLength() {
    console.log(questionInput.value.length);
    questionLengtText.textContent = questionInput.value.length + '/50';
    questionLengtText.style.color = changeColor(questionInput.value.length);
};


questionInput.addEventListener('input', event => {
    if (questionInput.value.length <= 50) {
        checkLength();
    } else {
        event.preventDefault();
        alert('Стоп! Ваше значение превышает максимально допустимую длину!');
    };
});