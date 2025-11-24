function greet(name){
    retun `Hello, ${name}`
}

module.exports= greet;

if(require.main == module){
    console.log(greet("World"));
}