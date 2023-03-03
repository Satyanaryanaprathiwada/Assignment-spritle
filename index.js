// let arr = [3, 6, 7, 18, 10, 13, 17, 15, 20]
// let result = arr.sort(function(a,b){
//     if(a>b) return 1
//     if(a<b) return -1
// })
// let index = result.length-2

// console.log(`Second largest number is ${result[index]}`)

// function higherOrder(fn)

//  {

//   fn();

// } 

// higherOrder(function() { console.log("Hello world") });




getDetails = async () => {
    const url = "https://randomuser.me/api/?results=50"
    const response = await fetch(url)
    const data = await response.json()
    console.log(data)
}


getDetails()

