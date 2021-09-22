// Learn more about F# at http://fsharp.org

open System

let function5 x y =
  let mutable s=0
  for i in (1) .. (y) do
    s<-s+x
  s


[<EntryPoint>]
let main argv =
    
    let a=function5 5 7
    printfn "Multipliacion: 5*7=%i" a

    0 // return an integer exit code
