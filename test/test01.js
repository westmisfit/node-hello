var should = require("should")

describe('test01', function () {

  describe('addOne()', function () {

    it('should correctly add one to the given number', function () {
      // assertions here
    })

  })

  describe('subtractOne()', function () {

    it('should correctly subtract one from the given number', function () {
      // assertions here
    })

  })

  describe('Student', function () {

    var student = { classes: [ 'English', 'Maths', 'Science' ] }

    it('should have correct number of classes', function () {
      student.should.have.property('classes').with.lengthOf(3)
    })

  })

})