var form = document.forms.change;
var deleteButton = document.querySelector('.delete')
var editButton = document.querySelector('.edit')

console.log(form)

function confirmDelete() {
    var action = confirm('Do you really want to delete the question?');
    // console.log(action)
    if (action) {
        form.submit();
    }
}

function changeQuestion() {
    alert('This function are disable!')
}

deleteButton.addEventListener('click', confirmDelete);
editButton.addEventListener('click',changeQuestion)