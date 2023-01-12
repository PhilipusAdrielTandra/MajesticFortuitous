// Grabs the button class 'update-cart' from store.html
var updateBtns = document.getElementsByClassName('update-cart')

function checkloginstatus(){
	var login = document.getElementById("login");
	var logout = document.createElement("a");
	logout.className = "btn btn-dark";
	logout.href = "logout";
	logout.innerHTML = "Logout";
	if (user == 'AnonymousUser'){
		logout.replaceWith(login);
	}else{
		login.replaceWith(logout);
	}
}
window.onload = checkloginstatus;

//Loops through the variable of buttons to get its ID and action
for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		var login = document.getElementById('login')
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)
		//If statement for if the user is logged in or not, if the user is not logged in, he cannot purchase anything from the store
		if (user == 'AnonymousUser'){
			console.log('Not logged in')
		}else{
			updateUserOrder(productId, action)
		}
	})
}

//Update user function
function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data')
		//Goes to /update_tem/ from views.py and urls.py
		var url = '/update_item/'
		//Fetch api to get the resources from the server, this being the product id and action
		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				/*CSRF protection is used in django for protection against malicious attacks and essentially
				creates a token and ensures that requests are cross checked with said token*/
				'X-CSRFToken':csrftoken,
			}, 
			//Converts the values to a JSON format, essentially making it into a dictionary
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		//Returns the JSON response
		.then((response) => {
		   return response.json();
		})
		//Takes in the 'add' action and essentially ports it back to reload live as seen on the cart item number on the topright
		.then((data) => {
		    console.log('data:', data)
			location.reload()
		});
}