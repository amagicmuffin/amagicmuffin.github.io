function checkDarkmode() {
	console.log("got here");
	var r = document.querySelector(':root');
	var bgColor = getComputedStyle(r).getPropertyValue("--bg");

	console.log("cookie is " + document.cookie);
	if(document.cookie == "darkmode=Off") { // bg should be white
		console.log("switch TO DARK")
		r.style.setProperty('--bg', 'black');
		r.style.setProperty('--text', 'white');
	} else {
		console.log("switch TO LIGHT")
		r.style.setProperty('--bg', 'white');
		r.style.setProperty('--text', 'black');
	}
}

checkDarkmode();