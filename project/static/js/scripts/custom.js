/* Filename: custom.js */


/** DOM attribute
classname, tagName, id, href, title, rel, src
**/

/** Get Attrribute value **/
function myFunction1() {
    var x = document.getElementById("username");
    x.value = x.value.toUpperCase();

    /*document.getElementById('password').value='text to be displayed' ; */
	document.getElementById('password').value=x.value ; 
 };

/** set Attrribute value **/
function myFunction2() {
	document.getElementById("password").setAttribute("value", "http://www.w3schools.com"); 
};

/** set(chaange) Attrribute type **/
function myFunction3() {
    document.getElementsByTagName("INPUT")[1].setAttribute("type", "button"); 
};


/** Interaction , drag and down  **/
$(document).ready(function() {
    $( "#draggable" ).draggable();
 });

/* tag name <p> */
/*
$(document).ready(function() {
    $("p").css("background-color", "yellow");
});
*/

/* tag id Selects a single element with the given id myid.*/
$(document).ready(function() {
    $("#mydiv1").css("background-color", "blue");
});



/* Tag Class   class id ".classid"  - Selects all the elements with the given class ID big.*/
$(document).ready(function() {
    $(".big").css("background-color", "red");
});

$(document).ready(function() {
    $(".small").css("background-color", "yellow");
});

$(document).ready(function() {
    $("#mydiv2").css("background-color", "red");
});

$(document).ready(function() {
   	$(".medium, #mydiv2").css("background-color", "green");
});


/** JQuery DOM Filter Methods   **/
/** select from list by index  **/
$(document).ready(function() {
	$("li").eq(2).addClass("selected");
 });

 $(document).ready(function() {
   	$("li").filter(".middle").addClass("selected");
 });


/** DOM Manipulation Methods https:// www.tutorialspoint.com/jquery/jquery-dom.htm **/
/** DOM Element Replacement **/
$(document).ready(function() {
    $("#mydiv2").click(function () {
    	$(this).replaceWith("<h1>JQuery is Great</h1>");
    });
});

/** Content Manipulation **/
$(document).ready(function() {
   $("#division").click(function () {
  		var content = $(this).html();
      	$("#result").text( content );
   	});
});


/** Events Handling .bind() ---- https://www.tutorialspoint.com/jquery/jquery-events.htm **/
$(document).ready(function() {
	$('.event').bind('click', 
		function( event ){alert('Hi there!');
    });
});



/** Showing and Hiding elements speed/callback https://www.tutorialspoint.com/jquery/jquery-effects.htm **/
$(document).ready(function() {
 	$("#show").click(function () {
      	$(".effect").show( 200 );

   	});

   	$("#hide").click(function () {
  		$(".effect").hide( 200 );
  	});
				
});



