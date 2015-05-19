var should = require("should")
var User = require("../lib/models/user")

describe('testUser', function () {

  describe('create', function () {

    var user = new User();
    user.name = "bob";
    user.age = 18;
    user.print();

    it('should correctly add one to the given number', function () {
      user.should.have.property('name').equal("bob");
      user.should.have.property('age').equal(18);
    })

  })

})