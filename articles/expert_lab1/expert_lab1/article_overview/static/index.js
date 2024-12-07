// function test(){
//     console.log("Hello World");
//     setTimeout(() => {
//         console.log("Hello World");
//     }, 1000);
//     alert("Hello World");
// }

// test();


openForm = () => {
    let form = document.getElementById("addForm");
    console.log(form);
    document.getElementById("addForm").style.display = "block";
};

closeForm = () => {
    document.getElementById("addForm").style.display = "none";
};