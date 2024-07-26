let user = {
  id: 123,
  userName : "junior",
  senha: 12345,
  admin: true
}

// console.log(user.senha)

if (user.id === 123 && user.userName === "junior"){
  console.log("ID ou nome válido")
}else {
  console.log("ID ou nome inválido")
}

console.log("--------------------------------")
if (user.userName === "junioir"|| user.senha === "12345"){
  console.log("ID ou nome válido")
}else {
  console.log("ID ou nome inválido")
}

console.log("--------------------------------")
if(user.admin){
  console.log("Acesso permitido")
}else{
  console.log("Acesso negado")
}