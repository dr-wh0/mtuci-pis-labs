
var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        console.log("you clicked", e.target);

//        event.target.parentElement.getElementsByClassName('article-author')[0].style.display = "none";
//        event.target.parentElement.getElementsByClassName('article-created-date')[0].style.display = "none";
//        event.target.parentElement.getElementsByClassName('article-text')[0].style.display = "none";
//        event.target.innerHTML = "развернуть";

//        if (e.target.className == "fold-button folded") {
//            e.target.innerHTML = "свернуть";
//            e.target.className = "fold-button";
//            var displayState = "block";
//        } else {
//            e.target.innerHTML = "развернуть";
//            e.target.className = "fold-button folded";
//            var displayState = "none";
//        }
//        e.target.parentElement
//            .getElementsByClassName('article-author')[0]
//            .style.display = displayState;
//        e.target.parentElement
//            .getElementsByClassName('article-created-date')[0]
//            .style.display = displayState;
//        e.target.parentElement
//            .getElementsByClassName('article-text')[0]
//            .style.display = displayState;

        var post = e.target.closest('.one-post');
        post.classList.toggle('folded');
        if (post.classList.contains('folded')) {
            e.target.textContent = 'развернуть';
        } else {
            e.target.textContent = 'свернуть';
        }
    })
};
