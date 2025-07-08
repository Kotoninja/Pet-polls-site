const jsonData = JSON.parse(document.getElementById("county-data").textContent)

// Question creator
var creatorName = jsonData.creator
var creatorFild = document.querySelector(".creator");
var creatorInput = document.querySelector("input[name='creator']")


function changecreator() {
    if (creatorInput.value === creatorName) {
        creatorInput.value = 'Anonymous'
        creatorFild.textContent = "User: " + creatorInput.value
    } else {
        creatorInput.value = creatorName
        creatorFild.textContent = "User: " + creatorName
    }
};

creatorFild.addEventListener("click", changecreator)
