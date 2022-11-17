package main

import "fmt"

func main() {
	a := 123
	str := "welcome"

    fmt.Println("Hello, World!")
    fmt.Println("Code=%d&endDate=%s",a,str)
	
    var stockcode=123
    var enddate="2020-12-31"
    var url="Code=%d&endDate=%s"
    fmt.Println("Code=%d&endDate=%s",a,str)
    var target_url=fmt.Sprintf(url,stockcode,enddate)
    fmt.Println(target_url)
}