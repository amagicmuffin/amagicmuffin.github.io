quotes = [
    ["https://backrooms-wiki.wikidot.com/entity-71", "A broken ring of mail"],
    ["https://backrooms-wiki.wikidot.com/entity-71", "erstwhile"],
    ["https://backrooms-wiki.wikidot.com/entity-71", "a finger of an arm of a body that died eons ago."],
    ["https://www.google.com/search?q=Adib+Sin+-+To+Eternity", "you were dancing to a thousand stars"],
];



window.onload = function() {
    quote = quotes[Math.floor(Math.random()*quotes.length)];
    
    document.getElementById("quote").innerHTML += ` <a href=\"${quote[0]}\">${quote[1]}</a>`;
};
