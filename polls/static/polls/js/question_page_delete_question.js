var form = document.forms.change;
var deleteButton = document.querySelector('.delete');

function confirmDelete() {
    var action = confirm('Do you really want to delete the question?');
    if (action) {
        form.submit();
    };
};

deleteButton.addEventListener('click', confirmDelete);
