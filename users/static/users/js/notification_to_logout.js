var form = document.forms.formLogout
var logoutButton = document.querySelector(".logout")

function confirmLogout() {
    var action = confirm("You want to logout?")
    if (action) {
        form.submit()
    }
}

logoutButton.addEventListener("click", confirmLogout)