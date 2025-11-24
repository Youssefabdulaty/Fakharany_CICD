console.log("App is running");


function greet(name){
    return `Hello, ${name}`
}

module.exports= greet;

if(require.main == module){
    console.log(greet("World"));
}