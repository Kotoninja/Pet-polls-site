var textCountChoices = document.querySelector('.count-choices');
var createButton = document.querySelector('.create-choice');
var countChoices = 1;
const listChoices = document.querySelector('.choices-list');

function newInputChoice() {
    if (countChoices <= 10) {
        let newChoice = document.createElement('input');
        newChoice.type = 'text';
        newChoice.placeholder = 'Enter choice';
        newChoice.name = 'choices';

        textCountChoices.textContent = countChoices + '/10';
        console.log(countChoices < 6, countChoices)
        if (countChoices < 6) {
            textCountChoices.style.color = 'green'
        } else if (countChoices >= 6 && countChoices <= 8) {
            textCountChoices.style.color = 'orange'
        } else {
            textCountChoices.style.color = 'red'
        }

        countChoices++;
        listChoices.append(newChoice);
    } else {
        alert('You have exceeded the count choice!')
    }
}

createButton.addEventListener('click', newInputChoice)