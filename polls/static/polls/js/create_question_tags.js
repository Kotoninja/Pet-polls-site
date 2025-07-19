var tagsField = document.querySelector('.tags-list');
var tagInput = document.querySelector(".input-tag");
var tagAdd = document.querySelector(".add-tag");

function addTagToField (){
    if (tagInput.value) {
        // Create new div
        var newDiv = document.createElement("div");
        newDiv.className = "added-tag"

        // New Tag title
        var tagNew = document.createElement("p");
        tagNew.textContent = "#" + tagInput.value;
        tagInput.value = '';
    
        // Add button
        var removeButton = document.createElement("button");
        removeButton.type = "button";

        // Remove Tag icon
        var tagIcon = document.createElement("i");
        tagIcon.className = "bi bi-x-square-fill";

        removeButton.appendChild(tagIcon)

        newDiv.appendChild(tagNew);
        newDiv.appendChild(removeButton);
        
        tagsField.appendChild(newDiv);

        function removeTag() {
            newDiv.remove()
        }
        removeButton.addEventListener("click", removeTag);
    };
};


tagAdd.addEventListener("click", addTagToField);
tagInput.addEventListener("keydown", function (action) {
    if (action.key == "Enter") {
        console.log(action.key)
        action.preventDefault();
        addTagToField();
    }
})