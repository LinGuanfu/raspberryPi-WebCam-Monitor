
In_image = function(){
	var verifImg = document.getElementById("Inside");
	$.ajax({
	    type:'GET',
	    url:'/Pi_image',
	    success: function() {
		verifImg.setAttribute('src', "Pi_image");
		console.log("Image Refresh succussed!");
	    },
	    error: function() {
		verifImg.setAttribute("src", "Pi_image");
	    }
	});
}

Out_image = function(){
	var verifImg = document.getElementById("Outside");
	$.ajax({
	type:'GET',
	    url:'/Usb_image',
	    success: function() {
		verifImg.setAttribute("src", "Usb_image");
		console.log("Image Refresh succussed!");
	    },
	    error: function() {
		verifImg.setAttribute("src", "Usb_image");
		}
	});
}

