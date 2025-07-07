const jsonData = JSON.parse(document.getElementById("county-data").textContent)

var textCountChoices = document.querySelector(".count-choices");
var createButton = document.querySelector(".create-choice");
var countChoices = 0;

// Question creator
var creatorName = jsonData.creator
var creatorFild = document.querySelector(".creator");
var creatorInput = document.querySelector("input[name='creator']")

const listChoices = document.querySelector(".choices-list");
const blankValuse = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];


function changeColor() {
    if (countChoices < 6) {
        return "green";
    } else if (countChoices >= 6 && countChoices <= 8) {
        return "orange";
    } else {
        return "red";
    }
}

function newInputChoice() {
    if (countChoices < 10) {
        countChoices++;

        // check for available id
        if (blankValuse.length != 0) {
            numberId = blankValuse.pop();
        }

        // new div
        let newPlace = document.createElement("div");
        newPlace.id = "choice-set" + numberId;

        // input choice
        let newChoice = document.createElement("input");
        newChoice.type = "text";
        newChoice.placeholder = "Enter choice";
        newChoice.name = "choices";

        // delete choice button
        let newChoiceDeleteButton = document.createElement("button");
        newChoiceDeleteButton.type = "button";
        newChoiceDeleteButton.className = "choice-delete";
        newChoiceDeleteButton.value = numberId;

        // add icon for button
        let choiceDeleteButtonIcon = document.createElement("i");
        choiceDeleteButtonIcon.className = "bx bxs-trash";

        newChoiceDeleteButton.append(choiceDeleteButtonIcon);

        textCountChoices.textContent = countChoices + "/10";
        textCountChoices.style.color = changeColor();

        newChoiceDeleteButton.addEventListener("click", function () {
            if (countChoices > 2) {
                document.getElementById("choice-set" + newChoiceDeleteButton.value).remove();
                countChoices--;
                textCountChoices.textContent = countChoices + "/10";
                textCountChoices.style.color = changeColor();
                blankValuse.push(+newChoiceDeleteButton.value);
            } else {
                alert("Count number of choices at least two");
            };
        });

        newPlace.append(newChoice);
        newPlace.append(newChoiceDeleteButton);
        listChoices.append(newPlace);
    } else {
        alert("You have exceeded the count choice!");
    }
}

function changecreator() {
    if (creatorInput.value === creatorName) {
        creatorInput.value = 'Anonymous'
        creatorFild.textContent = "User: " + creatorInput.value
    } else {
        creatorInput.value = creatorName
        creatorFild.textContent = "User: " + creatorName
    }
};

newInputChoice();
newInputChoice();
createButton.addEventListener("click", newInputChoice);
creatorFild.addEventListener("click", changecreator)
