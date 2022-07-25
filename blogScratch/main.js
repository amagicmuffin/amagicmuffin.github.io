// TODO yknow what just do this in python during build.bat

let blogPosts = [
    {
        title: "Blog One",
        link: "blogPosts/blog1.html",
        description: "the first blog post",
    },
    {
        title: "Blog Two",
        link: "blogPosts/blog2.html",
        description: "the second blog post",
    },
]

let HTML = "";

blogPosts.forEach((d,i) => {
    HTML += `<a href="${d.link}">${d.title}</a> ${d.description} <br>`;
})

document.getElementById("site-container").innerHTML = HTML;