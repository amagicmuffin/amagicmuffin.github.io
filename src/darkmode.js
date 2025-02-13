function checkDarkmode() {
	console.log("got here");
	let root = document.documentElement.style;
	// let bgColor = getComputedStyle(root).getPropertyValue("--bg");

	console.log("cookie is " + document.cookie);
	if(document.cookie == "darkmode=On") {
		console.log("switch TO DARK")
		root.setProperty('--bg', '#20384B');
		root.setProperty('--text', '#E1F2FF');
	} else {
		console.log("switch TO LIGHT")
		root.setProperty('--bg', 'white');
		root.setProperty('--text', 'black');
	}
}

checkDarkmode();