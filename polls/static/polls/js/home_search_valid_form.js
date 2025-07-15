var form = document.querySelector(".searchForm");
var searchString = document.querySelector("input[name='search']");
var button = document.querySelector(".submitForm");


function isValid() {
    if (searchString.value) {
        console.log('form')
        form.submit();
    };
};

button.addEventListener("click", isValid);