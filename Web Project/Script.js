var database = firebase.database().ref();
//Button's actions
function sendMessage(){
	var message = $("#message").val();
	//send to your database
	database.push({
		'MESSAGE': message
	});
}
	// database.on('child_added',function(dataRow){
	// 	var row = dataRow.val();
	// 	$("#messageBoard").append("<p>" + row.MESSAGE + "</p>");
	// })
