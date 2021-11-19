//////////////////////////////////////////////////////////////
// GET GITHUB API
//////////////////////////////////////////////////////////////

var getGithubBtn = document.querySelector(".get-github-btn");

getGithubBtn.addEventListener("click", async function() {
    console.log("**** In add event listener *****")
    fetch("https://api.github.com/users/adion81")
        .then(response => response.json() )
        .then(dataReceived => {
            console.log(dataReceived.name);
            var name = dataReceived.name;
            var pic = dataReceived.avatar_url
            var githubInfo = document.querySelector(".github-info");
            githubInfo.innerHTML = "<h2>Name: "+ name +"</h2>"
            var githubPic = document.querySelector(".github-pic");
            githubPic.innerHTML = "<img src=\"" + pic + "\"></img>";
            })
        .catch(err => console.log(err) )
})
