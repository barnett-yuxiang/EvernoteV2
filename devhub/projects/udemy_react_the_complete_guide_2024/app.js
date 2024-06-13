// Class is rarely used
class User {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, I am ${this.name}`);
  }
}

const user = new User('Max', 30);
console.log(user);


// Arrays & Array Methods like map()
hobbies = ['Sports', 'Cooking', 'Reading'];
console.log(hobbies)
hobbies.push('Programming');
console.log(hobbies);

const index = hobbies.findIndex((item) => {
  return item === 'Cooking';
});
console.log(index);

const edditHobbies = hobbies.map((item) => item + "!");
console.log(edditHobbies);
