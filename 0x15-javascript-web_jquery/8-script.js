const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json' function (data, textStatus) {
	const ttl = data.results;
	for (let i = 0; i < ttl.length; i++) {
		$('UL#list_movies').append('<li>' + ttl[i].title + '</li>');
	}
});
