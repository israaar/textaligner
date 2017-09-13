
function demux_text(aligned_text){
	var result = ['', ''];
	for(var i=0; i < aligned_text.length; ++i){
		var section_class = (i%2 == 0) ? "text-span" : "text-span-alt";
		result[0] += '<span class="' + section_class + '">' + aligned_text[i][0] + '</span>' + '<br>';
		result[1] += '<span class="' + section_class + '">' + aligned_text[i][1] + '</span>' + '<br>';
	}
	
	return result;
}

function strip_html(text) {
	text = text.replace('<br>', '\n');
	text = text.replace(/<\/?.+?>/g, '');
	return text;
}