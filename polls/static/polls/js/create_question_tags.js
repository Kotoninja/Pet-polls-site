var tagsField = document.querySelector('.tags-list');
var tagInput = document.querySelector(".input-tag");
var tagAdd = document.querySelector(".add-tag");

function addTagToField() {
    if (tagInput.value) {
        // Create new div
        const newDiv = document.createElement("div");
        newDiv.className = "added-tag";

        // Create hidden input
        const hiddenInput = document.createElement("input");
        hiddenInput.type = "hidden";
        hiddenInput.name = "tags";
        hiddenInput.value = tagInput.value;


        // New Tag title
        const tagNew = document.createElement("p");
        tagNew.textContent = "#" + tagInput.value;
        tagInput.value = '';

        // Add button
        const removeButton = document.createElement("button");
        removeButton.type = "button";

        // Remove Tag icon
        const tagIcon = document.createElement("i");
        tagIcon.className = "bi bi-x-square-fill";

        removeButton.appendChild(tagIcon);

        newDiv.appendChild(hiddenInput);
        newDiv.appendChild(tagNew);
        newDiv.appendChild(removeButton);

        tagsField.appendChild(newDiv);

        function removeTag() {
            newDiv.remove();
        };
        removeButton.addEventListener("click", removeTag);
    };
};


tagAdd.addEventListener("click", addTagToField);
tagInput.addEventListener("keydown", function (action) {
    if (action.key == "Enter") {
        action.preventDefault();
        addTagToField();
    };
});