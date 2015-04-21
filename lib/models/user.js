function User() {
	this.name = "";
	this.age = -1;
}

User.prototype.print = function() {
	console.log("name = " + this.name);
	console.log("age = " + this.age);
}

module.exports = User
