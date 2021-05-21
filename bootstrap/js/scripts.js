const isValidEmail = (email) => {
  const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
};
const form = document.querySelector('form');
const thankYou = document.querySelector('.thank-you');
const contact = document.querySelector('.contact');
const nameInput = document.querySelector('input[name="nombreF"]');
const emailInput = document.querySelector('input[name="emailF"]');
const subjectInput = document.querySelector('input[name="asuntoF"]');
const messageInput = document.querySelector('textarea[name="mensajeF"]');
let isFormValid = false;
let isValidationOn = false;

const inputs = [nameInput, emailInput, subjectInput, messageInput];

const resetElm = (elm) => {
	elm.classList.remove('invalid');
	elm.nextElementSibling.classList.add("hidden");
};
const invalidateElm = (elm) => {
	elm.classList.add("invalid");
	elm.nextElementSibling.classList.remove("hidden");
};

const validateInputs = () => {
	if (!isValidationOn) return;
	isFormValid = true;
	resetElm(nameInput);
	resetElm(emailInput);
	resetElm(subjectInput);
	resetElm(messageInput);

	if (!nameInput.value){
		invalidateElm(nameInput);
		isFormValid = false;
	}
	if (!isValidEmail(emailInput.value)){
		invalidateElm(emailInput);
		isFormValid = false;
	}
	if (!subjectInput.value){
		invalidateElm(subjectInput);
		isFormValid = false;
	}
	if (!messageInput.value){
		invalidateElm(messageInput);
		isFormValid = false;
	}
};

form.addEventListener('submit', (e) => {
	e.preventDefault();
	isValidationOn = true;
	validateInputs();
	if (isFormValid) {
		contact.classList.add("hidden");
		form.remove();
		thankYou.classList.remove("hidden");
	}
});

inputs.forEach(input => {
	input.addEventListener("input", () =>{
		validateInputs();
	});
});

function initMap(){
	var options = {
		zoom:15,
		center:{lat:-33.462352822082, lng:-70.58612291833506}
	};

	var map = new google.maps.Map(document.getElementById('map'), options);

	var marker = new google.maps.Marker({
		position:{lat:-33.462352822082, lng:-70.58612291833506},
		map:map
	});
}