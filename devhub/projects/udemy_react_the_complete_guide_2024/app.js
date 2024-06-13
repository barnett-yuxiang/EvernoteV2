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

const user = new User("Max", 30);
console.log(user);

// Arrays & Array Methods like map()
hobbies = ["Sports", "Cooking", "Reading"];
console.log(hobbies);
hobbies.push("Programming");
console.log(hobbies);

const index = hobbies.findIndex((item) => {
  return item === "Cooking";
});
console.log(index);

const edditHobbies = hobbies.map((item) => item + "!");
console.log(edditHobbies);

const anotherEdditHobbies = hobbies.map((item) => ({ text: item }));
console.log(anotherEdditHobbies);

// Destructuring
const [firstName, lastName] = ["Max", "Schwarz"];
console.log(firstName, lastName);

const { name: userName, age } = {
  name: "Max",
  age: 30,
};

console.log(userName, age);

// The Spread Operator
const newHobbies = ["GYM"];
const mergedHobbies = [...hobbies, ...newHobbies];
console.log(mergedHobbies);

const person = {
  name: "Max",
  age: 30,
};

const extendedPerson = {
  isAdmin: true,
  ...person,
};
console.log(extendedPerson);

// Revisiting Control Structures
for (const hb of hobbies) {
  console.log(hb);
}

// Using Functions as Values
function handleTimeOut() {
  console.log("Time out!");
}

const handleTimeOut2 = () => {
  console.log("Time out ... agent!");
};

setTimeout(handleTimeOut, 2000);
setTimeout(handleTimeOut2, 3000);
setTimeout(() => {
  console.log("Time out ... anonymous!");
}, 4000);
