//reference
var database = firebase.database().ref();

//Button's actions
function sendMessage(){
	var name = $("#name").val();
	var message = $("#message").val();
	//send to your database
	database.push({
		'NAME': name,
		'MESSAGE': message
	});
}
	database.on('child_added',function(dataRow){
		var row = dataRow.val();
		$("#messageBoard").append("<p>" + row.NAME + ": " + row.MESSAGE);
	})