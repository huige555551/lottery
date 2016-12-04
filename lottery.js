var href ="http://live.aicai.com/zc/xyo_1249018_ouzhi.html"
$(document).ready(function(){
	$("#open_win").click(function(){
		var data = window.frames["test-iframe"].document;
		data.getElementsByClassName('jq_lottery_matchStatus').click();

			// document.getElementsByClassName('jq_lottery_matchStatus').click();
		
		// var download=window.onload(href);
		// console.log(download.document);
		// download.onload=function() {download.document.getElementsByClassName('jq_lottery_matchStatus').click();
		// };
		// download.onload();
		
	}
	)
})