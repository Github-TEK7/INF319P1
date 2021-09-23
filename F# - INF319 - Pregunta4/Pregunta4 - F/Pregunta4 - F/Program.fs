// Learn more about F# at http://fsharp.org

open System

[<EntryPoint>]
let main argv =
    
    //let lista =[1..10]
    let lista = [2;34;3;7;16;1;13;4;21;8]
    let listap = [ for i in lista do if i%2=0 then yield i ]
    let listai = [ for i in lista do if i%2<>0 then yield i ]

    printfn "La lista original es: %A" lista
    printfn "La lista de pares es: %A" listap
    printfn "La lista de impares es: %A" listai

    
    0 // return an integer exit code
