var questionLengtText = document.querySelector(".question-length-counter");
var questionInput = document.querySelector("input[name='question']");


function changeColorQuestion(length) {
    if (length < 25) {
        return "green";
    } else if (length >= 25 && length <= 40) {
        return "sandybrown";
    } else {
        return "red";
    };
};

function checkLength() {
    questionLengtText.textContent = questionInput.value.length + '/50';
    questionLengtText.style.color = changeColorQuestion(questionInput.value.length);
};


questionInput.addEventListener('input', event => {
    if (questionInput.value.length <= 50) {
        checkLength();
    } else {
        questionInput.value = questionInput.value.slice(0, -1);
        alert('Стоп! Ваше значение превышает максимально допустимую длину!');
    };
});