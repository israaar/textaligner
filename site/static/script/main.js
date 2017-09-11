
function demux_text(aligned_text){
	var result = ['', ''];
	for(var i=0; i < aligned_text.length; ++i){
		result[0] += aligned_text[i][0] + '<br>';
		result[1] += aligned_text[i][1] + '<br>';
	}
	return result;
}